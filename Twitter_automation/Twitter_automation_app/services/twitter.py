import textwrap
from PIL import Image, ImageDraw, ImageFont
import os
import random
import string


def generate_tweet_image(color, text_color, tweet_text):
    # Set up the image size and font properties
    image_width, image_height = 800, 600
    print("we are inside the generate tweet image function")
    font_size = 40
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    font_path = os.path.join(base_dir, "fonts/arial", "arial.ttf")
    font = ImageFont.truetype(font_path, font_size)
    # Split the tweet text into multiple lines
    wrapped_lines = textwrap.wrap(tweet_text, width=int(image_width/font_size))


    # Create the image object and the drawing context
    image = Image.new('RGB', (image_width, image_height), color=color)
    # image = image.resize((108, 108))
    draw = ImageDraw.Draw(image)

    # Define the starting coordinates for the first line of text
    x, y = 50, 50

    # Render each line of text onto the image
    font_color = get_rgb(text_color)
    print(font_color)
    for line in wrapped_lines:
        draw.text((x, y), line, font=font, fill=font_color)
        y += font.getsize(line)[1] + 10

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_name = "tweet_image_" + generate_random_string(5) + ".png"

    font_path = os.path.join(base_dir, "static", image_name)


    image.save(font_path)
    print("we have saved and generated the image")
    # Return the image object
    return image, image_name


def generate_random_string(length=6):
    """Generate a random string with the given length."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_rgb(color_name):
    colors = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 128, 0),
        "BLUE": (0, 0, 255),
        "YELLOW": (255, 255, 0),
        "CYAN": (0, 255, 255),
        "MAGENTA": (255, 0, 255)
    }
    return colors.get(color_name, (255, 255, 255))


