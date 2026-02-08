from django.contrib import admin
from .models import Person, About, CaruselBanner, Category
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CaruselBanner)
class CaruselBannerAdmin(admin.ModelAdmin):
    list_display = ['title', "category", "published_date"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']