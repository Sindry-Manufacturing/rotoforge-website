import math
from engine import *

def circ_pts(cx, cy, r, a0, a1, n=24):
    """points on a circle from angle a0 to a1 (degrees, image convention: clockwise from +x)"""
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def qbez(p0, p1, p2, n=16):
    return [((1 - u) ** 2 * p0[0] + 2 * u * (1 - u) * p1[0] + u * u * p2[0], (1 - u) ** 2 * p0[1] + 2 * u * (1 - u) * p1[1] + u * u * p2[1]) for u in [i / n for i in range(n + 1)]]

def curve_arrow(c, pts, color, width=1.4):
    c.polyline(pts, color, width)
    c.arrow(pts[-2], pts[-1], color, width, 7)

def rot_rect(cx, cy, L, Wd, ang_deg):
    a = math.radians(ang_deg); ux, uy = math.cos(a), math.sin(a); vx, vy = -uy, ux
    return [(cx + ux * L + vx * Wd, cy + uy * L + vy * Wd), (cx + ux * L - vx * Wd, cy + uy * L - vy * Wd),
            (cx - ux * L - vx * Wd, cy - uy * L - vy * Wd), (cx - ux * L + vx * Wd, cy - uy * L + vy * Wd)]

def wire30(c, end, half=7, length=250, fill=LAYER, outline=SEP):
    """wire descending at 30 deg, ending (centreline) at `end`"""
    ux, uy = math.cos(math.radians(30)), math.sin(math.radians(30))
    vx, vy = -uy, ux
    x1, y1 = end; x0, y0 = x1 - ux * length, y1 - uy * length
    c.poly([(x0 - vx * half, y0 - vy * half), (x1 - vx * half, y1 - vy * half), (x1 + vx * half, y1 + vy * half), (x0 + vx * half, y0 + vy * half)], fill=fill, outline=outline)
    return (x0, y0)

def pool(c, cx, cy, rx, ry):
    c.ellipse(cx - rx - 16, cy + 2, cx + rx + 16, cy + ry + 22, fill=WARM)          # heat-affected zone
    c.ellipse(cx - rx, cy - ry, cx + rx, cy + ry, fill=MOLTEN, outline=AMBER, width=0.8)
    c.ellipse(cx - rx * 0.5, cy - ry * 0.5, cx + rx * 0.5, cy + ry * 0.4, fill='#FFF1C2')

class Scene:
    title = ''; subtitle = ''; legend = [(HOT, 'hot'), (COOL, 'cooling'), (COLD, 'cold')]
    layers = 3; lh = 12; layer_col = LAYER
    def draw(self, c, t):
        draw_workpiece(c, t, self.layers, self.lh, self.layer_col)
        self.body(c, t)
        draw_header(c, self.title, self.subtitle, self.legend)
    def body(self, c, t): pass

# 1 ---------------------------------------------------------------- AFRB
class AFRB(Scene):
    title = 'Additive friction roll bonding (AFRB)'
    subtitle = 'A spinning carbide wheel drags preheated wire under its rim and rolls it onto the layer below'
    CX, CY, R = 300, 162, 90
    def __init__(self):
        self.flow = Flow([((47.1, 128), (268, 255.5), 60), ((268, 255.5), (300, 258), 50), ((300, 258), (595, 258), V)])
    def body(self, c, t):
        draw_bead(c, 300, STD_RAMP)
        wire30(c, (268, 255.5))
        c.poly(rot_rect(169.2, 198.5, 26, 13, 30), fill=SHOE, outline='#993C1D')
        c.arc((264, 261), 30, 180, 210, SEP, 1.0); c.text((222, 257), '30°', 11, MUTED, anchor='rs')
        zone = [(255, 239.9)] + circ_pts(self.CX, self.CY, self.R, 120, 90, 12) + [(332, 252), (332, 264), (264, 264)]
        c.poly(zone, fill=HOT)
        c.circle((self.CX, self.CY), self.R, fill=TOOL, outline=TOOLE, width=1)
        a0 = -360 * t
        for i in range(6):
            a = math.radians(a0 + 60 * i)
            c.line((self.CX + 18 * math.cos(a), self.CY + 18 * math.sin(a)), (self.CX + 76 * math.cos(a), self.CY + 76 * math.sin(a)), SEP, 2)
        c.circle((self.CX, self.CY), 14, fill=SEP); c.circle((self.CX, self.CY), 3, fill=TEXT)
        curve_arrow(c, qbez((262, 219), (300, 237), (338, 219)), DARK)
        heat_down(c, [292, 300, 308]); c.arrow((278, 247), (272, 231), HOT, 1.0, 5); c.arrow((322, 247), (328, 231), HOT, 1.0, 5)
        c.arrow((300, 54), (300, 70), TEXT, 1.4); c.text((308, 64), 'Fz', 12, TEXT, bold=True)
        c.arrow((338, 258), (378, 258), TEXT, 1.4); c.text((384, 249), 'Ft', 12, TEXT, bold=True)
        self.flow.draw(c, t)
        label(c, (40, 86), 'wire Ø0.5 mm, fed in at 30°', (90, 141))
        label(c, (40, 236), 'hotshoe preheat'); c.dashed((146, 232), (161, 209), LEADER)
        label(c, (412, 121), 'rim runs against travel'); c.dashed((342, 217), (404, 128), LEADER)
        label(c, (412, 153), 'shear zone: friction heat, no melt'); c.dashed((334, 258), (404, 160), LEADER)
        label(c, (412, 215), 'bead cools, bonded to layer below'); c.dashed((470, 251), (470, 226), LEADER)

# 2 ---------------------------------------------------------------- AFSD
class AFSD(Scene):
    title = 'Additive friction stir deposition (AFSD)'
    subtitle = 'A rotating shoulder stirs the fed rod or wire into a wide layer; forces and torques are high'
    def __init__(self):
        self.flow = Flow([((300, 78), (300, 244), 45), ((300, 244), (338, 258), 30), ((338, 258), (595, 258), V)])
    def body(self, c, t):
        draw_bead(c, 338, STD_RAMP)
        c.rect(262, 248, 338, 270, fill=HOT)                       # stir zone (dips into the layer below)
        c.rect(272, 96, 328, 240, fill=TOOL, outline=TOOLE, width=1)
        rot_stripes(c, 300, 26, 100, 236, t)
        c.rect(294, 96, 306, 240, fill='#EDEBE5', outline=SEP)       # bore
        c.rect(296, 76, 304, 240, fill=LAYER)                        # feedstock rod
        c.rect(262, 240, 338, 252, fill=TOOL, outline=TOOLE, width=1)  # shoulder
        c.polyline([(300 + 36 * math.cos(math.radians(a)), 96 + 7 * math.sin(math.radians(a))) for a in range(200, 330, 10)], DARK, 1.4)
        c.arrow((300 + 36 * math.cos(math.radians(325)), 96 + 7 * math.sin(math.radians(325))), (300 + 36 * math.cos(math.radians(340)), 96 + 7 * math.sin(math.radians(340))), DARK, 1.4, 6)
        c.arrow((300, 54), (300, 72), TEXT, 1.8, 8); c.text((308, 64), 'F', 12, TEXT, bold=True)
        heat_down(c, [280, 300, 320], SURF + 7, 18)
        self.flow.draw(c, t)
        label(c, (340, 84), 'rod / wire fed down the bore'); c.dashed((306, 86), (336, 84), LEADER)
        label(c, (412, 153), 'shoulder spins at high torque'); c.dashed((340, 176), (404, 158), LEADER)
        label(c, (412, 232), 'stir zone: wide, plasticised, high force'); c.dashed((340, 250), (404, 237), LEADER)

# 3 ---------------------------------------------------------------- AFED
class AFED(Scene):
    title = 'Additive friction extrusion deposition (AFED)'
    subtitle = 'Friction heats feedstock inside a rotating chamber; it is extruded through a tiny die'
    def __init__(self):
        self.flow = Flow([((300, 62), (300, 225), 30), ((300, 225), (300, 250), 20), ((300, 250), (306, 260), 20), ((306, 260), (595, 260), V)])
    def body(self, c, t):
        draw_bead(c, 306, [(350, WARM), (420, COOL), (595, COLD)], h=8)
        c.rect(268, 96, 332, 226, fill=TOOL, outline=TOOLE, width=1)
        c.poly([(268, 226), (332, 226), (306, 254), (294, 254)], fill=TOOL, outline=TOOLE, width=1)
        rot_stripes(c, 300, 32, 100, 224, t, n=8)
        c.rect(284, 100, 316, 158, fill=LAYER); c.rect(284, 158, 316, 195, fill=WARM); c.rect(284, 195, 316, 226, fill=HOT)
        c.poly([(284, 226), (316, 226), (303, 252), (297, 252)], fill=HOT)
        c.polyline([(300 + 40 * math.cos(math.radians(a)), 96 + 7 * math.sin(math.radians(a))) for a in range(200, 330, 10)], DARK, 1.4)
        c.arrow((300 + 40 * math.cos(math.radians(325)), 96 + 7 * math.sin(math.radians(325))), (300 + 40 * math.cos(math.radians(340)), 96 + 7 * math.sin(math.radians(340))), DARK, 1.4, 6)
        c.rect(296, 60, 304, 100, fill=LAYER, outline=SEP)
        c.arrow((300, 50), (300, 58), TEXT, 1.4, 5)
        self.flow.draw(c, t)
        label(c, (340, 84), 'feed pressure on the wire'); c.dashed((306, 80), (336, 84), LEADER)
        label(c, (412, 153), 'spinning chamber: wall friction heats it'); c.dashed((334, 170), (404, 158), LEADER)
        label(c, (412, 232), '0.4 mm die: fast wear'); c.dashed((310, 246), (404, 237), LEADER)

# 4 ---------------------------------------------------------------- laser wire DED
class LaserDED(Scene):
    title = 'Laser directed energy deposition (wire DED)'
    subtitle = 'A laser melts a pool on the part; wire is fed into it and freezes into a bead'
    legend = [(MOLTEN, 'molten'), (HOT, 'hot'), (COOL, 'cooling'), (COLD, 'cold')]
    def __init__(self):
        self.flow = Flow([((72, 130), (278, 249), 50), ((278, 249), (322, 258), 40), ((322, 258), (595, 258), V)])
    def body(self, c, t):
        draw_bead(c, 322, [(360, HOT), (420, WARM), (470, COOL), (595, COLD)])
        pool(c, 300, 258, 22, 13)
        c.overlay(lambda l: l.poly([(288, 96), (312, 96), (300, 252)], fill='#E24B4A'), alpha=70)
        c.line((288, 96), (300, 252), '#E24B4A', 0.7); c.line((312, 96), (300, 252), '#E24B4A', 0.7)
        c.rect(280, 60, 320, 96, fill=DARK); c.rect(288, 92, 312, 98, fill=ELEC2)
        for x0, x1 in ((270, 278), (330, 322)):
            c.dashed((x0, 120), (x1, 236), ELEC2, 0.8)
        u = 0.5 + 0.5 * math.sin(2 * math.pi * 2 * t)
        wire30(c, (278, 249), half=4, length=238); c.circle((283, 251), 4 + 2 * u, fill=MOLTEN, outline=AMBER)
        heat_down(c, [288, 300, 312], SURF + 10, 14)
        self.flow.draw(c, t)
        label(c, (40, 86), 'wire fed into the pool', (100, 139))
        label(c, (412, 121), 'focused laser beam'); c.dashed((318, 150), (404, 128), LEADER)
        label(c, (412, 153), 'shield gas'); c.dashed((330, 200), (404, 160), LEADER)
        label(c, (412, 232), 'melt pool: liquid metal'); c.dashed((324, 250), (404, 237), LEADER)

# 5 ---------------------------------------------------------------- cold spray
class ColdSpray(Scene):
    title = 'Cold spray'
    subtitle = 'Supersonic gas fires solid particles that flatten and stick on impact'
    legend = [(COLD, 'solid particles'), (COOL, 'impact-warmed')]
    def __init__(self):
        self.flows = [Flow([((234, 92 + dy), (293, 116 + dy * 0.3), 40), ((293, 116 + dy * 0.3), (300 + dx, 124), 60), ((300 + dx, 124), (300 + dx * 2, 210), 160), ((300 + dx * 2, 210), (300 + dx * 3, 250), 220)], spacing=0.2, r=1.8) for dx, dy in ((0, 0), (-2, 3), (2, -3))]
    def body(self, c, t):
        draw_bead(c, 330, [(595, COLD)], h=8)
        c.poly([(270, 256), (282, 248), (300, 242), (318, 248), (330, 256), (330, 264), (270, 264)], fill=COOL)   # gaussian footprint
        for k in range(14):                                                                   # splats
            x = 340 + k * 20 + (V * t) % 20
            if x < 592: c.ellipse(x - 2.5, 257, x + 2.5, 260, fill=SEP)
        c.poly([(270, 70), (294, 120), (284, 210), (316, 210), (306, 120), (330, 70)], fill=ELEC3)
        c.polyline([(270, 70), (294, 120), (284, 210)], TOOLE, 3); c.polyline([(330, 70), (306, 120), (316, 210)], TOOLE, 3)
        c.arrow((280, 56), (280, 66), ELEC2, 1.2, 5); c.arrow((320, 56), (320, 66), ELEC2, 1.2, 5)
        c.poly([(230, 86), (272, 100), (272, 108), (230, 98)], fill=ELEC3, outline=TOOLE, width=1.2)
        for f in self.flows: f.draw(c, t, color=DARK)
        label(c, (340, 66), 'high-pressure gas (N₂ / He)'); c.dashed((322, 62), (336, 66), LEADER)
        label(c, (40, 86), 'powder feed'); c.dashed((110, 90), (232, 90), LEADER)
        label(c, (412, 153), 'de Laval nozzle: gas goes supersonic'); c.dashed((318, 165), (404, 158), LEADER)
        label(c, (412, 232), 'Gaussian footprint: awkward layers'); c.dashed((330, 250), (404, 237), LEADER)

# 6 ---------------------------------------------------------------- flame / detonation spray
class FlameSpray(Scene):
    title = 'Flame spray / detonation spray (Open Pyrojet)'
    subtitle = 'Inkjet droplets ride a flame jet, arrive hot and oxidised, and splat onto the part'
    legend = [(MOLTEN, 'molten'), (HOT, 'hot'), (COOL, 'cooling'), (COLD, 'cold')]
    def __init__(self):
        self.flows = [Flow([((300 + dx, 102), (300 + dx * 3, 250), 90)], spacing=0.3, r=2.0) for dx in (0, -3, 3)]
    def body(self, c, t):
        draw_bead(c, 330, [(370, HOT), (430, COOL), (595, COLD)], h=10)
        c.poly([(270, 258), (282, 249), (300, 244), (318, 249), (330, 258), (330, 264), (270, 264)], fill=HOT)
        for k in range(16):
            x = 336 + k * 16 + (V * t) % 16
            if x < 592: c.circle((x, 258 + (k % 3) * 2), 1.2, fill=DARK if k % 2 else 'white')
        w = 1 + 0.15 * math.sin(2 * math.pi * 3 * t)
        c.poly([(278, 100), (322, 100), (300 + 16 * w, 246), (300 - 16 * w, 246)], fill=AMBER)
        c.poly([(288, 100), (312, 100), (300 + 8 * w, 240), (300 - 8 * w, 240)], fill=MOLTEN)
        c.rect(272, 60, 328, 100, fill=DARK); c.rect(296, 96, 304, 102, fill=ELEC2)
        c.poly([(236, 70), (272, 78), (272, 86), (236, 78)], fill=ELEC3, outline=TOOLE); c.poly([(364, 70), (328, 78), (328, 86), (364, 78)], fill=ELEC3, outline=TOOLE)
        for x in (372, 396):
            pts = [(x + 4 * math.sin(2 * math.pi * (y / 40 + 0.5 * t)), y) for y in range(250, 190, -4)]
            c.polyline(pts, '#B4B2A9', 1.2)
        cf = lambda u, p: LAYER if u < 0.3 else (WARM if u < 0.55 else (HOT if u < 0.8 else MOLTEN))
        for f in self.flows: f.draw(c, t, cfn=cf)
        label(c, (40, 62), 'fuel + O₂'); c.dashed((104, 66), (234, 74), LEADER)
        label(c, (370, 62), 'thermal-inkjet metal ink'); c.dashed((306, 98), (366, 66), LEADER)
        label(c, (412, 153), 'flame heats and melts the droplets'); c.dashed((316, 170), (404, 158), LEADER)
        label(c, (412, 232), 'oxidised, porous, organic-rich splats'); c.dashed((332, 250), (404, 237), LEADER)
        label(c, (412, 190), 'fumes'); c.dashed((400, 196), (408, 194), LEADER)

# 7 ---------------------------------------------------------------- ultrasonic AM
class UAM(Scene):
    title = 'Ultrasonic additive manufacturing (UAM)'
    subtitle = 'A vibrating roller scrubs foil onto the stack: a solid-state bond near room temperature'
    legend = [(WARM, 'scrub heat (small)'), (COLD, 'cold')]
    layers = 8; lh = 4.5
    R = 38.2
    def body(self, c, t):
        draw_bead(c, 300, [(595, COLD)], h=4)
        c.rect(284, 259, 316, 265, fill=WARM)
        c.circle((120, 150), 28, fill=TOOL, outline=TOOLE, width=1); c.circle((120, 150), 20, outline=SEP); c.circle((120, 150), 12, outline=SEP); c.circle((120, 150), 4, fill=SEP)
        c.poly([(122, 178), (266, 258), (266, 262), (120, 182)], fill=LAYER, outline=SEP)
        jit = 0.8 * math.sin(2 * math.pi * 5 * t)
        cx, cy = 300 + jit, 260 - self.R
        c.circle((cx, cy), self.R, fill=TOOL, outline=TOOLE, width=1)
        a0 = -math.degrees(V * t / self.R)
        for i in range(12):
            a = math.radians(a0 + 30 * i)
            c.line((cx + (self.R - 6) * math.cos(a), cy + (self.R - 6) * math.sin(a)), (cx + self.R * math.cos(a), cy + self.R * math.sin(a)), SEP, 1.6)
        c.circle((cx, cy), 6, fill=SEP)
        c.dbl_arrow((cx - 22, cy - 50), (cx + 22, cy - 50), TEXT, 1.2, 5); c.text((cx, cy - 57), '20 kHz', 11, TEXT, anchor='ms')
        c.arrow((300, 116), (300, 138), TEXT, 1.4); c.text((308, 130), 'Fz', 12, TEXT, bold=True)
        label(c, (40, 112), 'foil tape (~0.1 mm)'); c.dashed((110, 116), (118, 122), LEADER)
        label(c, (412, 153), 'sonotrode: rolls, presses, and scrubs'); c.dashed((338, 210), (404, 158), LEADER)
        label(c, (412, 232), 'oxide scrubbed off: solid-state bond'); c.dashed((322, 259), (404, 237), LEADER)

# 8 ---------------------------------------------------------------- thermosonic AM
class Thermosonic(UAM):
    title = 'Thermosonic additive manufacturing'
    subtitle = 'Ultrasonic scrub plus heat: a warm stage and tool make bonding easier at lower force'
    legend = [(HOT, 'hot'), (COOL, 'warm'), (COLD, 'cold')]
    layers = 3; lh = 12; layer_col = COOL
    def body(self, c, t):
        draw_bead(c, 300, [(360, WARM), (595, COOL)], h=8)
        c.rect(30, 252, 292, 264, fill=LAYER, outline=SEP)
        c.rect(284, 254, 316, 266, fill=HOT)
        c.rect(XL, 331, XR, 338, fill=AMBER)
        for x in range(90, 600, 120):
            c.polyline([(x + 2.5 * math.sin(2 * math.pi * (y / 24 + 0.5 * t)), y) for y in range(298, 268, -3)], WARM, 0.8)
        jit = 0.8 * math.sin(2 * math.pi * 5 * t)
        cx, cy = 300 + jit, 256 - self.R
        c.circle((cx, cy), self.R, fill=COOL, outline=TOOLE, width=1)
        a0 = -math.degrees(V * t / self.R)
        for i in range(12):
            a = math.radians(a0 + 30 * i)
            c.line((cx + (self.R - 6) * math.cos(a), cy + (self.R - 6) * math.sin(a)), (cx + self.R * math.cos(a), cy + self.R * math.sin(a)), '#993C1D', 1.6)
        c.circle((cx, cy), 6, fill=SEP)
        c.dbl_arrow((cx - 22, cy - 50), (cx + 22, cy - 50), TEXT, 1.2, 5); c.text((cx, cy - 57), '20 kHz', 11, TEXT, anchor='ms')
        c.arrow((300, 112), (300, 134), TEXT, 1.4); c.text((308, 126), 'Fz', 12, TEXT, bold=True)
        label(c, (30, 328), 'heated stage', color='white')
        label(c, (40, 236), 'wire laid flat'); c.dashed((124, 240), (150, 251), LEADER)
        label(c, (412, 153), 'heated sonotrode vibrates and presses'); c.dashed((338, 206), (404, 158), LEADER)
        label(c, (412, 232), 'warm + scrubbed: bonds at lower force'); c.dashed((322, 256), (404, 237), LEADER)

# 9 ---------------------------------------------------------------- electrochemical AM
class ECAM(Scene):
    title = 'Electrochemical additive manufacturing (ECAM)'
    subtitle = 'Metal ions in a tiny electrolyte meniscus plate onto the part: no heat, but slow'
    legend = [(ELEC, 'electrolyte'), (COPPER, 'plated metal')]
    def __init__(self):
        self.flow = Flow([((300, 74), (300, 250), 30), ((300, 250), (305, 258), 20)], spacing=0.5, r=1.8, color=ELEC2)
    def body(self, c, t):
        draw_bead(c, 304, [(595, COPPER)], h=8)
        c.ellipse(286, 244, 314, 260, fill=ELEC)
        c.poly([(290, 70), (310, 70), (310, 226), (304, 248), (296, 248), (290, 226)], fill=ELEC, outline=TOOLE, width=1.2)
        c.line((300, 60), (300, 200), DARK, 1.5); c.text((306, 66), '+', 13, TEXT, bold=True)
        c.polyline([(300, 60), (200, 60), (200, 108)], DARK, 1.0)
        c.line((190, 108), (210, 108), DARK, 2.0); c.line((194, 116), (206, 116), DARK, 1.0)
        c.polyline([(200, 116), (200, 250), (22, 250), (22, 312), (30, 312)], DARK, 1.0)
        c.text((176, 100), '+', 12, TEXT, bold=True); c.text((176, 124), '−', 12, TEXT, bold=True)
        self.flow.draw(c, t)
        label(c, (340, 110), 'electrolyte-filled nozzle, anode inside'); c.dashed((312, 120), (336, 110), LEADER)
        label(c, (412, 232), 'meniscus: ions plate onto the cathode'); c.dashed((316, 252), (404, 237), LEADER)
        label(c, (40, 236), 'substrate is the cathode (−)'); c.dashed((176, 240), (200, 250), LEADER)

# 10 --------------------------------------------------------------- laser-induced electrochemical deposition
class LaserECD(Scene):
    title = 'Laser-induced electrochemical deposition'
    subtitle = 'A laser heats one spot inside a plating bath; metal deposits only where it is hot'
    legend = [(ELEC3, 'electrolyte'), (HOT, 'laser-heated spot'), (COPPER, 'plated metal')]
    def __init__(self):
        self.flows = [Flow([((300 + 80 * math.cos(math.radians(a)), 262 + 80 * math.sin(math.radians(a))), (300, 262), 30)], spacing=0.6, r=1.8, color=ELEC2) for a in range(195, 350, 22)]
    def body(self, c, t):
        draw_bead(c, 300, [(595, COPPER)], h=6)
        c.overlay(lambda l: l.rect(XL, 150, XR, SURF, fill=ELEC), alpha=120)
        c.polyline([(x, 150 + 1.5 * math.sin(2 * math.pi * (x / 60 + 0.5 * t))) for x in range(XL, XR + 1, 4)], ELEC2, 1.0)
        c.ellipse(286, 256, 314, 270, fill=HOT)
        c.overlay(lambda l: l.poly([(292, 92), (308, 92), (300, 262)], fill='#E24B4A'), alpha=70)
        c.line((292, 92), (300, 262), '#E24B4A', 0.7); c.line((308, 92), (300, 262), '#E24B4A', 0.7)
        c.rect(284, 60, 316, 92, fill=DARK); c.rect(292, 88, 308, 94, fill=ELEC2)
        for f in self.flows: f.draw(c, t)
        label(c, (40, 142), 'electrolyte bath'); c.dashed((132, 146), (150, 152), LEADER)
        label(c, (412, 121), 'laser beam through the bath'); c.dashed((312, 160), (404, 128), LEADER)
        label(c, (412, 232), 'hot spot: plating rate jumps here'); c.dashed((316, 258), (404, 237), LEADER)
        label(c, (412, 180), 'ions drawn to the spot'); c.dashed((372, 214), (404, 186), LEADER)
