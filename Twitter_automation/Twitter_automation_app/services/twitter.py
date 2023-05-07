import textwrap
from PIL import Image, ImageDraw, ImageFont
import os

def generate_tweet_image(tweet_text):
    # Set up the image size and font properties
    image_width, image_height = 800, 600
    font_size = 40
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    font_path = os.path.join(base_dir, "fonts/arial", "arial.ttf")
    font = ImageFont.truetype(font_path, font_size)
    # Split the tweet text into multiple lines
    wrapped_lines = textwrap.wrap(tweet_text, width=int(image_width/font_size))

    # Create the image object and the drawing context
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    # Define the starting coordinates for the first line of text
    x, y = 50, 50

    # Render each line of text onto the image
    for line in wrapped_lines:
        draw.text((x, y), line, font=font, fill=(0, 0, 0))
        y += font.getsize(line)[1] + 10

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_name = "tweet_image_" + generate_random_string(2) + ".png"

    font_path = os.path.join(base_dir, "generate_image", image_name)

    image.save(font_path)
    # Return the image object
    return image

import random
import string

def generate_random_string(length=6):
    """Generate a random string with the given length."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

