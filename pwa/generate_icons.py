from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded background with smooth gradient-like color
    bg_color = (37, 99, 235, 255) # Royal Blue #2563EB
    r = int(size * 0.22)
    draw.rounded_rectangle([0, 0, size, size], radius=r, fill=bg_color)
    
    # Accent circle inside
    draw.ellipse([size * 0.15, size * 0.15, size * 0.85, size * 0.85], fill=(59, 130, 246, 255))
    
    # Draw simple text or geometric shapes
    # Draw a stylized book / multimedia play badge
    # Draw play triangle
    poly = [
        (size * 0.42, size * 0.35),
        (size * 0.42, size * 0.65),
        (size * 0.68, size * 0.50)
    ]
    draw.polygon(poly, fill=(255, 255, 255, 255))
    
    # Draw small star or badge
    draw.ellipse([size * 0.65, size * 0.22, size * 0.78, size * 0.35], fill=(250, 204, 21, 255))

    img.save(filename)
    print(f"Saved {filename} ({size}x{size})")

os.makedirs("pwa/icons", exist_ok=True)
create_icon(192, "pwa/icons/icon-192.png")
create_icon(512, "pwa/icons/icon-512.png")
create_icon(180, "pwa/icons/apple-touch-icon.png")
