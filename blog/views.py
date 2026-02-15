from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, About, CaruselBanner, Article, ArticleMore, Contact, Comment
import requests
from django.conf import settings
# Create your views here.

def my_profil(request):
    person = Person.objects.all()
    
    context = {
        'persons': person
    }
    
    return render(request, 'base.html', context)


def home_page(request):
    carusel = CaruselBanner.objects.all()
    article = Article.objects.all().order_by('-published_date')

    
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
    success_message = None
    error_message = None

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # ✅ backend validatsiya
        if not name or not email or not subject or not message:
            error_message = "Iltimos, barcha maydonlarni to'ldiring ❗"
            return render(request, "contact.html", {
                "success_message": success_message,
                "error_message": error_message
            })

        text = (
            "📩 Yangi kontakt xabari!\n\n"
            f"👤 Ism: {name}\n"
            f"📧 Email: {email}\n"
            f"🧾 Mavzu: {subject}\n"
            f"📝 Xabar:\n{message}"
        )

        url = f"https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage"
        r = requests.post(url, data={"chat_id": settings.TG_CHAT_ID, "text": text}, timeout=10)

        if r.status_code == 200:
            success_message = "Xabaringiz yuborildi ✅"
        else:
            error_message = "Xabar yuborishda xatolik bo'ldi. Keyinroq urinib ko'ring ❗"

    return render(request, "contact.html", {
        "success_message": success_message,
        "error_message": error_message
    })


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
        'article_mores': article_more,
        'comment': comment,
        'comment_count': comment_count,
        'success_message': success_message,
        
    }
        
    return render(request, 'single.html', context)