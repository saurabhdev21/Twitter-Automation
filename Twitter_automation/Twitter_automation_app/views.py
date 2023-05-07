from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .services.twitter import get_tweet_text


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request=request))


def submit_page(request):
    if request.method == 'POST':
        tweet_link = request.POST.get('tweet-link')
        tweet_text = get_tweet_text(tweet_link)
        return render(request, 'submit_page.html', {'tweet_link': tweet_text})
    else:
        return render(request, 'main.html')
