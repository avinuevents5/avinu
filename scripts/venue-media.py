"""Prepara las fotos de una landing inmersiva de venue.

    python scripts/venue-media.py <slug> <picks.json>

picks.json = { "<nombre>": { "src": "<ruta a la foto original>", "alt": "...", "cap": "...", "cat": "<categoría de galería>" }, ... }

Genera:
  public/venues/<slug>/media/<nombre>-800.webp y -1600.webp
  src/data/venues/<slug>.photos.json   (w, h, alt, cap, cat que usa components/VenueImmersive.astro)
"""
import json, os, sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
slug, picks_path = sys.argv[1], sys.argv[2]
picks = json.load(open(picks_path, encoding='utf-8'))
base = os.path.dirname(os.path.abspath(picks_path))
out_dir = os.path.join(ROOT, 'public', 'venues', slug, 'media')
os.makedirs(out_dir, exist_ok=True)

photos, total = {}, 0
for name, p in picks.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(base, p['src']))).convert('RGB')
    w, h = im.size
    for size in (800, 1600):
        r = im.copy()
        if w > size:
            r = r.resize((size, round(h * size / w)), Image.LANCZOS)
        f = os.path.join(out_dir, f'{name}-{size}.webp')
        r.save(f, 'WEBP', quality=80 if size == 1600 else 78, method=6)
        total += os.path.getsize(f)
    photos[name] = {'w': min(w, 1600), 'h': round(h * min(w, 1600) / w), 'alt': p['alt'], 'cap': p['cap'], 'cat': p.get('cat', '')}

json.dump(photos, open(os.path.join(ROOT, 'src', 'data', 'venues', f'{slug}.photos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(slug, len(photos), 'fotos,', round(total / 1024 / 1024, 1), 'MB')
