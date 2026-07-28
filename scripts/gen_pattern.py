# -*- coding: utf-8 -*-
"""
Gera um padrao botanico sem emenda (seamless), inspirado em papel de parede
Arts & Crafts: frondes de samambaia, rosetas e pequenas irises.
Desenho autoral, gerado por curvas parametricas.
"""
import math, random

TILE = 240

SAGE_L = "#C3D4A8"
SAGE   = "#9BB77C"
GREEN  = "#6E8E52"
CORAL  = "#E07A50"
CORAL_D= "#CB5E36"
PEACH  = "#F2B08C"
TEAL   = "#3D96B4"
TEAL_D = "#2A7B99"
GOLD   = "#DFC05A"


def bez(p0, p1, p2, p3, t):
    mt = 1 - t
    x = (mt**3)*p0[0] + 3*(mt**2)*t*p1[0] + 3*mt*(t**2)*p2[0] + (t**3)*p3[0]
    y = (mt**3)*p0[1] + 3*(mt**2)*t*p1[1] + 3*mt*(t**2)*p2[1] + (t**3)*p3[1]
    return x, y


def bez_tangent(p0, p1, p2, p3, t):
    mt = 1 - t
    x = 3*(mt**2)*(p1[0]-p0[0]) + 6*mt*t*(p2[0]-p1[0]) + 3*(t**2)*(p3[0]-p2[0])
    y = 3*(mt**2)*(p1[1]-p0[1]) + 6*mt*t*(p2[1]-p1[1]) + 3*(t**2)*(p3[1]-p2[1])
    return math.atan2(y, x)


def leaflet(bx, by, tipx, tipy, width, T):
    """Foliolo em forma de amendoa pontiaguda (base -> ponta)."""
    dx, dy = tipx - bx, tipy - by
    ln = math.hypot(dx, dy) or 1.0
    ux, uy = dx/ln, dy/ln
    px, py = -uy, ux                      # perpendicular unitaria
    mx, my = bx + dx*0.42, by + dy*0.42   # barriga mais perto da base
    a = T(bx, by)
    b = T(mx + px*width, my + py*width)
    c = T(tipx, tipy)
    d = T(mx - px*width, my - py*width)
    return (f'<path d="M{a[0]:.1f},{a[1]:.1f} Q{b[0]:.1f},{b[1]:.1f} '
            f'{c[0]:.1f},{c[1]:.1f} Q{d[0]:.1f},{d[1]:.1f} '
            f'{a[0]:.1f},{a[1]:.1f} Z"')


def frond(x, y, angle, scale, color, leaf_color, n=20, opacity=1.0):
    """Fronde de samambaia: haste curva + foliolos finos alternados."""
    out = []
    L = 92 * scale
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)

    def T(px, py):
        return (x + px*ca - py*sa, y + px*sa + py*ca)

    p0 = (0, 0)
    p1 = (L*0.30, -L*0.16)
    p2 = (L*0.66, -L*0.20)
    p3 = (L, -L*0.02)

    d0, d1, d2, d3 = T(*p0), T(*p1), T(*p2), T(*p3)
    out.append(
        f'<path d="M{d0[0]:.1f},{d0[1]:.1f} C{d1[0]:.1f},{d1[1]:.1f} '
        f'{d2[0]:.1f},{d2[1]:.1f} {d3[0]:.1f},{d3[1]:.1f}" fill="none" '
        f'stroke="{color}" stroke-width="{1.5*scale:.2f}" stroke-linecap="round" '
        f'stroke-opacity="{opacity}"/>'
    )

    for i in range(n):
        t = 0.06 + (i / (n - 1)) * 0.92
        bx, by = bez(p0, p1, p2, p3, t)
        tang = bez_tangent(p0, p1, p2, p3, t)
        # foliolos longos no meio da fronde, curtos nas pontas
        taper = math.sin(math.pi * min(max((t + 0.14) / 1.14, 0), 1)) ** 0.7
        ll = (30 * taper + 5) * scale
        for side in (-1, 1):
            # inclinacao para a ponta (fica mais fechada no fim da fronde)
            spread = math.radians((62 - 26 * t) * side)
            la = tang + spread
            tipx = bx + math.cos(la) * ll
            tipy = by + math.sin(la) * ll
            out.append(leaflet(bx, by, tipx, tipy, ll * 0.20, T)
                       + f' fill="{leaf_color}" fill-opacity="{opacity}"/>')
    return out


def rosette(x, y, scale, outer, inner, core):
    """Roseta tipo camelia: aneis de petalas concentricos."""
    out = []
    R = 17 * scale
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R:.1f}" fill="{outer}"/>')
    for ring, (rr, cnt, col) in enumerate([
        (R*0.98, 10, outer), (R*0.72, 8, inner), (R*0.46, 6, inner)
    ]):
        off = ring * 0.34
        for i in range(cnt):
            a = (i / cnt) * math.tau + off
            px = x + math.cos(a) * rr * 0.62
            py = y + math.sin(a) * rr * 0.62
            pr = rr * 0.40
            out.append(
                f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{pr:.1f}" '
                f'fill="{col}" fill-opacity="0.92"/>'
            )
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R*0.26:.1f}" fill="{core}"/>')
    for i in range(7):
        a = (i / 7) * math.tau
        out.append(
            f'<circle cx="{x + math.cos(a)*R*0.15:.1f}" '
            f'cy="{y + math.sin(a)*R*0.15:.1f}" r="{R*0.055:.1f}" fill="{GREEN}" '
            f'fill-opacity="0.55"/>'
        )
    return out


def iris(x, y, angle, scale):
    """Iris estilizada: petalas caidas + petalas erguidas + estria pontilhada."""
    out = []
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)

    def T(px, py):
        return (x + px*ca - py*sa, y + px*sa + py*ca)

    # petalas erguidas (standards): estreitas, curtas, atras
    for ang, ln in [(-108, 21), (-72, 21)]:
        r = math.radians(ang)
        tx, ty = math.cos(r)*ln*scale, math.sin(r)*ln*scale
        out.append(leaflet(0, 0, tx, ty, ln*scale*0.24, T) + f' fill="{TEAL}"/>')

    # petalas caidas (falls): largas, curvas, abrindo para os lados e para baixo
    for ang, ln in [(168, 32), (12, 30), (104, 24)]:
        r = math.radians(ang)
        tx, ty = math.cos(r)*ln*scale, math.sin(r)*ln*scale
        # curva a ponta para baixo, dando o caimento tipico da iris
        tx += 4*scale
        ty += 9*scale
        out.append(leaflet(0, 0, tx, ty, ln*scale*0.52, T) + f' fill="{TEAL_D}"/>')
        for k in range(3):
            q = 0.34 + k*0.20
            dp = T(tx*q, ty*q)
            out.append(f'<circle cx="{dp[0]:.1f}" cy="{dp[1]:.1f}" '
                       f'r="{1.5*scale:.1f}" fill="#FFFFFF" fill-opacity="0.8"/>')

    c = T(0, 0)
    out.append(f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{3.6*scale:.1f}" fill="{GOLD}"/>')
    return out


def ring_dots(x, y, r, count, color, dot_r=1.6, opacity=0.5):
    """Anel de pontinhos - textura de fundo tipo papel de parede."""
    out = []
    for i in range(count):
        ang = (i / count) * math.tau
        out.append(
            f'<circle cx="{x + math.cos(ang)*r:.1f}" cy="{y + math.sin(ang)*r:.1f}" '
            f'r="{dot_r:.1f}" fill="{color}" fill-opacity="{opacity}"/>'
        )
    return out


def sprig(x, y, angle, scale):
    """Raminho de florzinhas coral."""
    out = []
    a = math.radians(angle)
    for i in range(5):
        t = i / 4
        px = x + math.cos(a) * 30 * scale * t
        py = y + math.sin(a) * 30 * scale * t
        perp = a + math.pi/2
        for side in (-1, 1):
            fx = px + math.cos(perp) * 9 * scale * side * (1-t*0.5)
            fy = py + math.sin(perp) * 9 * scale * side * (1-t*0.5)
            out.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{3.1*scale:.1f}" fill="{CORAL}"/>')
            out.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{1.2*scale:.1f}" fill="{GOLD}"/>')
    return out


def place(bucket, fn, x, y, radius, *args, **kw):
    """Desenha o motivo e repete nas bordas opostas para costura perfeita."""
    xs = [x]
    ys = [y]
    if x - radius < 0:     xs.append(x + TILE)
    if x + radius > TILE:  xs.append(x - TILE)
    if y - radius < 0:     ys.append(y + TILE)
    if y + radius > TILE:  ys.append(y - TILE)
    for px in xs:
        for py in ys:
            bucket += fn(px, py, *args, **kw)


def frond_bbox(angle, scale):
    """Bbox real da fronde em coords locais, ja rotacionada -> (dx-, dx+, dy-, dy+)."""
    L = 92 * scale
    pad = 36 * scale                      # alcance maximo do foliolo
    corners = [(-pad, -0.22*L - pad), (L + pad, -0.22*L - pad),
               (L + pad, pad), (-pad, pad)]
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    pts = [(px*ca - py*sa, px*sa + py*ca) for px, py in corners]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), max(xs), min(ys), max(ys)


def place_frond(bucket, x, y, angle, scale, *args, **kw):
    """Como place(), mas usando o bbox real da fronde (bem menos duplicatas)."""
    dxn, dxp, dyn, dyp = frond_bbox(angle, scale)
    xs = [x]
    ys = [y]
    if x + dxn < 0:     xs.append(x + TILE)
    if x + dxp > TILE:  xs.append(x - TILE)
    if y + dyn < 0:     ys.append(y + TILE)
    if y + dyp > TILE:  ys.append(y - TILE)
    for px in xs:
        for py in ys:
            bucket += frond(px, py, angle, scale, *args, **kw)


def build(seed=11):
    rnd = random.Random(seed)
    back, mid, front = [], [], []

    # --- textura de fundo: aneis de pontinhos (tipo papel de parede) ---
    for _ in range(26):
        place(back, ring_dots, rnd.uniform(0, TILE), rnd.uniform(0, TILE), 14,
              rnd.uniform(6, 12), rnd.randint(6, 9), SAGE_L, 1.5, 0.45)
    for _ in range(70):
        px, py = rnd.uniform(0, TILE), rnd.uniform(0, TILE)
        back.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" '
                    f'r="{rnd.uniform(0.9,1.9):.1f}" fill="{SAGE_L}" fill-opacity="0.5"/>')

    # --- camada 1: frondes pallidas grandes, varrendo o tile ---
    for (px, py, ang, sc) in [
        (10, 132, -40, 1.30), (128, 12, -40, 1.30), (196, 210, -40, 1.15),
        (88, 62, 150, 1.20), (218, 178, 150, 1.20), (8, 214, 150, 1.05),
        (150, 168, -100, 1.00), (36, 40, -100, 0.92),
        (232, 76, 44, 1.05), (104, 232, 44, 1.05),
        (60, 176, -8, 0.95), (188, 108, 172, 0.95),
    ]:
        place_frond(back, px, py, ang, sc, SAGE_L, SAGE_L, n=17, opacity=1.0)

    # --- camada 2: frondes medias mais saturadas ---
    for (px, py, ang, sc) in [
        (34, 208, -64, 0.85), (166, 88, -64, 0.85), (214, 24, -64, 0.72),
        (182, 100, 116, 0.78), (54, 232, 116, 0.78), (120, 152, 116, 0.66),
        (112, 148, 6, 0.68), (240, 28, 6, 0.60),
        (16, 88, -140, 0.70), (148, 216, -140, 0.70),
        (200, 156, 88, 0.62), (72, 28, 88, 0.62),
    ]:
        place_frond(mid, px, py, ang, sc, SAGE, SAGE, n=14, opacity=0.95)

    # --- raminhos de florzinhas coral ---
    for (px, py, ang) in [(196, 34, 24), (44, 196, -150), (108, 78, 200),
                          (236, 132, -70), (10, 128, 40), (150, 244, 130)]:
        place(mid, sprig, px, py, 40, ang, 1.0)

    # --- camada 3: rosetas coral (o ponto focal) ---
    for (px, py, sc) in [(58, 58, 1.05), (178, 178, 1.05), (206, 44, 0.85),
                         (44, 200, 0.85), (128, 108, 0.72), (240, 240, 0.95)]:
        place(front, rosette, px, py, 22, sc, CORAL, PEACH, GOLD)

    # --- camada 3: irises teal ---
    for (px, py, ang) in [(148, 38, -10), (20, 150, 165), (238, 190, 95), (96, 210, -100)]:
        place(front, iris, px, py, 40, ang, 0.95)

    body = "\n".join(back + mid + front)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{TILE}" height="{TILE}" viewBox="0 0 {TILE} {TILE}">
  <title>Padrao botanico - frondes, rosetas e irises</title>
  <defs>
    <pattern id="botanico" width="{TILE}" height="{TILE}" patternUnits="userSpaceOnUse">
{body}
    </pattern>
  </defs>
  <rect width="{TILE}" height="{TILE}" fill="url(#botanico)"/>
</svg>
'''


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "padrao.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write(build())
    print("escrito:", out)
