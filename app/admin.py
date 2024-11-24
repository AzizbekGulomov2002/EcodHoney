from django.contrib import admin
from .models import Header, SocialMedia, AboutUs, HoneySorts, Facts, Shop,Mission

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text')
    search_fields = ('title',)

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)
    filter_horizontal = ('contacts',)

@admin.register(HoneySorts)
class HoneySortsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

@admin.register(Facts)
class FactsAdmin(admin.ModelAdmin):
    list_display = ('text', 'image')
    search_fields = ('text',)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'office', 'phone', 'email', 'address')
    search_fields = ('name', 'email')


admin.site.register(Mission)