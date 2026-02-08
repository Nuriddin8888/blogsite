from django.urls import path
from .views import home_page, about_page, blog_page, contact_page, single_page

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('blog/', blog_page, name="blog"),
    path('contact/', contact_page, name="contact"),
    path('single/<int:id>/', single_page, name="single"),
]