from django.contrib import admin
from .models import Person, About, CaruselBanner, Category, Article, ArticleMore, Comment, Contact
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CaruselBanner)
class CaruselBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']


@admin.register(ArticleMore)
class ArticleMoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']

        
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'article', 'message']