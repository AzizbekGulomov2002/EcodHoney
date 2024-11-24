from django.urls import path
from .views import IndexView, header_list, about,shop_list,quality
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('headers/', header_list, name='header_list'),
    path('about/', about, name='about_us'),
    path("shop/",shop_list, name='shop'),
    path("quality/",quality, name='quality')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 
