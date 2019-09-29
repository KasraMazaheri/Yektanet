from django.contrib import admin
from advertiser_management.models import Ad, Advertiser, Click, View

# Register your models here.

class AdAdmin(admin.ModelAdmin):
    search_fields = ['title', 'link']
    list_filter = ['approved']
    list_display = ['title', 'link', 'approved']
    ordering = ['title']
    actions = ['approve_ad']

    def approve_ad(self, request, queryset):
        ads_updated = queryset.update(approved = 1)
        if ads_updated == 1:
            message = "1 ad was"
        else:
            message = "%s ads were" %ads_updated
        message += " successfully marked as approved."
        self.message_user(request, message)
    approve_ad.short_description = "Mark selected ads as approved"

class AdvertiserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    ordering = ['name']

admin.site.register(Ad, AdAdmin)
admin.site.register(Advertiser, AdvertiserAdmin)
