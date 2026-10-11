// Reseñas de Google (Places API New). Se piden UNA vez, al construir la web; la Action
// diaria (instagram-daily.yml) vuelve a publicar cada mañana, así que la calificación,
// el total y las reseñas se actualizan solos. Google devuelve como máximo 5 reseñas y
// elige cuáles ("más relevantes"): se muestran solo las de 5 estrellas con texto y, si no
// alcanzan, se completan con las fijas de home.ts. Si la API falla, todo queda como antes.
//
// Variables en Vercel: GOOGLE_PLACES_KEY (obligatoria) y GOOGLE_PLACE_ID (opcional; sin ella
// se busca el negocio por nombre en cada build).
import { reviews as staticReviews, googleReviews } from './home';

export type Review = { name: string; text: string; photo?: string };
export type ReviewsData = { rating: string; count: number; reviews: Review[]; href: string };

const SHOWN = 4; // 1 cita destacada + 3 tarjetas
const SEARCH_QUERY = 'Avinu Music & Productions';
const FIELDS = ['id', 'rating', 'userRatingCount', 'reviews', 'googleMapsUri'];

type PlaceReview = {
  rating?: number;
  text?: { text?: string };
  originalText?: { text?: string };
  publishTime?: string;
  authorAttribution?: { displayName?: string; photoUri?: string };
};
type Place = { id?: string; rating?: number; userRatingCount?: number; reviews?: PlaceReview[]; googleMapsUri?: string };

const env = (k: string): string | undefined => (import.meta.env[k] as string | undefined) || process.env[k];

// Corta en un límite de palabra, como los textos fijos ("…").
function clip(raw: string, max: number): string {
  const text = raw.replace(/\s+/g, ' ').trim();
  if (text.length <= max) return text;
  const cut = text.slice(0, max);
  const space = cut.lastIndexOf(' ');
  return `${cut.slice(0, space > max * 0.6 ? space : max).replace(/[\s,.;:–-]+$/, '')}…`;
}

const fallback = (): ReviewsData => ({ rating: '4.5', count: 51, reviews: staticReviews, href: googleReviews });

async function fetchPlace(key: string): Promise<Place> {
  const headers = { 'X-Goog-Api-Key': key, 'X-Goog-FieldMask': '' };
  const placeId = env('GOOGLE_PLACE_ID');
  if (placeId) {
    headers['X-Goog-FieldMask'] = FIELDS.join(',');
    const res = await fetch(`https://places.googleapis.com/v1/places/${placeId}`, { headers, signal: AbortSignal.timeout(8000) });
    if (!res.ok) throw new Error(`Places ${res.status}: ${await res.text()}`);
    return (await res.json()) as Place;
  }
  headers['X-Goog-FieldMask'] = FIELDS.map((f) => `places.${f}`).join(',');
  const res = await fetch('https://places.googleapis.com/v1/places:searchText', {
    method: 'POST',
    headers: { ...headers, 'Content-Type': 'application/json' },
    body: JSON.stringify({ textQuery: SEARCH_QUERY, pageSize: 1 }),
    signal: AbortSignal.timeout(8000),
  });
  if (!res.ok) throw new Error(`Places search ${res.status}: ${await res.text()}`);
  const place = ((await res.json()) as { places?: Place[] }).places?.[0];
  if (!place) throw new Error('Places search: no result');
  console.info(`[reviews] Place ID (guardar como GOOGLE_PLACE_ID): ${place.id}`);
  return place;
}

export async function loadReviews(): Promise<ReviewsData> {
  const key = env('GOOGLE_PLACES_KEY');
  if (!key) {
    console.warn('[reviews] GOOGLE_PLACES_KEY missing, using static reviews');
    return fallback();
  }
  try {
    const place = await fetchPlace(key);
    if (!place.rating || !place.userRatingCount) throw new Error('Places: no rating');
    const live = (place.reviews ?? [])
      .filter((r) => r.rating === 5)
      .sort((a, b) => (b.publishTime ?? '').localeCompare(a.publishTime ?? ''))
      .map((r, i) => ({
        name: r.authorAttribution?.displayName?.trim() ?? '',
        // Texto original (español o inglés), no la traducción de Google.
        text: clip(r.originalText?.text ?? r.text?.text ?? '', i === 0 ? 120 : 140),
        photo: r.authorAttribution?.photoUri,
      }))
      .filter((r) => r.name && r.text);
    const names = new Set(live.map((r) => r.name));
    const reviews = [...live, ...staticReviews.filter((r) => !names.has(r.name))].slice(0, SHOWN);
    return {
      rating: place.rating.toFixed(1),
      count: place.userRatingCount,
      reviews,
      href: place.googleMapsUri ?? googleReviews,
    };
  } catch (e) {
    console.warn('[reviews] Google Places unavailable, using static reviews:', e);
    return fallback();
  }
}
