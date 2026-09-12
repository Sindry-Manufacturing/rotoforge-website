import math
from engine import *
from scenes_a import Scene, wire30, pool, circ_pts, curve_arrow

def flat_wire(c, x1=292, h=12, fill=LAYER):
    c.rect(XL, SURF - h, x1, SURF, fill=fill, outline=SEP)

def heater_band(c, x0, x1, y0, y1):
    c.rect(x0, y0, x1, y1, fill=AMBER, outline='#BA7517')
    for x in range(int(x0) + 3, int(x1) - 2, 6):
        c.line((x, y0 + 2), (x, y1 - 2), '#BA7517', 0.6)

# 11 --------------------------------------------------------------- heated micro power-hammer forging
class Powerhammer(Scene):
    title = 'Heated micro power-hammer forging'
    subtitle = 'A heated hammer forges the wire flat, strike by strike: a sewing machine for metal'
    def body(self, c, t):
        s = math.sin(2 * math.pi * 2 * t)
        lift = 24 * (1 - s) / 2
        strike = s > 0.9
        draw_bead(c, 312, [(360, WARM), (430, COOL), (595, COLD)], h=8)
        for k in range(8):                                                     # hammer marks on the forged bead
            x = 318 + k * 40 + (V * t) % 40
            if x < 592: c.arc((x, 258), 6, 200, 340, SEP, 0.8)
        flat_wire(c, 292)
        c.rect(288, 254, 312, 264, fill=HOT)
        c.rect(292, 252, 308, 256, fill=HOT if strike else WARM)
        y_tip = 256 - lift
        c.rect(288, 70, 312, y_tip, fill=TOOL, outline=TOOLE, width=1)
        heater_band(c, 288, 312, 130 - lift, 152 - lift)
        c.rect(290, y_tip - 12, 310, y_tip, fill=COOL, outline=TOOLE)
        c.dbl_arrow((330, 232), (330, 256), TEXT, 1.2, 5)
        if strike:
            for dx in (-1, 1):
                c.line((300 + dx * 16, 250), (300 + dx * 24, 244), '#EF9F27', 1.5); c.line((300 + dx * 14, 258), (300 + dx * 24, 262), '#EF9F27', 1.5)
            heat_down(c, [294, 300, 306], SURF + 1, 14)
        label(c, (278, 124), 'heated hammer', anchor='rs'); c.dashed((286, 140 - lift), (282, 128), LEADER)
        label(c, (40, 240), 'wire lies on the surface'); c.dashed((174, 244), (200, 251), LEADER)
        label(c, (412, 153), 'rapid heated strikes'); c.dashed((334, 240), (404, 158), LEADER)
        label(c, (412, 232), 'forged flat and bonded, blow by blow'); c.dashed((332, 256), (404, 237), LEADER)

# 12 --------------------------------------------------------------- micro arc / plasma
class MicroArc(Scene):
    title = 'Micro arc / plasma deposition'
    subtitle = 'An arc melts the wire and a pool on the part; shield gas needed, heat input is high'
    legend = [(MOLTEN, 'molten'), (HOT, 'hot'), (COOL, 'cooling'), (COLD, 'cold')]
    def __init__(self):
        self.flow = Flow([((72, 130), (278, 249), 50), ((278, 249), (322, 258), 40), ((322, 258), (595, 258), V)])
    def body(self, c, t):
        draw_bead(c, 320, [(360, HOT), (420, WARM), (470, COOL), (595, COLD)])
        pool(c, 300, 258, 20, 12)
        j = 2 * math.sin(2 * math.pi * 5 * t); j2 = 2 * math.cos(2 * math.pi * 7 * t)
        c.overlay(lambda l: l.poly([(298, 236), (302, 236), (318 + j, 252), (282 + j2, 252)], fill=PLASMA), alpha=150)
        c.poly([(299, 236), (301, 236), (304 + j2 * 0.5, 250), (296 + j * 0.5, 250)], fill='#FFFFFF')
        c.poly([(270, 100), (330, 100), (316, 200), (284, 200)], fill=TOOL, outline=TOOLE, width=1)
        c.rect(297, 80, 303, 236, fill=DARK); c.poly([(297, 232), (303, 232), (300, 240)], fill=DARK)
        c.dashed((286, 204), (290, 238), ELEC2, 0.8); c.dashed((314, 204), (310, 238), ELEC2, 0.8)
        u = 0.5 + 0.5 * math.sin(2 * math.pi * 2 * t)
        wire30(c, (278, 249), half=4, length=238); c.circle((283, 251), 4 + 2 * u, fill=MOLTEN, outline=AMBER)
        heat_down(c, [288, 300, 312], SURF + 10, 14)
        self.flow.draw(c, t)
        label(c, (40, 86), 'wire fed into the pool', (100, 139))
        label(c, (412, 100), 'tungsten electrode'); c.dashed((304, 110), (404, 106), LEADER)
        label(c, (412, 153), 'shield gas cup'); c.dashed((322, 176), (404, 160), LEADER)
        label(c, (412, 232), 'arc plasma melts wire and substrate'); c.dashed((322, 250), (404, 237), LEADER)

# 13 --------------------------------------------------------------- joule printing
class Joule(Scene):
    title = 'Joule printing'
    subtitle = 'Current through the wire–substrate contact heats it (I²R) while the head presses the wire down'
    def __init__(self):
        self.cur = Flow([((450, 110), (340, 110), 120), ((340, 110), (340, 236), 120), ((340, 236), (310, 236), 120), ((310, 236), (300, 258), 120), ((300, 258), (300, 324), 120)], spacing=0.4, r=1.6, color=AMBER)
        self.ret = Flow([((300, 324), (616, 324), 120), ((616, 324), (616, 150), 120), ((616, 150), (475, 150), 120), ((475, 150), (475, 124), 120)], spacing=0.4, r=1.6, color=AMBER)
    def body(self, c, t):
        draw_bead(c, 308, [(360, WARM), (430, COOL), (595, COLD)], h=8)
        flat_wire(c, 292)
        c.rect(288, 254, 312, 264, fill=HOT)
        c.rect(288, 80, 312, 230, fill=TOOL, outline=TOOLE, width=1)
        c.rect(292, 230, 308, 256, fill=DARK, radius=3)
        c.polyline([(450, 110), (340, 110), (340, 236), (310, 236)], DARK, 1.0)
        c.polyline([(475, 124), (475, 150), (616, 150), (616, 324)], DARK, 1.0)
        c.rect(450, 96, 500, 124, fill='white', outline=TOOLE, width=1); c.text((475, 114), 'DC', 12, TEXT, anchor='ms')
        c.text((444, 106), '+', 12, TEXT, bold=True, anchor='rs'); c.text((482, 142), '−', 12, TEXT, bold=True)
        self.cur.draw(c, t); self.ret.draw(c, t)
        c.arrow((300, 54), (300, 74), TEXT, 1.4); c.text((308, 66), 'F', 12, TEXT, bold=True)
        label(c, (40, 240), 'wire lies on the surface'); c.dashed((174, 244), (200, 251), LEADER)
        label(c, (40, 128), 'insulated printhead, electrode tip'); c.dashed((226, 132), (286, 150), LEADER)
        label(c, (412, 232), 'I²R heating at the contact'); c.dashed((316, 256), (404, 237), LEADER)
        label(c, (412, 190), 'current returns via the substrate'); c.dashed((404, 198), (412, 196), LEADER)

# 14 --------------------------------------------------------------- micro welding
class MicroWeld(Scene):
    title = 'Micro welding'
    subtitle = 'A pulsed micro-welder tacks the wire down dot by dot; the spots overlap into a bead'
    legend = [(MOLTEN, 'molten'), (HOT, 'hot'), (COOL, 'cooling'), (COLD, 'cold')]
    def body(self, c, t):
        draw_bead(c, 300, [(595, COLD)])
        for k in range(16):                                   # spot welds, coloured by age
            age = k * 0.5 + (t % 0.5)
            x = 300 + age * V
            col = MOLTEN if age < 0.25 else (HOT if age < 0.9 else (WARM if age < 1.8 else (COOL if age < 3.2 else COLD)))
            if x < 590: c.ellipse(x - 12, 250, x + 12, 266, fill=col, outline=SEP)
        flat_wire(c, 296)
        pulse = (t % 0.5) < 0.08
        c.rect(286, 80, 314, 150, fill=TOOL, outline=TOOLE, width=1)
        c.rect(297, 150, 303, 236, fill=DARK); c.poly([(297, 232), (303, 232), (300, 242)], fill=DARK)
        if pulse:
            c.overlay(lambda l: l.poly([(299, 238), (301, 238), (310, 252), (290, 252)], fill=PLASMA), alpha=180)
            for dx in (-1, 1):
                c.line((300 + dx * 10, 246), (300 + dx * 18, 240), '#EF9F27', 1.3)
        label(c, (40, 240), 'wire lies on the surface'); c.dashed((174, 244), (200, 251), LEADER)
        label(c, (412, 121), 'pulsed micro-arc or resistance electrode'); c.dashed((304, 130), (404, 128), LEADER)
        label(c, (412, 232), 'spot welds overlap into a bead'); c.dashed((340, 250), (404, 237), LEADER)

# 15 --------------------------------------------------------------- glow-plug semisolid direct write
class Glowplug(Scene):
    title = 'Glow-plug semisolid metal direct write'
    subtitle = 'A ceramic glow plug heats the wire into a mushy semisolid that is extruded through a nozzle'
    legend = [(MOLTEN, 'molten'), (HOT, 'hot'), (COOL, 'cooling'), (COLD, 'solid grains')]
    def __init__(self):
        self.flow = Flow([((300, 58), (300, 226), 25), ((300, 226), (300, 250), 18), ((300, 250), (306, 259), 18), ((306, 259), (595, 259), V)], color=COLD)
    def body(self, c, t):
        draw_bead(c, 306, [(360, HOT), (420, WARM), (470, COOL), (595, COLD)], h=10)
        self.barrel(c, t)
        c.rect(262, 120, 274, 220, fill=TOOL, outline=TOOLE, width=1); c.rect(262, 170, 274, 220, fill=AMBER, outline='#BA7517')
        c.rect(274, 180, 282, 215, fill='#BA7517')
        self.flow.draw(c, t, cfn=lambda u, p: COLD if p[1] < 150 or p[1] > 262 else ('#8B8A83'))
        label(c, (40, 140), 'ceramic glow plug heater'); c.dashed((196, 144), (260, 160), LEADER)
        label(c, (412, 121), 'wire fed in cold'); c.dashed((306, 100), (404, 128), LEADER)
        label(c, (412, 232), 'semisolid slurry: solid grains in liquid'); c.dashed((320, 236), (404, 237), LEADER)
    def barrel(self, c, t):
        c.rect(282, 90, 318, 226, fill=TOOL, outline=TOOLE, width=1)
        c.poly([(282, 226), (318, 226), (306, 252), (294, 252)], fill=TOOL, outline=TOOLE, width=1)
        c.rect(286, 94, 314, 140, fill=LAYER); c.rect(286, 140, 314, 175, fill=WARM); c.rect(286, 175, 314, 205, fill=HOT); c.rect(286, 205, 314, 226, fill=MOLTEN)
        c.poly([(286, 226), (314, 226), (304, 250), (296, 250)], fill=MOLTEN)
        c.rect(296, 56, 304, 94, fill=LAYER, outline=SEP)

# 16 --------------------------------------------------------------- induction-heated semisolid
class Induction(Glowplug):
    title = 'Semisolid metal direct write, induction heated'
    subtitle = 'An RF coil induces eddy currents that heat the barrel and feedstock to the semisolid range'
    def body(self, c, t):
        draw_bead(c, 306, [(360, HOT), (420, WARM), (470, COOL), (595, COLD)], h=10)
        for k in range(5):                                       # back half of the coil turns
            y = 150 + 16 * k
            c.polyline([(300 + 30 * math.cos(math.radians(a)), y - 6 + 5 * math.sin(math.radians(a))) for a in range(180, 361, 12)], '#E8B99A', 2.0)
        self.barrel(c, t)
        for k in range(5):                                       # front half of the coil turns
            y = 150 + 16 * k
            c.polyline([(300 + 30 * math.cos(math.radians(a)), y + 5 * math.sin(math.radians(a))) for a in range(0, 181, 12)], COPPER, 2.4)
        c.polyline([(270, 150), (250, 150), (250, 236), (238, 236)], COPPER, 1.6); c.polyline([(270, 214), (256, 214), (256, 236)], COPPER, 1.6)
        c.text((236, 240), '~', 14, TEXT, bold=True, anchor='rs')
        ph = 2 * math.pi * 2 * t
        for i, (rx, ry) in enumerate(((44, 62), (54, 74))):
            pts = [(300 + rx * math.cos(a), 182 + ry * math.sin(a)) for a in [j * 2 * math.pi / 40 for j in range(41)]]
            for j in range(0, 40, 2):
                if (j + int(ph / (math.pi / 10))) % 4 < 2: c.line(pts[j], pts[j + 1], '#B5D4F4' if i else ELEC2, 1.0)
        self.flow.draw(c, t, cfn=lambda u, p: COLD if p[1] < 150 or p[1] > 262 else ('#8B8A83'))
        label(c, (40, 128), 'induction coil (HF supply)'); c.dashed((196, 132), (232, 150), LEADER)
        label(c, (412, 121), 'wire fed in cold'); c.dashed((306, 100), (404, 128), LEADER)
        label(c, (412, 180), 'alternating field'); c.dashed((356, 182), (404, 186), LEADER)
        label(c, (412, 232), 'semisolid slurry extruded'); c.dashed((320, 236), (404, 237), LEADER)

# 17 --------------------------------------------------------------- FDM-style hotend
class FDM(Scene):
    title = 'Semisolid metal direct write, the FDM way'
    subtitle = 'A modified FDM hotend melts low-temperature solder wire and lays it down like plastic'
    legend = [(MOLTEN, 'molten'), (HOT, 'hot'), (COOL, 'cooling'), (COLD, 'cold')]
    def __init__(self):
        self.flow = Flow([((300, 58), (300, 246), 30), ((300, 246), (306, 259), 20), ((306, 259), (595, 259), V)], color=COLD)
    def body(self, c, t):
        draw_bead(c, 306, [(350, HOT), (400, WARM), (450, COOL), (595, COLD)], h=10)
        c.rect(296, 56, 304, 250, fill=LAYER, outline=SEP)                  # filament (solder wire)
        for k in range(5):                                                  # heat-sink fins
            c.rect(272, 98 + k * 9, 328, 102 + k * 9, fill=TOOL, outline=TOOLE)
        c.rect(295, 98, 305, 160, fill=TOOL, outline=TOOLE)                 # heat break
        c.rect(274, 160, 326, 192, fill=DARK)                               # heater block
        c.circle((286, 176), 5, fill=AMBER); c.circle((314, 176), 2.5, fill='white')
        c.poly([(280, 192), (320, 192), (304, 248), (296, 248)], fill='#8B8A83', outline=TOOLE, width=1)   # nozzle
        c.poly([(297, 192), (303, 192), (302, 250), (298, 250)], fill=MOLTEN)
        c.rect(297, 160, 303, 192, fill=MOLTEN)
        a = math.degrees(2 * math.pi * 0.5 * t)
        for cx, sgn in ((286, 1), (314, -1)):
            c.circle((cx, 76), 10, fill=TOOL, outline=TOOLE, width=1)
            for i in range(8):
                an = math.radians(sgn * a + 45 * i)
                c.line((cx + 6 * math.cos(an), 76 + 6 * math.sin(an)), (cx + 10 * math.cos(an), 76 + 10 * math.sin(an)), SEP, 1.2)
        self.flow.draw(c, t, cfn=lambda u, p: COLD if p[1] < 162 else (DARK if p[0] > 306 else MOLTEN))
        label(c, (340, 80), 'drive gears push solder wire'); c.dashed((326, 76), (336, 80), LEADER)
        label(c, (40, 120), 'heat sink and heat break'); c.dashed((186, 124), (270, 118), LEADER)
        label(c, (412, 180), 'heater block + nozzle, < 500 °C'); c.dashed((322, 186), (404, 186), LEADER)
        label(c, (412, 232), 'molten / semisolid solder bead'); c.dashed((326, 250), (404, 237), LEADER)

# 18 --------------------------------------------------------------- hot tool orbital friction stirring
class Orbital(Scene):
    title = 'Hot-tool orbital friction stirring'
    subtitle = 'A heated foot orbits in a small circle (no spin), stirring the wire into the layer below'
    def __init__(self):
        self.flow = Flow([((47.1, 128), (268, 255.5), 60), ((268, 255.5), (322, 258), 40), ((322, 258), (595, 258), V)])
    def body(self, c, t):
        draw_bead(c, 322, STD_RAMP)
        wire30(c, (268, 255.5))
        c.rect(276, 254, 324, 264, fill=HOT)
        dx = 6 * math.cos(2 * math.pi * 3 * t)
        c.rect(286 + dx, 90, 314 + dx, 236, fill=TOOL, outline=TOOLE, width=1)
        heater_band(c, 286 + dx, 314 + dx, 120, 142)
        c.rect(278 + dx, 236, 322 + dx, 252, fill=COOL, outline=TOOLE, width=1, radius=3)
        pts = [(300 + 12 * math.cos(a), 244 + 4 * math.sin(a)) for a in [i * 2 * math.pi / 32 for i in range(33)]]
        for i in range(0, 32, 2): c.line(pts[i], pts[i + 1], TEXT, 1.0)
        curve_arrow(c, [(300 + 24 * math.cos(math.radians(a)), 70 + 6 * math.sin(math.radians(a))) for a in range(200, 345, 10)], TEXT)
        c.text((330, 66), 'orbit', 11, TEXT)
        heat_down(c, [292, 300, 308], SURF + 1, 16)
        self.flow.draw(c, t)
        label(c, (40, 86), 'wire fed in at 30°', (90, 141))
        label(c, (412, 153), 'heated foot orbits, does not spin'); c.dashed((326, 190), (404, 158), LEADER)
        label(c, (412, 232), 'stir zone: hot and sheared, no melt'); c.dashed((326, 257), (404, 237), LEADER)

# 19 --------------------------------------------------------------- hot tool rotary vibro welding
class RotaryVibro(Scene):
    title = 'Hot-tool rotary vibro welding'
    subtitle = 'A heated tool twists back and forth a few degrees at high frequency to friction-heat the wire'
    def body(self, c, t):
        draw_bead(c, 320, STD_RAMP)
        flat_wire(c, 280)
        c.rect(278, 254, 322, 264, fill=HOT)
        c.rect(280, 90, 320, 252, fill=TOOL, outline=TOOLE, width=1)
        ph = math.radians(40) * math.sin(2 * math.pi * 4 * t)
        for i in range(6):
            a = 2 * math.pi * i / 6 + ph
            if math.cos(a) > 0.05:
                c.line((300 + 18 * math.sin(a), 96), (300 + 18 * math.sin(a), 248), '#9A9891', 1.0 * (0.5 + 0.6 * math.cos(a)))
        heater_band(c, 280, 320, 120, 142)
        arcpts = [(300 + 30 * math.cos(math.radians(a)), 76 + 7 * math.sin(math.radians(a))) for a in range(200, 341, 10)]
        c.polyline(arcpts, TEXT, 1.3); c.arrow(arcpts[-2], arcpts[-1], TEXT, 1.3, 6); c.arrow(arcpts[1], arcpts[0], TEXT, 1.3, 6)
        heat_down(c, [292, 300, 308], SURF + 1, 16)
        label(c, (40, 240), 'wire lies on the surface'); c.dashed((174, 244), (200, 251), LEADER)
        label(c, (412, 121), 'rotary oscillation, ± a few degrees'); c.dashed((332, 90), (404, 128), LEADER)
        label(c, (412, 153), 'heater in the tool'); c.dashed((322, 131), (404, 158), LEADER)
        label(c, (412, 232), 'hot tool + shear bond the wire'); c.dashed((324, 257), (404, 237), LEADER)

# 20 --------------------------------------------------------------- hot tool linear vibro welding
class LinearVibro(Scene):
    title = 'Hot-tool linear vibro welding'
    subtitle = 'A heated tool shuttles along the travel direction at high frequency to friction-heat the wire'
    def body(self, c, t):
        draw_bead(c, 320, STD_RAMP)
        flat_wire(c, 280)
        c.rect(278, 254, 322, 264, fill=HOT)
        dx = 5 * math.sin(2 * math.pi * 5 * t)
        c.rect(280 + dx, 90, 320 + dx, 252, fill=TOOL, outline=TOOLE, width=1)
        heater_band(c, 280 + dx, 320 + dx, 120, 142)
        c.dbl_arrow((272, 78), (328, 78), TEXT, 1.3, 6)
        heat_down(c, [292, 300, 308], SURF + 1, 16)
        label(c, (40, 240), 'wire lies on the surface'); c.dashed((174, 244), (200, 251), LEADER)
        label(c, (412, 121), 'linear oscillation along travel'); c.dashed((332, 80), (404, 128), LEADER)
        label(c, (412, 153), 'heater in the tool'); c.dashed((322, 131), (404, 158), LEADER)
        label(c, (412, 232), 'hot tool + shear bond the wire'); c.dashed((324, 257), (404, 237), LEADER)
