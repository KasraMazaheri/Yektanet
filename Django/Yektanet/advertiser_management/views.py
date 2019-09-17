from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import RedirectView

from .models import Advertiser, Ad


def Home(request):
    for ad in Advertiser.objects.all():
        ad.incViews()
    context = {'advertisers': Advertiser.objects.all()}
    return render(request, 'advertiser_management/home.html', context)


def RedirectToAd(request, ad_id):
    ad = get_object_or_404(Ad, pk = ad_id)
    ad.incClicks()
    return RedirectView.as_view(url = ad.link)(request)


def Create(request):
    if request.method == 'GET':
        return render(request, 'advertiser_management/create.html')

    _name = request.POST['advertiser']
    _title = request.POST['title']
    _image = request.POST['image']
    _link = request.POST['link']
    
    A = Advertiser.objects.all().filter(name = _name)
    if A.count() > 0:
        advertiser = A[0]
    else:
        advertiser = Advertiser(name = _name)
        advertiser.save()

    ad = Ad(title = _title, image = _image, link = _link, _advertiser = advertiser)
    ad.save()
        
    return RedirectView.as_view(url = '../home')(request)
