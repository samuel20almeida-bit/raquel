# -*- coding: utf-8 -*-
"""Redimensiona e comprime o retrato para uso web, preservando o original."""
import sys, shutil
from pathlib import Path
from PIL import Image, ImageOps

src = Path(sys.argv[1])
LARGURA_ALVO = 1200          # cobre telas retina (exibe ~500px)
ALVO_KB = 400

img = Image.open(src)
img = ImageOps.exif_transpose(img)      # respeita rotação da câmera
print(f'original : {img.size[0]}x{img.size[1]}  {img.mode}  '
      f'{src.stat().st_size/1024/1024:.2f} MB')

# backup antes de qualquer escrita
bkp = src.with_name('raquel-original.jpg')
if not bkp.exists():
    shutil.copy2(src, bkp)
    print(f'backup   : {bkp.name}')

if img.mode not in ('RGB',):
    img = img.convert('RGB')

w, h = img.size
if w > LARGURA_ALVO:
    nova_h = round(h * LARGURA_ALVO / w)
    img = img.resize((LARGURA_ALVO, nova_h), Image.LANCZOS)
    print(f'redim.   : {img.size[0]}x{img.size[1]}')

# procura a maior qualidade que ainda cabe no alvo
melhor = None
for q in (88, 85, 82, 78, 74, 70):
    img.save(src, 'JPEG', quality=q, optimize=True, progressive=True)
    kb = src.stat().st_size / 1024
    melhor = (q, kb)
    print(f'  q={q:>2} -> {kb:6.1f} KB')
    if kb <= ALVO_KB:
        break

q, kb = melhor
print(f'\nfinal    : {img.size[0]}x{img.size[1]}  qualidade {q}  {kb:.1f} KB')
print(f'proporcao: {img.size[0]}/{img.size[1]} = {img.size[0]/img.size[1]:.3f}  '
      f'(o CSS espera 4/5 = 0.800)')
