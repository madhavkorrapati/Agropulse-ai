"""
Helper script to generate clean sample leaf images for offline testing.
"""
import os
from PIL import Image, ImageDraw

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data", "sample_leaves")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_leaf(filename, base_color, spot_color=None, spots=None, stripe_color=None):
    img = Image.new("RGB", (400, 400), (240, 243, 240))
    draw = ImageDraw.Draw(img)

    # Draw leaf base oval / polygon
    draw.polygon([
        (200, 30),
        (280, 110),
        (330, 210),
        (300, 320),
        (200, 370),
        (100, 320),
        (70, 210),
        (120, 110)
    ], fill=base_color, outline=(30, 80, 30), width=3)

    # Draw central vein
    draw.line([(200, 40), (200, 360)], fill=(40, 100, 40), width=4)
    # Side veins
    for y in range(80, 330, 40):
        draw.line([(200, y), (260, y - 25)], fill=(50, 120, 50), width=2)
        draw.line([(200, y), (140, y - 25)], fill=(50, 120, 50), width=2)

    # Draw spots if specified (e.g. blight / rust spots)
    if spot_color and spots:
        for (sx, sy, sr) in spots:
            draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=spot_color, outline=(40, 20, 10), width=1)
            # Concentric ring for early blight
            if "early" in filename:
                draw.ellipse([sx - sr//2, sy - sr//2, sx + sr//2, sy + sr//2], outline=(100, 50, 20), width=1)

    if stripe_color:
        for x in [160, 180, 220, 240]:
            draw.line([(x, 100), (x, 300)], fill=stripe_color, width=3)

    path = os.path.join(OUTPUT_DIR, filename)
    img.save(path, "JPEG", quality=90)
    print(f"Generated sample leaf: {filename}")

if __name__ == "__main__":
    # 1. Tomato Early Blight (Green leaf with concentric dark brown target spots)
    create_leaf("tomato_early_blight.jpg", (95, 145, 60), spot_color=(90, 45, 20), spots=[
        (160, 150, 22), (240, 190, 28), (170, 260, 18), (220, 290, 15), (270, 140, 14)
    ])

    # 2. Tomato Late Blight (Dark water-soaked necrotic lesions)
    create_leaf("tomato_late_blight.jpg", (80, 120, 50), spot_color=(45, 35, 30), spots=[
        (180, 110, 45), (250, 170, 40), (140, 220, 38), (210, 300, 42)
    ])

    # 3. Healthy Crop (Pure vibrant green)
    create_leaf("healthy_crop.jpg", (46, 170, 60))

    # 4. Rice Blast (Spindle/diamond lesions)
    create_leaf("rice_blast.jpg", (100, 160, 70), spot_color=(120, 80, 40), spots=[
        (190, 120, 18), (210, 190, 22), (180, 250, 16), (220, 290, 15)
    ])

    # 5. Corn Common Rust (Orange/cinnamon pustules)
    create_leaf("corn_common_rust.jpg", (130, 165, 60), spot_color=(195, 95, 20), spots=[
        (170, 120, 10), (190, 140, 12), (230, 160, 11), (160, 200, 12),
        (220, 230, 10), (180, 270, 11), (240, 290, 12)
    ])
