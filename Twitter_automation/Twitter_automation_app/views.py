from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .services.twitter import generate_tweet_image



def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request=request))



def submit_page(request):
    if request.method == 'POST':
        tweet_link = request.POST.get('tweet-link')
        image, image_name = generate_tweet_image(tweet_link)
        return render(request, 'submit_page.html', {'image_name': image_name})
    else:
        return render(request, 'main.html')
