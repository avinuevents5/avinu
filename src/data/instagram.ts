// Últimas 6 publicaciones de @avinuevents (feed JSON de Behold, plan gratis).
// Se piden UNA vez, al construir la web: cada petición cuenta como "vista" en Behold
// (1,200/mes en el plan gratis), así que nunca se piden desde el navegador.
// Si Behold falla, se usan las fotos fijas de antes.
import { iggrid, instagram } from './home';

const FEED_URL = 'https://feeds.behold.so/9mFyvWYwGuvNCT6QPGIP';

export type IgPost = { src: string; href: string; caption: string; date: string; video: boolean };
export type IgFeed = { posts: IgPost[]; followers: string | null };

type BeholdPost = {
  permalink?: string;
  prunedCaption?: string;
  caption?: string;
  timestamp?: string;
  mediaType?: string;
  mediaUrl?: string;
  thumbnailUrl?: string;
  sizes?: { medium?: { mediaUrl?: string } };
};

// Primera línea del texto, legible en la tipografía de la web: sin hashtags, @menciones,
// enlaces, teléfonos ni emojis; las letras "decorativas" (𝙏𝙝𝙚) pasan a normales.
function cleanCaption(raw: string): string {
  const line = raw.normalize('NFKC').split('\n')[0] ?? '';
  const text = line
    .replace(/[#@][\w.]+/g, '')
    .replace(/\b[\w-]+\.(com|net|org)\b\S*/gi, '')
    .replace(/\+?\d[\d .()-]{7,}\d/g, '')
    .replace(/[\p{Extended_Pictographic}\u{FE0F}\u{200D}]/gu, '')
    .replace(/\s+/g, ' ')
    .replace(/\s+([!?.,])/g, '$1')
    .trim()
    .replace(/[\s,:;–-]+$/, '');
  if (text.length <= 34) return text;
  const cut = text.slice(0, 34);
  return `${cut.slice(0, cut.lastIndexOf(' ') > 16 ? cut.lastIndexOf(' ') : 34)}…`;
}

const shortDate = (iso?: string) =>
  iso ? new Date(iso).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'America/New_York' }) : '';

const compact = (n: number) =>
  n >= 1000 ? `${(n / 1000).toFixed(n >= 10000 ? 0 : 1).replace(/\.0$/, '')}K` : String(n);

const fallback = (): IgFeed => ({
  posts: iggrid.map((src) => ({ src, href: instagram, caption: '', date: '', video: false })),
  followers: null,
});

export async function loadInstagram(): Promise<IgFeed> {
  try {
    const res = await fetch(FEED_URL, { signal: AbortSignal.timeout(8000) });
    if (!res.ok) throw new Error(`Behold ${res.status}`);
    const json = (await res.json()) as { posts?: BeholdPost[]; followersCount?: number };
    const posts = (json.posts ?? [])
      .map((p) => ({
        // medium = imagen (también para reels) servida por Behold; no caduca como las URLs de Instagram.
        src: p.sizes?.medium?.mediaUrl ?? p.thumbnailUrl ?? p.mediaUrl ?? '',
        href: p.permalink ?? instagram,
        caption: cleanCaption(p.prunedCaption ?? p.caption ?? ''),
        date: shortDate(p.timestamp),
        video: p.mediaType === 'VIDEO',
      }))
      .filter((p) => p.src)
      .slice(0, 6);
    if (!posts.length) return fallback();
    return { posts, followers: json.followersCount ? compact(json.followersCount) : null };
  } catch (e) {
    console.warn('[instagram] Behold feed unavailable, using static photos:', e);
    return fallback();
  }
}
