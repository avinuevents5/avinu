// Ajustes de cada venue EN VIVO desde el Hub (Hub → Venues → ficha): Kosher Yes / No, Website page y
// AVINU Approved con su nota (0.5–5; null = sin evaluar).
// GET <CRM>/api/public/venues → { venues: [{ slug, kosher: 'yes' | 'no' | null, approved?: boolean, rating?: number | null }] }.
// Kosher null (sin marcar) o un venue que el Hub no tiene = se queda lo publicado en la web.
// Si el Hub no responde (o tarda), la página sigue igual: nunca rompe nada. Una sola llamada por página.

export type HubKosher = 'yes' | 'no';
export type HubVenue = { kosher: HubKosher | null; approved: boolean; rating: number | null };

let pending: Promise<Map<string, HubVenue>> | null = null;

export function fetchHubVenues(origin: string | undefined): Promise<Map<string, HubVenue>> {
  if (pending) return pending;
  pending = (async () => {
    const out = new Map<string, HubVenue>();
    if (!origin) return out;
    try {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), 5000);
      const res = await fetch(`${origin.replace(/\/+$/, '')}/api/public/venues`, { signal: ctrl.signal });
      clearTimeout(t);
      if (!res.ok) return out;
      const body = (await res.json()) as { venues?: { slug?: unknown; kosher?: unknown; approved?: unknown; rating?: unknown }[] };
      for (const v of body.venues ?? []) {
        if (typeof v.slug !== 'string') continue;
        // Valores de antes (kitchen / catering) cuentan como Yes.
        const kosher: HubKosher | null = v.kosher === 'yes' || v.kosher === 'kitchen' || v.kosher === 'catering' ? 'yes' : v.kosher === 'no' ? 'no' : null;
        const approved = v.approved === true;
        const r = typeof v.rating === 'number' && v.rating >= 0.5 && v.rating <= 5 ? Math.round(v.rating * 2) / 2 : null;
        out.set(v.slug, { kosher, approved, rating: approved ? r : null });
      }
    } catch {
      // sin conexión con el Hub: queda lo publicado
    }
    return out;
  })();
  return pending;
}

/** Solo Kosher (lo de antes): slug → yes / no. */
export async function fetchHubKosher(origin: string | undefined): Promise<Map<string, HubKosher>> {
  const out = new Map<string, HubKosher>();
  for (const [slug, v] of await fetchHubVenues(origin)) if (v.kosher) out.set(slug, v.kosher);
  return out;
}
