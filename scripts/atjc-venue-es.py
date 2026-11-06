"""Genera la versión en español de la página del venue ATJC a partir de la versión en inglés.

    python scripts/atjc-venue-es.py

Entrada:  src/pages/venues/aventura-turnberry-jewish-center/index.astro      (EN, la que se edita)
Salida:   src/pages/es/venues/aventura-turnberry-jewish-center/index.astro   (ES, NO editar a mano)

Si se cambia un texto en la versión en inglés, el script avisa cuál traducción ya no encuentra:
actualizar aquí el par (inglés → español) y volver a correrlo.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'pages', 'venues', 'aventura-turnberry-jewish-center', 'index.astro')
OUT = os.path.join(ROOT, 'src', 'pages', 'es', 'venues', 'aventura-turnberry-jewish-center', 'index.astro')
EN_URL = 'https://www.avinuevents.com/venues/aventura-turnberry-jewish-center/'
ES_URL = 'https://www.avinuevents.com/es/venues/aventura-turnberry-jewish-center/'

s = open(SRC, encoding='utf-8').read()
missing = []

def t(en, es):
    """Reemplaza todas las apariciones; avisa si el texto en inglés ya no está."""
    global s
    if en not in s:
        missing.append(en[:90]); return
    s = s.replace(en, es)

# ───────── Encabezado y SEO ─────────
s = re.sub(r'^---.*?---\n', "---\n// GENERADA por scripts/atjc-venue-es.py desde la versión en inglés. No editar a mano.\n"
           "import MoreVenues from '../../../../components/MoreVenues.astro';\n---\n", s, count=1, flags=re.S)

# ───────── Volver al listado y "Más venues" ─────────
t('<li class="nav-out"><a href="/venues/">All venues</a></li>', '<li class="nav-out"><a href="/venues/">Todos los venues</a></li>')
t('<a class="hero-back" href="/venues/">All venues</a>', '<a class="hero-back" href="/venues/">Todos los venues</a>')
t('<MoreVenues current="aventura-turnberry-jewish-center" foot={false} />', '<MoreVenues current="aventura-turnberry-jewish-center" foot={false} lang="es" />')
t("'More filters to the left', -1)", "'Más filtros a la izquierda', -1)")
t("'More filters', 1)", "'Más filtros', 1)")
t('<html lang="en">', '<html lang="es">')
t('<title>Aventura Turnberry Jewish Center · Celebrations in Aventura</title>',
  '<title>Aventura Turnberry Jewish Center · Celebraciones en Aventura</title>')
t('content="Weddings, bar & bat mitzvahs and galas at Aventura Turnberry Jewish Center: a ballroom for up to 650 guests with in-house kosher cuisine by Premier Event Catering. Production by Avinu Events."',
  'content="Bodas, bar y bat mitzvahs y galas en Aventura Turnberry Jewish Center: un salón para hasta 650 invitados con cocina kosher propia de Premier Event Catering. Producción de Avinu Events."')
t('<link rel="canonical" href="' + EN_URL + '" />', '<link rel="canonical" href="' + ES_URL + '" />')

# ───────── Selector de idioma ─────────
t('<div class="lang" role="group" aria-label="Language"><a href="/venues/aventura-turnberry-jewish-center/" aria-current="page" lang="en" hreflang="en">EN</a>',
  '<div class="lang" role="group" aria-label="Idioma"><a href="/venues/aventura-turnberry-jewish-center/" lang="en" hreflang="en" title="View in English">EN</a>')
t('<a href="/es/venues/aventura-turnberry-jewish-center/" lang="es" hreflang="es" title="Ver en español">ES</a>',
  '<a href="/es/venues/aventura-turnberry-jewish-center/" aria-current="page" lang="es" hreflang="es">ES</a>')

# ───────── Barra y menú ─────────
t('>Skip to content<', '>Saltar al contenido<')
t('aria-label="Aventura Turnberry Jewish Center, back to top"', 'aria-label="Aventura Turnberry Jewish Center, volver arriba"')
t('<nav aria-label="Sections">', '<nav aria-label="Secciones">')
t('>The Ballroom<', '>El salón<')
t('>Celebrations<', '>Celebraciones<')
t('>Gallery<', '>Galería<')
t('>Cuisine</a>', '>Cocina</a>')
t('>Production</a>', '>Producción</a>')
t('<a href="#plan">Plan</a>', '<a href="#plan">Reserva</a>')
t('Check your date', 'Consulta tu fecha')
t('Open menu', 'Abrir menú')
t('Close menu', 'Cerrar menú')

# ───────── Hero ─────────
t('A couple beneath a floral chuppah in the ATJC ballroom', 'Una pareja bajo una jupá floral en el salón de ATJC')
t('Aventura, Florida · Celebrations since 1990', 'Aventura, Florida · Celebraciones desde 1990')
t('A ballroom for up to 650 guests, kosher cuisine prepared in-house by Premier Event Catering, and a team that has hosted South Florida’s simchas for more than three decades.',
  'Un salón para hasta 650 invitados, cocina kosher preparada en casa por Premier Event Catering y un equipo que lleva más de tres décadas recibiendo las simjás del sur de Florida.')
t('Plan your celebration', 'Planea tu celebración')
t('Explore the ballroom', 'Conoce el salón')
t('<span>Guests</span>', '<span>Invitados</span>')
t('<span>In-house</span>', '<span>Propia</span>')
t('<span>Since</span>', '<span>Desde</span>')
t('Photo: Domino Arts Photography', 'Foto: Domino Arts Photography')
t('Pause background video', 'Pausar video de fondo')
t('Play background video', 'Reproducir video de fondo')

# ───────── El salón ─────────
t('One room, <em>every kind</em> of celebration', 'Un salón, <em>todo tipo</em> de celebraciones')
t('In the heart of Aventura, ATJC brings the synagogue, the ballroom and the kitchen together on one campus. Weddings, bar and bat mitzvahs, brit milah, Shabbat brunches and community galas all happen here.',
  'En el corazón de Aventura, ATJC reúne la sinagoga, el salón y la cocina en un mismo lugar. Aquí se celebran bodas, bar y bat mitzvahs, brit milá, brunches de Shabat y galas de la comunidad.')
t('Décor, lighting and catering are coordinated in-house, so families plan with one team instead of five.',
  'La decoración, la iluminación y el catering se coordinan en casa: las familias planean con un solo equipo en vez de cinco.')
t('The ATJC ballroom set for a reception, with an illuminated LED dance floor', 'El salón de ATJC montado para una recepción, con pista de baile LED iluminada')
t('The ballroom, set for a reception', 'El salón, montado para una recepción')
t('A tablescape with pink roses, crystal glassware and floral china', 'Una mesa con rosas rosadas, cristalería y vajilla floral')
t('Guests in the ballroom', 'Invitados en el salón')
t('Off-site catering', 'Catering externo')
t('Years of simchas', 'Años de simjás')

# ───────── Celebraciones ─────────
t('Made for <em>milestones</em>', 'Hecho para <em>los grandes momentos</em>')
t('aria-label="Type of celebration"', 'aria-label="Tipo de celebración"')
t("label: 'Weddings', short: 'Weddings'", "label: 'Bodas', short: 'Bodas'")
t("title: 'Weddings',", "title: 'Bodas',")
t('Wedding beneath a floral chuppah', 'Boda bajo una jupá floral')
t('Ceremony, cocktail hour and reception without moving your guests: the chuppah, the dinner and the dancing all happen under one roof.',
  'Ceremonia, cóctel y recepción sin mover a tus invitados: la jupá, la cena y el baile, todo bajo un mismo techo.')
t("'Ballroom seating for up to 650 guests', 'Kosher menus by Premier Event Catering', 'Ceremony music, DJ and lighting by Avinu Events'",
  "'Capacidad para hasta 650 invitados en el salón', 'Menús kosher de Premier Event Catering', 'Música de ceremonia, DJ e iluminación de Avinu Events'")
t("'Bar & Bat Mitzvahs'", "'Bar y Bat Mitzvahs'")
t('B\\u2019nai Mitzvah d\\u00e9cor and desserts', 'Decoración y postres de B\\u2019nai Mitzvah')
t('A synagogue and a ballroom on the same campus, so the service and the party flow into each other.',
  'La sinagoga y el salón están en el mismo lugar, así que el servicio y la fiesta fluyen uno tras otro.')
t("'Lounge seating, themed décor and a full dance floor', 'Kosher menus for every generation at the table', 'DJ, MC, dancers and LED walls by Avinu Events'",
  "'Lounges, decoración temática y una pista de baile completa', 'Menús kosher para todas las generaciones de la mesa', 'DJ, MC, bailarines y pantallas LED de Avinu Events'")
t('Candlelit tables and an LED stage', 'Mesas con velas y escenario LED')
t("title: 'Galas & community events'", "title: 'Galas y eventos de la comunidad'")
t('Seated dinners and fundraisers for the community, with a kitchen that also caters off-site events of 2,000 guests or more.',
  'Cenas de gala y eventos benéficos para la comunidad, con una cocina que también atiende eventos externos de 2,000 invitados o más.')
t("'Seated dinners for up to 650 in the ballroom', 'Off-site kosher catering for 2,000+', 'Stage sound, projection and LED by Avinu Events'",
  "'Cenas para hasta 650 personas en el salón', 'Catering kosher externo para 2,000+', 'Sonido de escenario, proyección y LED de Avinu Events'")
t("Plan ${c.label.toLowerCase().startsWith('gala') ? 'a gala' : c.id === 'weddings' ? 'a wedding' : 'a mitzvah'} at ATJC",
  "Planea ${c.id === 'galas' ? 'tu gala' : c.id === 'weddings' ? 'tu boda' : 'tu mitzvah'} en ATJC")

# ───────── El salón, transformado ─────────
t('The room, transformed', 'El salón, transformado')
t('From chuppah <em>to dance floor</em>', 'De la jupá <em>a la pista de baile</em>')
t('The same ballroom moves from ceremony to reception to late-night lounge. Choose a moment to see the room change.',
  'El mismo salón pasa de la ceremonia a la recepción y al lounge de la noche. Elige un momento para ver cómo cambia.')
t('Official ballroom film coming soon', 'Muy pronto, el video oficial del salón')
t('aria-label="Moments of the evening"', 'aria-label="Momentos de la noche"')
t("title: 'Ceremony', text: 'Beneath the chuppah'", "title: 'Ceremonia', text: 'Bajo la jupá'")
t("title: 'Reception', text: 'Dinner and the dance floor'", "title: 'Recepción', text: 'La cena y la pista de baile'")
t("title: 'Late night', text: 'Lounge and conversation'", "title: 'La noche', text: 'Lounge y sobremesa'")

# ───────── Galería ─────────
t('Inside <em>ATJC</em>', 'Dentro de <em>ATJC</em>')
t('aria-label="Filter gallery"', 'aria-label="Filtrar galería"')
t("[ ['all', 'All'], ['ballroom', 'Ballroom'], ['ceremony', 'Ceremony'], ['decor', 'Décor'], ['cuisine', 'Cuisine'] ]",
  "[ ['all', 'Todo'], ['ballroom', 'Salón'], ['ceremony', 'Ceremonia'], ['decor', 'Decoración'], ['cuisine', 'Cocina'] ]")
t('`Open photo: ${p.cap}`', '`Abrir foto: ${p.cap}`')
t('<small>Photo: ${p.credit}</small>', '<small>Foto: ${p.credit}</small>')
t('aria-label="Photo viewer"', 'aria-label="Visor de fotos"')
t('aria-label="Close"', 'aria-label="Cerrar"')
t('aria-label="Previous photo"', 'aria-label="Foto anterior"')
t('aria-label="Next photo"', 'aria-label="Foto siguiente"')

# ───────── Fotos y videos (textos alternativos y pies) ─────────
for en, es in [
    ("alt: 'Lounge seating under floral columns and violet lighting', cap: 'Lounge seating in the ballroom'",
     "alt: 'Lounge bajo columnas florales y luz violeta', cap: 'Zona lounge en el salón'"),
    ("cap: 'Tablescape with roses and crystal'", "cap: 'Mesa con rosas y cristal'"),
    ("alt: 'Mirrored round tables with sculptural centerpieces under violet lighting', cap: 'Mirrored tables and centerpieces'",
     "alt: 'Mesas redondas de espejo con centros de mesa escultóricos bajo luz violeta', cap: 'Mesas de espejo y centros de mesa'"),
    ("alt: 'Dry-aged ribeye steaks on a wooden board', cap: 'Dry-aged ribeye'",
     "alt: 'Ribeye madurado en seco sobre una tabla de madera', cap: 'Ribeye madurado en seco'"),
    ("alt: 'Faroe Island salmon in a cast-iron pan', cap: 'Faroe Island salmon'",
     "alt: 'Salmón de las Islas Feroe en sartén de hierro', cap: 'Salmón de las Islas Feroe'"),
    ("alt: 'Black grouper ceviche served in small bowls', cap: 'Black grouper ceviche'",
     "alt: 'Ceviche de mero negro servido en cuencos pequeños', cap: 'Ceviche de mero negro'"),
    ("alt: 'Bluefin tuna maki in a bamboo steamer', cap: 'Bluefin tuna maki'",
     "alt: 'Maki de atún rojo en una vaporera de bambú', cap: 'Maki de atún rojo'"),
    ("alt: 'Ora King salmon tartare with crisp skin and herb oils', cap: 'Ora King salmon tartare'",
     "alt: 'Tartar de salmón Ora King con piel crocante y aceites de hierbas', cap: 'Tartar de salmón Ora King'"),
    ("alt: 'Seared tuna tataki', cap: 'Tuna tataki'", "alt: 'Tataki de atún sellado', cap: 'Tataki de atún'"),
    ("alt: 'Roasted butternut squash with heirloom tomatoes', cap: 'Roasted butternut squash, heirloom tomatoes'",
     "alt: 'Calabaza asada con tomates heirloom', cap: 'Calabaza asada y tomates heirloom'"),
    ("label: 'A reception with floral hoops, long tables and rose lighting'",
     "label: 'Una recepción con aros florales, mesas largas y luz rosada'"),
    ("label: 'B\\u2019nai Mitzvah d\\u00e9cor: neon signs, a living wall and desserts'",
     "label: 'Decoración de B\\u2019nai Mitzvah: letreros de neón, un muro verde y postres'"),
    ("label: 'Candlelit tables in front of an LED screen'", "label: 'Mesas con velas frente a una pantalla LED'"),
    ("label: 'Kosher sushi station', cap: 'Kosher sushi bar'", "label: 'Estación de sushi kosher', cap: 'Barra de sushi kosher'"),
    ("label: 'Steak seared and served as crostini', cap: 'Steak crostini'", "label: 'Carne sellada y servida en crostini', cap: 'Crostini de carne'"),
    ("label: 'Fresh salads plated during an event', cap: 'Salads, plated live'",
     "label: 'Ensaladas frescas emplatadas durante un evento', cap: 'Ensaladas emplatadas al momento'"),
]:
    t(en, es)

# ───────── Reproductor ─────────
t("(video.muted ? 'Turn sound on' : 'Mute')", "(video.muted ? 'Activar sonido' : 'Silenciar')")
t("(playing ? 'Pause' : 'Play') + ' video: '", "(playing ? 'Pausar' : 'Reproducir') + ' video: '")

# ───────── Cocina ─────────
t('Four generations of <em>kosher</em> cuisine', 'Cuatro generaciones de cocina <em>kosher</em>')
t('Every celebration at ATJC is catered in-house by Premier Event Catering, the Pollak family’s kitchen and the venue’s caterer since 1990. Menus are built for each event: plated dinners, stations, Shabbat brunch and a kosher sushi bar.',
  'Todas las celebraciones en ATJC las atiende en casa Premier Event Catering, la cocina de la familia Pollak y el caterer del salón desde 1990. Los menús se arman para cada evento: cenas servidas a la mesa, estaciones, brunch de Shabat y una barra de sushi kosher.')
t('aria-label="The Pollak family in kosher catering"', 'aria-label="La familia Pollak en el catering kosher"')
t('Bummy’s Caterers, New York', 'Bummy’s Caterers, Nueva York')
t('Events by Premier at ATJC, Aventura', 'Events by Premier en ATJC, Aventura')
t('>From the kitchen<', '>Desde la cocina<')
t('aria-label="Previous dishes"', 'aria-label="Platos anteriores"')
t('aria-label="Next dishes"', 'aria-label="Platos siguientes"')
t('aria-label="Dishes by Premier Event Catering"', 'aria-label="Platos de Premier Event Catering"')

# ───────── Reseñas (traducidas; el original en inglés está en la versión EN) ─────────
t('Families who celebrated here', 'Familias que celebraron aquí')
t('Reviews shared publicly by Premier Event Catering', 'Reseñas publicadas por Premier Event Catering (traducidas del inglés)')
t('aria-label="Previous review"', 'aria-label="Reseña anterior"')
t('aria-label="Next review"', 'aria-label="Reseña siguiente"')
t('aria-label="Choose a review"', 'aria-label="Elige una reseña"')
t('`Review ${i + 1}: ${r.who}`', '`Reseña ${i + 1}: ${r.who}`')
a, b = s.find('const REVIEWS = ['), None
if a < 0: missing.append('const REVIEWS = [')
else:
    b = s.index('];', a) + 2
    s = s[:a] + """const REVIEWS = [
  { q: 'Es nuestro segundo evento en este salón … celebraremos la boda de nuestro tercer hijo a su debido tiempo. ¡Los invitados todavía hablan maravillas!', who: 'Boda Zighelboim · agosto de 2025' },
  { q: 'La nueva renovación transformó por completo el espacio y le dio un aire glamoroso y moderno, perfecto para cualquier ocasión.', who: 'Jenny Ivcher · diciembre de 2024' },
  { q: 'Jeremy, Steven, Zack y el resto del equipo de la sinagoga Aventura Turnberry trabajaron con el corazón y el alma para que todo saliera perfecto.', who: 'Boda Dahan · marzo de 2025' },
  { q: 'Fue más allá de lo esperado y se adaptó a los cambios de último momento … ¡El menú no solo estuvo muy bien pensado, sino que fue absolutamente delicioso!', who: 'Bar Mitzvah Farbman · agosto de 2025' },
  { q: 'Su comida es deliciosa, su servicio es excelente y el salón es precioso y está bien ubicado.', who: 'Familia Cohen · marzo de 2025' },
];""" + s[b:]

# ───────── Producción (Avinu) ─────────
t('Music, lighting &amp; production', 'Música, iluminación y producción')
t('The room sets the stage. <em>We fill it.</em>', 'El salón pone el escenario. <em>Nosotros lo llenamos.</em>')
t('Avinu Events produces the entertainment for celebrations across South Florida: the music for the ceremony, the energy of the dance floor and the light that shapes the room.',
  'Avinu Events produce el entretenimiento de celebraciones en todo el sur de Florida: la música de la ceremonia, la energía de la pista y la luz que le da forma al salón.')
t('<b>Music</b><span>DJs and MCs, ceremony singers and cantors, live musicians and bands.</span>',
  '<b>Música</b><span>DJs y MCs, cantantes y jazanim para la ceremonia, músicos y bandas en vivo.</span>')
t('<b>Lighting</b><span>Uplighting, pin-spotting and dance-floor lighting designed around the ballroom.</span>',
  '<b>Iluminación</b><span>Luces ambientales, pin spots e iluminación de pista diseñadas para el salón.</span>')
t('<b>Production</b><span>Sound, LED walls and projection for entrances, speeches and montages.</span>',
  '<b>Producción</b><span>Sonido, pantallas LED y proyección para entradas, discursos y videos.</span>')
t('Production partner', 'Socio de producción')
t('An evening celebration produced by Avinu Events, with string lights and an illuminated dance floor',
  'Una celebración de noche producida por Avinu Events, con guirnaldas de luces y pista de baile iluminada')
t('An Avinu Events DJ performing', 'Un DJ de Avinu Events en plena fiesta')
t('An Avinu Events production in South Florida', 'Una producción de Avinu Events en el sur de Florida')

# ───────── Reserva (CTA final) ─────────
t('Begin planning', 'Empieza a planear')
t('Your celebration <em>at ATJC</em>', 'Tu celebración <em>en ATJC</em>')
t('Share your date and guest count. We’ll send music, ceremony and lighting options designed for this ballroom.',
  'Cuéntanos la fecha y el número de invitados. Te enviaremos opciones de música, ceremonia e iluminación pensadas para este salón.')
t('>Get directions<', '>Cómo llegar<')
t('<dt>Address</dt>', '<dt>Dirección</dt>')
t('<dt>Venue &amp; catering</dt>', '<dt>Salón y catering</dt>')
t('<dt>Entertainment</dt>', '<dt>Entretenimiento</dt>')

# ───────── Pie y barra móvil ─────────
t('· Kosher catering by Premier Event Catering', '· Catering kosher de Premier Event Catering')
t('Page by <a', 'Página de <a')
t('Food &amp; venue photography: Premier Event Catering / Domino Arts', 'Fotos de comida y del salón: Premier Event Catering / Domino Arts')
t('aria-label="Call Avinu Events"><svg', 'aria-label="Llamar a Avinu Events"><svg')
t('href="/venues/">View more venues</a>', 'href="/venues/">Ver más venues</a>')

if missing:
    print('FALTAN traducciones (el texto en inglés cambió):'); [print('  -', m) for m in missing]; sys.exit(1)

# Control: textos visibles que sigan en inglés
leftover = [w for w in ['Check your date', 'Celebrations', 'Ballroom<', 'Guests<', 'Weddings', 'Reception', 'Ceremony\'', 'Families who', 'Begin planning', 'Previous', 'Next '] if w in s]
if leftover: print('Aviso, quedan en inglés:', leftover)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(s)
print('ok ->', os.path.relpath(OUT, ROOT))
