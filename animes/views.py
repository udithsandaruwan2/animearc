from django.shortcuts import render, redirect
from .utils import getAnimeList, getEpi
from urllib.parse import quote, unquote
from django.http import HttpRequest
from django.urls import reverse

def animes(request):
    context = {}
    return render(request, 'animes/animes.html', context)


def btth(request: HttpRequest):
    episodes = getAnimeList('https://luciferdonghua.in/anime/battle-through-the-heavens-season-5/')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        encoded_url = quote(url, safe='')
        return redirect(reverse('single-epi') + f'?title={title}&url={encoded_url}')
    
    context = {'episodes': episodes}
    return render(request, 'animes/btth.html', context)

def singleEpi(request):
    title = request.GET.get('title')
    url = request.GET.get('url')
    episode = getEpi(url)
    
    context = {'title': title, 'episode': episode}
    return render(request, 'animes/single-epi.html', context)

# def downloadEpi(request):
#     download_video = 
#     pass
