"""Tiny schematic-animation engine: Pillow drawing at 2x, downsampled, then GIF via ffmpeg."""
import math, os, subprocess, shutil
from PIL import Image, ImageDraw, ImageFont

S = 2                      # supersampling factor
W, H = 640, 360            # output size (1x)
FPS, LOOP = 15, 6.0        # frames/s, loop seconds
NFRAMES = int(FPS * LOOP)
SURF = 264                 # top of previous layers (deposition surface)
BED0, BED1 = 300, 330      # bed plate
XL, XR = 30, 610           # workpiece extent
TX = 300                   # tool centre x
V = 40.0                   # workpiece scroll speed px/s (tool frame)
TICK = 40

# palette (matches the chat widget)
BED, LAYER, SEP, TOOL, TOOLE, DARK = '#5F5E5A', '#B4B2A9', '#888780', '#D3D1C7', '#5F5E5A', '#444441'
TEXT, MUTED, LEADER = '#2C2C2A', '#5F5E5A', '#888780'
MOLTEN, HOT, WARM, COOL, COLD = '#FFD166', '#D85A30', '#F0997B', '#F5C4B3', '#B4B2A9'
ELEC, ELEC2, ELEC3 = '#B5D4F4', '#378ADD', '#E6F1FB'
AMBER, AMBER2, COPPER, PLASMA = '#EF9F27', '#FAC775', '#D08A5C', '#85B7EB'
SHOE = '#F5C4B3'

FONT_DIR = '/usr/share/fonts/truetype/dejavu/'
_fonts = {}
def font(size, bold=False):
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_DIR + ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'), int(size * S))
    return _fonts[key]

def sc(p):
    return (p[0] * S, p[1] * S)

class Canvas:
    def __init__(self):
        self.im = Image.new('RGB', (W * S, H * S), 'white')
        self.d = ImageDraw.Draw(self.im)
    # --- primitives (1x coordinates) ---
    def line(self, p1, p2, color, width=1.0):
        self.d.line([sc(p1), sc(p2)], fill=color, width=max(1, int(round(width * S))))
    def polyline(self, pts, color, width=1.0):
        self.d.line([sc(p) for p in pts], fill=color, width=max(1, int(round(width * S))), joint='curve')
    def dashed(self, p1, p2, color, width=0.6, dash=4, gap=3):
        x1, y1 = p1; x2, y2 = p2
        L = math.hypot(x2 - x1, y2 - y1)
        if L == 0: return
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        s = 0.0
        while s < L:
            e = min(L, s + dash)
            self.line((x1 + ux * s, y1 + uy * s), (x1 + ux * e, y1 + uy * e), color, width)
            s += dash + gap
    def poly(self, pts, fill=None, outline=None, width=0.6):
        if fill is not None:
            self.d.polygon([sc(p) for p in pts], fill=fill)
        if outline is not None:
            self.polyline(list(pts) + [pts[0]], outline, width)
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=0.6, radius=0):
        if radius:
            self.d.rounded_rectangle([x0 * S, y0 * S, x1 * S, y1 * S], radius=radius * S, fill=fill, outline=outline, width=max(1, int(round(width * S))) if outline else 0)
        else:
            self.d.rectangle([x0 * S, y0 * S, x1 * S, y1 * S], fill=fill, outline=outline, width=max(1, int(round(width * S))) if outline else 0)
    def circle(self, c, r, fill=None, outline=None, width=0.6):
        x, y = c
        self.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=fill, outline=outline, width=max(1, int(round(width * S))) if outline else 0)
    def ellipse(self, x0, y0, x1, y1, fill=None, outline=None, width=0.6):
        self.d.ellipse([x0 * S, y0 * S, x1 * S, y1 * S], fill=fill, outline=outline, width=max(1, int(round(width * S))) if outline else 0)
    def arc(self, c, r, a0, a1, color, width=1.0):
        x, y = c
        self.d.arc([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], a0, a1, fill=color, width=max(1, int(round(width * S))))
    def arrow(self, p1, p2, color, width=1.2, head=7):
        x1, y1 = p1; x2, y2 = p2
        L = math.hypot(x2 - x1, y2 - y1)
        if L < 1: return
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        bx, by = x2 - ux * head, y2 - uy * head
        self.line(p1, (bx, by), color, width)
        w = head * 0.45
        self.poly([(x2, y2), (bx - uy * w, by + ux * w), (bx + uy * w, by - ux * w)], fill=color)
    def dbl_arrow(self, p1, p2, color, width=1.2, head=6):
        self.arrow(p1, p2, color, width, head); self.arrow(p2, p1, color, width, head)
    def text(self, p, s, size=12, color=MUTED, bold=False, anchor='ls'):
        self.d.text(sc(p), s, font=font(size, bold), fill=color, anchor=anchor)
    def text_w(self, s, size=12, bold=False):
        return self.d.textlength(s, font=font(size, bold)) / S
    def overlay(self, fn, alpha=110):
        """draw translucent shapes: fn(draw_layer_canvas) with fills given as RGB; blended at alpha."""
        layer = Image.new('RGBA', self.im.size, (0, 0, 0, 0))
        lc = Canvas.__new__(Canvas); lc.im = layer; lc.d = ImageDraw.Draw(layer)
        fn(lc)
        a = layer.split()[3].point(lambda v: alpha if v > 0 else 0)
        layer.putalpha(a)
        base = self.im.convert('RGBA')
        self.im = Image.alpha_composite(base, layer).convert('RGB')
        self.d = ImageDraw.Draw(self.im)
    def finish(self):
        return self.im.resize((W, H), Image.LANCZOS)

# ---------- shared drawing pieces ----------
def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def draw_header(c, title, subtitle, legend):
    c.text((30, 26), title, 15, TEXT, bold=True)
    c.text((30, 46), subtitle, 12, MUTED)
    # legend bottom-right
    x = 610
    for col, lab in reversed(legend):
        w = c.text_w(lab, 11)
        x -= w
        c.text((x, 351), lab, 11, MUTED)
        x -= 15
        c.rect(x, 342, x + 11, 351, fill=col)
        x -= 14
    c.text((30, 351), 'Head-fixed side view, not to scale', 11, MUTED)

def draw_workpiece(c, t, layers=3, lh=12, layer_col=LAYER, bed_col=BED, tick_top=None):
    c.rect(XL, BED0, XR, BED1, fill=bed_col)
    top = SURF
    c.rect(XL, top, XR, BED0, fill=layer_col)
    for i in range(1, layers + 1):
        y = SURF + i * lh
        if y <= BED0: c.line((XL, y), (XR, y), SEP, 0.6)
    c.line((XL, top), (XR, top), SEP, 0.6)
    # scrolling ticks (loop-safe: V*LOOP is a multiple of TICK)
    off = (V * t) % TICK
    y0 = tick_top if tick_top is not None else SURF + 2
    for k in range(-1, 16):
        x = XL + k * TICK + off
        if XL + 1 < x < XR - 1:
            c.line((x, y0), (x, BED1 - 3), '#8B8A83', 0.5)
    c.arrow((540, 315), (600, 315), '#D3D1C7', 1.4, 6)

def draw_bead(c, x0, ramp, h=12, y_top=None):
    """ramp: list of (x_end, color) from the tool backwards"""
    yt = SURF - h if y_top is None else y_top
    xs = x0
    for xe, col in ramp:
        c.rect(xs, yt, xe, SURF, fill=col)
        xs = xe
    c.line((x0, yt), (xs, yt), SEP, 0.5)

STD_RAMP = [(350, WARM), (420, COOL), (595, COLD)]

def heat_down(c, xs, y0=SURF + 1, length=20, col=HOT):
    for i, x in enumerate(xs):
        c.arrow((x, y0), (x, y0 + length + (6 if i == len(xs) // 2 else 0)), col, 1.0, 5)

def label(c, p_text, s, p_from=None, size=11, color=MUTED, anchor='ls'):
    c.text(p_text, s, size, color, anchor=anchor)
    if p_from is not None:
        # leader ends 4px short of the text baseline/start
        tx, ty = p_text
        c.dashed(p_from, (tx if anchor == 'ls' else tx, ty + 3 if p_from[1] > ty else ty - 12), LEADER, 0.6)

class Flow:
    """particles along a polyline with per-segment speeds; period snapped so the loop is seamless."""
    def __init__(self, segs, spacing=0.5, r=2.2, color=DARK):
        # segs: list of (p0, p1, speed)
        self.segs = []
        T = 0.0
        for p0, p1, v in segs:
            L = math.hypot(p1[0] - p0[0], p1[1] - p0[1]); dt = L / v
            self.segs.append([p0, p1, dt]); T += dt
        self.NP = max(2, int(round(T / spacing)))
        k = self.NP * spacing / T
        for sgm in self.segs: sgm[2] *= k
        self.T = self.NP * spacing; self.r = r; self.color = color
    def pos(self, tau):
        for p0, p1, dt in self.segs:
            if tau <= dt:
                u = tau / dt
                return (p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u)
            tau -= dt
        return self.segs[-1][1]
    def draw(self, c, t, color=None, rfn=None, cfn=None):
        for i in range(self.NP):
            tau = ((t / self.T + i / self.NP) % 1.0) * self.T
            p = self.pos(tau)
            rr = self.r if rfn is None else rfn(tau, p)
            col = cfn(tau / self.T, p) if cfn else (color or self.color)
            c.circle(p, rr, fill=col)

def rot_stripes(c, cx, x_half, y0, y1, t, n=6, rps=1.0, color='#9A9891', width=1.0, sign=1):
    """surface features of a cylinder rotating about a vertical axis, seen from the side."""
    for i in range(n):
        ph = 2 * math.pi * (i / n + sign * rps * t)
        if math.cos(ph) > 0.05:
            x = cx + x_half * math.sin(ph)
            c.line((x, y0), (x, y1), color, width * (0.5 + 0.6 * math.cos(ph)))

def render(scene, outdir, gif_path, fps=FPS):
    os.makedirs(outdir, exist_ok=True)
    for f in range(NFRAMES):
        t = f / fps
        c = Canvas()
        scene.draw(c, t)
        c.finish().save(os.path.join(outdir, 'f%03d.png' % f))
    # palette-based GIF via ffmpeg
    pal = os.path.join(outdir, 'pal.png')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(fps), '-i', os.path.join(outdir, 'f%03d.png'),
                    '-vf', 'palettegen=max_colors=96:stats_mode=diff', pal], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(fps), '-i', os.path.join(outdir, 'f%03d.png'), '-i', pal,
                    '-lavfi', 'paletteuse=dither=none:diff_mode=rectangle', '-loop', '0', gif_path], check=True)
    return os.path.getsize(gif_path)
