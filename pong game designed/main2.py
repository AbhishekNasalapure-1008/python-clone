from PIL import Image, ImageDraw
import random

def create_starry_background(width, height, num_stars):
    # Create a new black image
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)

    # Draw stars
    for _ in range(num_stars):
        x = random.randint(0, width)
        y = random.randint(0, height)
        brightness = random.randint(100, 255)
        size = random.randint(1, 3)
        color = (brightness, brightness, brightness)
        draw.ellipse([x, y, x+size, y+size], fill=color)

    # Save the image
    image.save('starry_background.png')
    print("Starry background created and saved as 'starry_background.png'")

# Create a 800x600 background with 200 stars
create_starry_background(800, 600, 200)