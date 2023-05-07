from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request=request))


def submit_page(request):
    if request.method == 'POST':
        tweet_link = request.POST.get('tweet-link')
        return render(request, 'submit_page.html', {'tweet_link': tweet_link})
    else:
        return render(request, 'main.html')
