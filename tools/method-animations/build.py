import sys, os, time
from PIL import Image
from engine import *
import scenes_a as A, scenes_b as B

SCENES = [
    ('afsd', A.AFSD), ('afed', A.AFED), ('afrb', A.AFRB),
    ('laser-wire-ded', A.LaserDED),
    ('cold-spray', A.ColdSpray), ('flame-spray', A.FlameSpray),
    ('ultrasonic-am', A.UAM), ('thermosonic-am', A.Thermosonic),
    ('electrochemical-am', A.ECAM), ('laser-induced-ecd', A.LaserECD),
    ('micro-powerhammer', B.Powerhammer), ('micro-arc-plasma', B.MicroArc),
    ('joule-printing', B.Joule), ('micro-welding', B.MicroWeld),
    ('glowplug-semisolid', B.Glowplug), ('induction-semisolid', B.Induction), ('fdm-semisolid', B.FDM),
    ('hot-tool-orbital', B.Orbital), ('hot-tool-rotary-vibro', B.RotaryVibro), ('hot-tool-linear-vibro', B.LinearVibro),
]

def contact_sheet(path, t=1.3, cols=2):
    ims = []
    for slug, cls in SCENES:
        c = Canvas(); cls().draw(c, t); ims.append(c.finish())
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (W * cols, H * rows), '#DDD')
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * W, (i // cols) * H))
    sheet.save(path)

if __name__ == '__main__':
    if sys.argv[1] == 'sheet':
        contact_sheet(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 1.3)
    elif sys.argv[1] == 'frame':
        slug, t = sys.argv[2], float(sys.argv[3])
        cls = dict(SCENES)[slug]; c = Canvas(); cls().draw(c, t); c.finish().save(sys.argv[4])
    elif sys.argv[1] == 'gifs':
        only = sys.argv[2:]  # optional subset
        os.makedirs('out', exist_ok=True)
        for slug, cls in SCENES:
            if only and slug not in only: continue
            t0 = time.time()
            size = render(cls(), 'frames/' + slug, 'out/%s.gif' % slug)
            print('%-24s %6.0f KB  %.1fs' % (slug, size / 1024, time.time() - t0), flush=True)
