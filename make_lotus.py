from PIL import Image, ImageDraw
import math

# Transparent canvas
S = 1000
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

cx, cy = S // 2, int(S * 0.60)
saffron = (255, 130, 40, 255)
saff_light = (255, 165, 80, 255)

def petal(cx, cy, angle_deg, length, width, color):
    """Draw a petal as a rotated ellipse-like polygon pointing outward."""
    a = math.radians(angle_deg)
    pts = []
    # build a leaf/petal shape along the axis
    steps = 24
    for i in range(steps + 1):
        t = i / steps
        # width profile (0 at tip and base, max in middle)
        w = width * math.sin(math.pi * t)
        # position along axis
        px = t * length
        # left side
        pts.append((px, w))
    for i in range(steps, -1, -1):
        t = i / steps
        w = width * math.sin(math.pi * t)
        px = t * length
        pts.append((px, -w))
    # rotate & translate
    rot = []
    for (x, y) in pts:
        rx = cx + x * math.cos(a) - y * math.sin(a)
        ry = cy + x * math.sin(a) + y * math.cos(a)
        rot.append((rx, ry))
    d.polygon(rot, fill=color, outline=(230, 90, 20, 255))

# Bottom base petals (wider, pointing down-out)
petal(cx, cy, 110, 300, 90, saff_light)
petal(cx, cy, 70, 300, 90, saff_light)

# Middle petals
petal(cx, cy, 130, 330, 80, saffron)
petal(cx, cy, 50, 330, 80, saffron)

# Upper side petals
petal(cx, cy, 152, 340, 75, saff_light)
petal(cx, cy, 28, 340, 75, saff_light)

# Center tall petal (pointing up)
petal(cx, cy, -90, 360, 95, saffron)
# two inner upper petals
petal(cx, cy, -65, 340, 80, saff_light)
petal(cx, cy, -115, 340, 80, saff_light)

# small stem/base green arc
d.arc([cx-160, cy+40, cx+160, cy+220], start=200, end=340, fill=(19,136,8,255), width=22)

img.save("bjp-logo.png")
print("lotus watermark saved")
