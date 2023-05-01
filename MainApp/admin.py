from django.contrib import admin
from . import models
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ("id","Title")


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id","Title")


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("id","Name","Message")




class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id","Icon","Title")




admin.site.register(models.Home,HomeAdmin)
admin.site.register(models.AboutUs,AboutUsAdmin)
admin.site.register(models.ContactUs,ContactUsAdmin)
admin.site.register(models.Services,ServicesAdmin)
