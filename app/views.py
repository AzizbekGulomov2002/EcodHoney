from django.shortcuts import render
from django.views import View
from .models import Header, AboutUs, HoneySorts, Facts, Shop,Mission

class IndexView(View):
    def get(self, request):
        context = {
            'headers': Header.objects.all(),
            'about_us': AboutUs.objects.first(),
            'honey_sorts': HoneySorts.objects.all(),
            'facts': Facts.objects.all(),
            'shops': Shop.objects.all(),
            'mission': Mission.objects.first(),
        }
        return render(request, 'index.html', context)


def header_list(request):
    headers = Header.objects.all()
    return render(request, 'header_list.html', {'headers': headers})

def about(request):
    about_us = AboutUs.objects.all()  # Fetching all AboutUs objects
    return render(request, 'about.html', {'about_us': about_us})

def facts_list(request):
    facts = Facts.objects.all()
    return render(request, 'facts_list.html', {'facts': facts})

def shop_list(request):
    shops = Shop.objects.all()
    about = AboutUs.objects.first()  # Assuming there's only one AboutUs object
    return render(request, 'shop.html', {'shops': shops, 'about': about})

def quality(request):
    quality = HoneySorts.objects.all()
    return render(request, 'quality.html', {'quality': quality, 'about': about})