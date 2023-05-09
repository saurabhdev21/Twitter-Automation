import os

from django.shortcuts import render
from .services.twitter import generate_tweet_image

def main(request):
    if request.method == 'POST':
        print("we are inside main, part 1")
        # Retrieve form data
        color = request.POST['color']
        font_style = request.POST['font-style']
        text = request.POST['text']
        font_color = request.POST['font-color']

        print("we are inside main")

        # Render submit page with form data

        context = {'color': color, 'font_style': font_style, 'text': text, 'font_color': font_color}
        print("we are inside main, part end")
        return render(request, 'submit_page.html', context)
    else:
        return render(request, 'main.html')


def submit_page(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        font_style = request.POST.get('font-style')
        text = request.POST.get('text')
        font_color = request.POST.get('font-color')
        print("we are inside submit_page, part end")

        context = {
            'color': color,
            'font_style': font_style,
            'text': text,
            'font_color': font_color
        }
        print(font_color)
        image, image_name = generate_tweet_image(color, font_color, text)
        return render(request, 'submit_page.html', {'image_name': image_name})
