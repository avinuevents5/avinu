// Últimas 6 publicaciones de @avinuevents (feed JSON de Behold, plan gratis).
// Se piden UNA vez, al construir la web: cada petición cuenta como "vista" en Behold
// (1,200/mes en el plan gratis), así que nunca se piden desde el navegador.
// Si Behold falla, se usan las fotos fijas de antes.
import { iggrid, instagram } from './home';

const FEED_URL = 'https://feeds.behold.so/9mFyvWYwGuvNCT6QPGIP';

export type IgPost = { src: string; href: string; alt: string };

type BeholdPost = {
  permalink?: string;
  prunedCaption?: string;
  mediaUrl?: string;
  thumbnailUrl?: string;
  sizes?: { medium?: { mediaUrl?: string } };
};

const fallback = (): IgPost[] => iggrid.map((src) => ({ src, href: instagram, alt: 'Avinu Events on Instagram' }));

export async function loadInstagram(): Promise<IgPost[]> {
  try {
    const res = await fetch(FEED_URL, { signal: AbortSignal.timeout(8000) });
    if (!res.ok) throw new Error(`Behold ${res.status}`);
    const json = (await res.json()) as { posts?: BeholdPost[] };
    const posts = (json.posts ?? [])
      .map((p) => ({
        // medium = imagen (también para reels) servida por Behold; no caduca como las URLs de Instagram.
        src: p.sizes?.medium?.mediaUrl ?? p.thumbnailUrl ?? p.mediaUrl ?? '',
        href: p.permalink ?? instagram,
        alt: (p.prunedCaption ?? '').slice(0, 120) || 'Avinu Events on Instagram',
      }))
      .filter((p) => p.src)
      .slice(0, 6);
    return posts.length ? posts : fallback();
  } catch (e) {
    console.warn('[instagram] Behold feed unavailable, using static photos:', e);
    return fallback();
  }
}
