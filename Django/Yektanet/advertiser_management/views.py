from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse
from django.views.generic.base import RedirectView, TemplateView

from .models import Advertiser, Ad, Click, View

def get_user_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if (ip):
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return (ip)

class HomeView(TemplateView):
    template_name = 'advertiser_management/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        for _ad in Ad.objects.all():
            if (_ad.approved):
                view = View(ip = get_user_ip(self.request), ad = _ad)
                view.save()
        context['advertisers'] = Advertiser.objects.all()
        return context

class RedirectToAdView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        _ad = get_object_or_404(Ad, pk = kwargs['ad_id'])
        if (_ad.approved == 0):
            raise Http404
        self.url = _ad.link
        click = Click(ip = get_user_ip(self.request), ad = _ad)
        click.save()
        return super().get_redirect_url(*args, **kwargs)

def create(request):
    if request.method == 'GET':
        return render(request, 'advertiser_management/create.html')

    _name = request.POST['advertiser']
    _title = request.POST['title']
    _image = request.POST['image']
    _link = request.POST['link']
    
    A = Advertiser.objects.all().filter(name = _name)
    if A.count() > 0:
        _advertiser = A[0]
    else:
        _advertiser = Advertiser(name = _name)
        _advertiser.save()

    ad = Ad(title = _title, image = _image, link = _link, advertiser = _advertiser)
    ad.save()
        
    return RedirectView.as_view(url = '../home')(request)

class StatsView(TemplateView):
    template_name = 'advertiser_management/stats.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        T = []
        L = []
        L.append('Ad\Hour')
        for i in range(24):
            L.append(i)
        context['header_table'] = L
        
        for ad in Ad.objects.all():
            if ad.approved:
                L = []
                L.append(ad.title)
                cnt = [0] * 24
                for click in ad.click_set.all():
                    cnt[click.get_time()] += 1
                for i in cnt:
                    L.append(i)
                T.append(L)
        context['clicks_table'] = T

        T = []
        for ad in Ad.objects.all():
            if ad.approved:
                L = []
                L.append(ad.title)
                cnt = [0] * 24
                for view in ad.view_set.all():
                    cnt[view.get_time()] += 1
                for i in cnt:
                    L.append(i)
                T.append(L)
        context['views_table'] = T

        T = []
        L = []
        L.append('Ad\Hour')
        for i in range(24):
            L.append(i)
        L.append('Overall')
        context['header_2_table'] = L

        S = []
        for ad in Ad.objects.all():
            if ad.approved:
                clicks = ad.click_set.count()
                views = ad.view_set.count()
                if views != 0:
                    S.append([clicks / views, ad])
                else:
                    S.append([0, ad])
        S.sort()
        S.reverse()
        for s in S:
            ad = s[1]
            L = []
            cnt_click = [0] * 24
            cnt_view = [0] * 24
            for click in ad.click_set.all():
                cnt_click[click.get_time()] += 1
            for view in ad.view_set.all():
                cnt_view[view.get_time()] += 1
            L.append(ad.title)
            for i in range(24):
                if cnt_view[i] == 0:
                    L.append('N/A')
                else:
                    L.append(cnt_click[i] / cnt_view[i])
            L.append(s[0])
            T.append(L)
        context['ratio_table'] = T

        T = []
        for ad in Ad.objects.all():
            if ad.approved:
                sm = 0
                for click in ad.click_set.all():
                    last = None
                    for view in ad.view_set.all():
                        if click.ip == view.ip and view.time < click.time:
                            if last == None:
                                last = view
                            elif last.time < view.time:
                                last = view
                    tt = click.time - last.time
                    sm += tt.seconds
                sm /= ad.click_set.count()
                T.append([ad.title, sm])
        context['average_table'] = T
        
        return context


