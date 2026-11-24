// AVINU Approved en la web (lo marca Mark en el Hub; llega en vivo con fetchHubVenues).
//  - Tarjetas de /venues: distintivo F4.2 (una línea, carbón con borde dorado mate, arriba a la derecha de la foto).
//  - Portada de cada venue: sello redondo H2 arriba a la derecha + una línea que explica que es una evaluación
//    editorial de Avinu (no un promedio de reseñas).
// Sin aprobar no se muestra nada; sin nota (null) no se muestran estrellas. Nunca "Not rated" en público.
import { fetchHubVenues } from './venue-kosher-live';

const CSS = `
.avb{position:absolute;z-index:3;top:14px;right:14px;display:inline-flex;align-items:center;gap:10px;height:25px;padding:0 14px 0 12px;border-radius:2px;background:#1b1813;border:1px solid #a88b4c;color:#c9ad6e;font-family:var(--font-body,'Hanken Grotesk',system-ui,sans-serif);font-size:.66rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;white-space:nowrap;line-height:1;pointer-events:none}
.avb svg{width:13px;height:13px;display:block;flex:none}
.avb .avb-sep{width:1px;height:11px;background:rgba(168,139,76,.45)}
.avb .avb-sc{display:inline-flex;align-items:center;gap:3px;font-size:.66rem;font-weight:500;letter-spacing:.02em;color:rgba(243,238,229,.62)}
.avb .avb-star{color:#a88b4c}
.avs{position:absolute;z-index:4;top:calc(var(--nav-h,76px) + 2.4rem);right:var(--gutter,2rem);width:132px;height:132px;border-radius:50%;background:#fffdf9;color:#17140f;box-shadow:0 6px 22px rgba(0,0,0,.22);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;text-align:center;font-family:var(--font-body,'Hanken Grotesk',system-ui,sans-serif);cursor:help}
.avs::before{content:"";position:absolute;inset:6px;border-radius:50%;border:1px solid rgba(140,108,36,.4);pointer-events:none}
.avs img{height:22px;width:auto;filter:brightness(0);display:block}
.avs .avs-ap{display:flex;align-items:center;gap:.3rem;font-size:.6rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.avs .avs-ap svg{width:13px;height:13px;display:block}
.avs .avs-st{position:relative;display:inline-block;font-size:12px;letter-spacing:1px;line-height:1;color:#ddd3c0;white-space:nowrap}
.avs .avs-st i{position:absolute;left:0;top:0;overflow:hidden;color:#b39554;font-style:normal}
.avs .avs-n{font-size:.7rem;font-weight:600;color:#4a453d;margin-top:-3px}
.avx{display:flex;align-items:center;gap:12px;max-width:1180px;margin:0 auto;padding:14px var(--gutter,2rem);font-family:var(--font-body,'Hanken Grotesk',system-ui,sans-serif);font-size:.8rem;line-height:1.5;color:#4a453d;background:#f3eee5;border-bottom:1px solid rgba(23,20,15,.1)}
.avx-wrap{background:#f3eee5}
.avx img{height:16px;width:auto;filter:brightness(0);flex:none}
@media (max-width:900px){.avs{width:104px;height:104px;gap:4px;top:calc(var(--nav-h,64px) + 4.6rem);right:1rem}.avs img{height:17px}.avs .avs-ap{font-size:.52rem}.avs .avs-st{font-size:10px}.avs .avs-n{font-size:.62rem}.avx{font-size:.76rem;align-items:flex-start}}
`;

const ck = (color: string) =>
  `<svg viewBox="0 0 14 14" aria-hidden="true"><circle cx="7" cy="7" r="6.3" fill="none" stroke="${color}" stroke-width="1.2"/><path d="M4.2 7.2 6.2 9.1 9.9 5" fill="none" stroke="${color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const fmt = (r: number) => r.toFixed(1);
const NOTE = 'AVINU Approved is our editorial assessment of venues where we have produced events: service, event experience, facilities, production suitability and reliability. It is not a customer review average.';

function styles() {
  if (document.getElementById('avinu-approved-css')) return;
  const s = document.createElement('style');
  s.id = 'avinu-approved-css';
  s.textContent = CSS;
  document.head.appendChild(s);
}

/** Distintivo de la tarjeta (F4.2). */
export function cardBadge(rating: number | null): HTMLElement {
  styles();
  const el = document.createElement('span');
  el.className = 'avb';
  el.setAttribute('aria-label', rating ? `AVINU Approved, rated ${fmt(rating)} out of 5` : 'AVINU Approved');
  el.innerHTML = `${ck('#b39554')}<span>AVINU Approved</span>` +
    (rating ? `<span class="avb-sep"></span><span class="avb-sc"><span class="avb-star">★</span>${fmt(rating)}</span>` : '');
  return el;
}

/** Sello redondo de la portada (H2) + línea de explicación después de la portada. */
export function mountHeroStamp(hero: HTMLElement | null, slug: string | undefined, origin: string | undefined) {
  if (!hero || !slug) return;
  fetchHubVenues(origin).then((hub) => {
    const v = hub.get(slug);
    if (!v || !v.approved) return;
    styles();
    if (getComputedStyle(hero).position === 'static') hero.style.position = 'relative';
    const stamp = document.createElement('div');
    stamp.className = 'avs';
    stamp.title = NOTE;
    stamp.setAttribute('role', 'img');
    stamp.setAttribute('aria-label', v.rating ? `AVINU Approved, rated ${fmt(v.rating)} out of 5. ${NOTE}` : `AVINU Approved. ${NOTE}`);
    stamp.innerHTML = `<img src="/img/avinu-white.png" alt="" width="84" height="38"><span class="avs-ap">${ck('#b39554')}Approved</span>` +
      (v.rating ? `<span class="avs-st">★★★★★<i style="width:${(v.rating / 5) * 100}%">★★★★★</i></span><span class="avs-n">${fmt(v.rating)}</span>` : '');
    hero.appendChild(stamp);
    const wrap = document.createElement('div');
    wrap.className = 'avx-wrap';
    wrap.innerHTML = `<p class="avx"><img src="/img/avinu-white.png" alt="" width="84" height="38"><span><b>AVINU Approved</b> ${NOTE.replace(/^AVINU Approved /, '')}</span></p>`;
    hero.insertAdjacentElement('afterend', wrap);
  });
}
