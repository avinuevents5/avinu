// Ajuste Kosher de cada venue EN VIVO desde el Hub (Hub → Venues → ficha → Kosher / Website page).
// GET <CRM>/api/public/venues → { venues: [{ slug, kosher: 'kitchen' | 'catering' | 'no' | null }] }.
// null (sin confirmar) o un venue que el Hub no tiene = se queda lo publicado en la web.
// Si el Hub no responde (o tarda), la página sigue igual: nunca rompe nada.

export type HubKosher = 'kitchen' | 'catering' | 'no';

export const KOSHER_LABEL: Record<'kitchen' | 'catering', string> = {
  kitchen: 'Kosher kitchen on site',
  catering: 'Kosher catering welcome',
};

export async function fetchHubKosher(origin: string | undefined): Promise<Map<string, HubKosher>> {
  const out = new Map<string, HubKosher>();
  if (!origin) return out;
  try {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), 5000);
    const res = await fetch(`${origin.replace(/\/+$/, '')}/api/public/venues`, { signal: ctrl.signal });
    clearTimeout(t);
    if (!res.ok) return out;
    const body = (await res.json()) as { venues?: { slug?: unknown; kosher?: unknown }[] };
    for (const v of body.venues ?? []) {
      if (typeof v.slug === 'string' && (v.kosher === 'kitchen' || v.kosher === 'catering' || v.kosher === 'no')) out.set(v.slug, v.kosher);
    }
  } catch {
    // sin conexión con el Hub: queda lo publicado
  }
  return out;
}
