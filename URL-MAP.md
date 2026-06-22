# avinuevents.com — Mapa maestro de URLs (migración WordPress → Astro)

> Generado del crawl de las 105 URLs del sitemap (`page-sitemap.xml`, Rank Math).
> **71 páginas con contenido real · 34 vacías/placeholder · 0 errores.**
> El contenido fiel de cada página está en `content-inventory/<slug>.md`.
>
> **Leyenda de acción:**
> - **KEEP** = URL limpia + contenido real → mantener la misma URL, solo reconstruir la página.
> - **301** = URL rota (typo / duplicado / consolidación) → redirigir a la URL nueva limpia.
> - **KILL** = basura / vacía / nunca construida / sensible → 410 o redirect al padre. No migrar.
>
> Filosofía SEO: **no cambiar las URLs buenas** (cada cambio cuesta un redirect y riesgo). Solo se tocan las rotas. Las decisiones marcadas con ⚠️SC dependen de datos de Google Search Console (tráfico real) antes de confirmarse.

---

## 🚨 Urgente (independiente de la migración)

| URL | Problema | Acción |
|---|---|---|
| `/eventreports/` | Login Gmail + **password en texto plano** + PDF interno, indexable | **Bajar del live + rotar la pass YA.** No migrar (KILL). Es página interna de coordinadores, no pública. |

---

## Core del sitio

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/` | Home (hub visual, w55) | **KEEP** | `/` |
| `/home/` | Home duplicado (w88) — ⚠️ el body dice **"Levine Events"**, no Avinu | **301** | `/` |
| `/about/` | About (w120) | **KEEP** | `/about/` |
| `/contact/` | Form de contacto (render JS, no se capturó) | **KEEP** | `/contact/` |
| `/get-a-quote/` | Form de cotización (render JS, no se capturó) — es el CTA principal del nav | **KEEP** | `/get-a-quote/` |
| `/terms-and-conditions/` | Términos (w1050, contenido real largo) | **301** (opcional) | `/terms/` |

> ⚠️ Los dos forms (`/contact/`, `/get-a-quote/`) se renderizan con JavaScript/Elementor y **no se pudieron capturar** con el crawler. Hay que recapturar los campos del form desde el sitio live (o del export de WP) antes de reconstruirlos.

---

## DJs

El índice está bien escrito (`/best-djs-in-south-florida/`, buen keyword local) pero **todos los perfiles cuelgan del path con typo `soth-florida`**. Se arregla con 301.

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/best-djs-in-south-florida/` | Roster de DJs (w170) | **KEEP** | `/best-djs-in-south-florida/` |
| `/best-djs-in-soth-florida/djlance/` | DJ Lance (w295) | **301** | `/best-djs-in-south-florida/dj-lance/` |
| `/best-djs-in-soth-florida/djmansel/` | DJ Mansel (w230) | **301** | `…/dj-mansel/` |
| `/best-djs-in-soth-florida/djtrey/` | DJ Trey (w295) | **301** | `…/dj-trey/` |
| `/best-djs-in-soth-florida/djricky/` | DJ Ricky (w220) | **301** | `…/dj-ricky/` |
| `/best-djs-in-soth-florida/djgrant/` | DJ Grant (w335) | **301** | `…/dj-grant/` |
| `/best-djs-in-soth-florida/djlevine/` | ⚠️ titula "DJ Levine" pero el bio es de **Mark Levine** (contenido cruzado) | **301** + revisar | `…/dj-levine/` |
| `/manseldj-2/` | ⚠️ titula "MarkLevine", categoría dj (w200) — duplicado/cruce | **KILL** o 301 | a confirmar |
| `/best-djs-in-soth-florida/dj-trey-test/` | Página de **TEST** (w230) | **KILL** | — |
| `/dj-details/` | Stub fino (w35) | **KILL** | — |
| `/djs-booking/` | Vacía (placeholder) | **KILL** → 301 | `/best-djs-in-south-florida/` |

> ⚠️ El roster menciona **7 DJs** (Levine, Ricky, Mansel, Joseph, Trey, Grant, Lance) pero **DJ Joseph no tiene página de perfil**. Confirmar si falta o si ya no trabaja.

---

## Cantantes (Singers)

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/jewish-ceremony-singer/` | Roster de cantantes (w110) | **KEEP** | `/jewish-ceremony-singer/` |
| `/anais-vivas/` | Anais Vivas (w320) | **KEEP** | `/anais-vivas/` |
| `/mark-levine/` | Mark Levine (w230) | **KEEP** | `/mark-levine/` |
| `/noam-agami/` | Noam Agami (w320) | **KEEP** | `/noam-agami/` |
| `/sergio-andre/` | Sergio Andre (w340) | **KEEP** | `/sergio-andre/` |
| `/singer-booking/` | Vacía (placeholder) | **KILL** → 301 | `/jewish-ceremony-singer/` |

> ⚠️ En todos los perfiles el copy usa pronombres masculinos boilerplate ("his exceptional artistry") incluso para Anais (mujer). Limpiar al reescribir.

---

## Músicos y Bandas

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/wedding-musicians-and-band/` | Roster de músicos por instrumento (w220) | **KEEP** | `/wedding-musicians-and-band/` |
| `/bands/` | Vacía | **KILL** → 301 | `/wedding-musicians-and-band/` |

---

## Planners

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/planners/` | Hub de planners (w75) — linkea a Zais | **KEEP** | `/planners/` |
| `/zais-cortez/` | Perfil planner Zais Cortez (w130) — ⚠️ nombre como "Zaiz" en headings | **KEEP** | `/zais-cortez/` |

---

## Venues (directorio)

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/best-affordable-venues-2/` | **Índice** de venues (w95, lista 25) — sufijo `-2` | **301** | `/venues/` |
| `/the-addison/` | The Addison (w175) | **KEEP** | `/the-addison/` |
| `/aventura-turnberry-jewish-center/` | ATJC (w110) | **KEEP** | `/aventura-turnberry-jewish-center/` |
| `/hyatt-centric-las-olas/` | Hyatt Centric (w410, el más completo) | **KEEP** | igual |
| `/walton-house/` | Walton House (w240) | **KEEP** | igual |
| `/the-confidante/` | The Confidante (w160) | **KEEP** | igual |
| `/old-school-square/` | Old School Square (w155) | **KEEP** | igual |
| `/eden-regal-ballroom/` | Eden Regal (w115) | **KEEP** | igual |
| `/bonaventure-resort/` | Bonaventure (w110) | **KEEP** | igual |
| `/wherehouse-2016/` | Wherehouse (w110) | **KEEP** | igual |
| `/viceroy-miami/` `/ritz-carlton-miami-beach/` `/douglas-entrance/` `/ninja-lounge/` | venues (w90-95) | **KEEP** | igual |
| `/temple-moses/` `/marriott-pompano-beach/` `/maps-backlot/` `/sheraton-suites-plantation/` | venues (w75-90) | **KEEP** | igual |
| `/eden-roc/` `/club-vault/` `/gallery-of-amazing-things/` `/embassy-suites-deerfield-beach/` | venues (w66-78) | **KEEP** | igual |
| `/benvenuto/` | ⚠️ Benvenuto **Restaurant** (Boynton Beach, w115) | **KEEP** | `/benvenuto/` |
| `/benvenuto-2/` | ⚠️ titula "Benvenuto" pero el contenido es **Beth Torah** (North Miami Beach, w110) — slug equivocado, NO es duplicado | **301** | `/beth-torah/` |
| `/yachts/` | Yachts (w75, 15 img) — es servicio/alquiler, no venue | **KEEP** | `/yachts/` |

> ⚠️ El índice lista 25 venues; 3 no tienen página propia (Beth Torah ya cubierto por benvenuto-2, Temple Beth El Hollywood, Vizcaya Museum). Confirmar si crear esas fichas.

### Galerías de fotos de eventos (duplicados a consolidar)
| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/ventura-turnberry-jewish-center-event-pictures/` | Galería (w15, 5 img) — ⚠️ "ventura" sin la A | **301** | dentro de `/aventura-turnberry-jewish-center/` |
| `/ventura-turnberry-jewish-center-event-pictures-2/` | Casi-duplicado (w120, 3 img) | **301** | dentro de `/aventura-turnberry-jewish-center/` |

---

## Tipos de evento

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/weddings/` | Weddings (w230) | **KEEP** | `/weddings/` |
| `/corporate/` | Corporate (w95) | **KEEP** | `/corporate/` |
| `/bar-mitzvahs/` | Bar/Bat Mitzvahs (w130) | **KEEP** | `/bar-mitzvahs/` |
| `/private/` | Private Events (w78) | **301** (opcional) | `/private-events/` |

---

## Servicios de producción

| URL actual | Contenido | Acción | URL nueva |
|---|---|---|---|
| `/wedding-lighting-in-south-florida/` | **Lighting** general (w240) | **301** | `/services/lighting/` |
| `/led-pannels/` | LED walls (w120) — typo "Pannels" | **301** | `/services/led-walls/` |
| `/photography-and-videography/` | Foto/video (w130) | **301** | `/services/photo-video/` |
| `/uplights/` | Uplights (w235) | **301** | `/services/uplights/` (o sub de lighting) |
| `/miamiphotobooth/` | Photo Booth Open Air (w86) — **contenido real** | **301** | `/services/photo-booth/` |
| `/photo-booth/` | Vacía (el contenido real está en miamiphotobooth) | **KILL** → 301 | `/services/photo-booth/` |
| `/luxury-car-rentals/` | Listado autos lujo (w75, 10 img) | **301** | `/services/luxury-cars/` |
| `/luxury-car-rentals-2/` | Ficha **Lamborghini Aventador SV** (w175) — no es duplicado, es un auto | **301** | `/services/luxury-cars/lamborghini-aventador-sv/` |
| `/concierge/` | Concierge (w88) | **301** | `/services/concierge/` |
| `/services-2/` | titula "Entertainment" (w90) — **contenido real** | **301** | `/services/` |
| `/services/` | Vacía | **REBUILD** como índice limpio | `/services/` |
| `/entertainment/` | Stub (w12) | **KILL** → 301 | `/services/` |
| `/other-services/` | Stub (w8) | **KILL** → 301 | `/services/` |
| `/music/` | Stub (w9) | **KILL** → 301 | `/services/` |

---

## KILL — páginas nunca construidas (vacías, w0-12, sin SEO)

Estas son taxonomías de sub-servicios que WordPress generó pero **nunca se llenaron**. Recomendación: **410/no migrar**, y si alguna tiene tráfico (⚠️SC) → 301 a su tipo de evento padre (`/weddings/`, `/private-events/`, `/corporate/`).

**`wedding-*` (vacías):** `wedding-private-services`, `wedding-bachelor-party`, `wedding-planning`, `wedding-special-acts`, `wedding-draping`, `wedding-photographers-videographers`, `wedding-photo-booths`, `wedding-lighting`, `wedding-dancers`, `wedding-dj-mcs`

**`private-events-*` (vacías):** `private-events-special-services`, `private-events-planning`, `private-events-special-acts`, `private-events-draping`, `private-events-photographers-videographers`, `private-events-photobooths`, `private-events-musicians-and-bands`, `private-events-lighting`, `private-events-dancers`, `private-events-dj-mcs`, `private-events-dancers/show-mapping-projector`

**`corporate-events-*` (vacías):** `corporate-events-dancers`

**Servicios stub vacíos:** `confetti-special-effects`, `private-chefs`, `day-of-coordination`, `led-robots`, `pin-spot-lighting`, `intelligent-dance-floor`

**Otras basura:** `info` (vacía), `elementor-9807` (template Elementor), `models` (vacía), `gallery` (vacía — rebuild si se quiere galería)

---

## Estructura nueva propuesta (IA limpia)

```
/                                  Home
/about/                            Nosotros
/contact/                          Contacto
/get-a-quote/                      Cotización (CTA principal)
/terms/                            Términos

/best-djs-in-south-florida/        DJs (índice, keep keyword)
   /dj-lance/  /dj-mansel/  /dj-trey/  /dj-ricky/  /dj-grant/  /dj-levine/

/jewish-ceremony-singer/           Cantantes (índice)
   (perfiles en raíz: /anais-vivas/, /mark-levine/, /noam-agami/, /sergio-andre/)

/wedding-musicians-and-band/       Músicos y bandas
/planners/  +  /zais-cortez/       Planners

/venues/                           Venues (índice, ex best-affordable-venues-2)
   ~22 fichas de venue (la mayoría keep en raíz)

/weddings/  /corporate/  /bar-mitzvahs/  /private-events/    Tipos de evento

/services/                         Servicios (índice nuevo)
   /lighting/  /led-walls/  /photo-video/  /photo-booth/
   /uplights/  /luxury-cars/  /concierge/

/yachts/                           Yachts
```

---

## Decisiones que dependen de datos (antes de cerrar el mapa)

1. **⚠️SC — Google Search Console:** qué URLs de las "KEEP" y de las "KILL vacías" reciben tráfico/clics. Define si alguna vacía merece 301 en vez de 410, y si conviene mover venues a `/venues/<slug>/` o dejarlas en raíz (menos redirects = más seguro).
2. **Forms (`/contact/`, `/get-a-quote/`):** recapturar campos desde el live (render JS).
3. **DJ Joseph:** ¿falta su perfil o se discontinuó?
4. **`/home/` branding "Levine Events":** ¿error o marca anterior?
5. **`benvenuto-2` = Beth Torah:** confirmar slug nuevo `/beth-torah/`.
6. **Venues sin ficha** (Temple Beth El Hollywood, Vizcaya): ¿crear?
