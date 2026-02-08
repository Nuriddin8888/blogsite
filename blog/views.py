from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, About, CaruselBanner, Article, ArticleMore, Contact, Comment
# Create your views here.

def my_profil(request):
    person = Person.objects.all()
    
    context = {
        'persons': person
    }
    
    return render(request, 'base.html', context)


def home_page(request):
    carusel = CaruselBanner.objects.all()
    article = Article.objects.all()
    
    context = {
        'carusels': carusel[:3],
        'articles': article
    }
    
    return render(request, 'index.html', context)


def about_page(request):
    about = About.objects.all()
    
    context = {
        'abouts': about
    }
    
    return render(request, 'about.html', context)


def blog_page(request):
    return render(request, 'blog.html')


def contact_page(request):
    return render(request, 'contact.html')



def single_page(request, id):
    success_message = None
    
    
    article = get_object_or_404(Article, id=id)
    article_more = ArticleMore.objects.filter(category=article.category)
    comment = Comment.objects.filter(article=article)
    comment_count = comment.count()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        pk = request.POST.get('pk') 
    
        Comment.objects.create(
            name=name,
            email=email,
            message=message,
            article=article
        )
        
        success_message = 'Habar muvaffaqqiyatli yuborildi!!!'
        return redirect('home')
    
    
    context = {
        'article': article,
        'article_more': article_more,
        'comment': comment,
        'comment_count': comment_count,
        'success_message': success_message,
        
    }
        
    return render(request, 'single.html', context)