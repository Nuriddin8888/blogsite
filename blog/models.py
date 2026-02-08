from django.db import models

# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
    
    
    

class About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="avatars/")
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    

class CaruselBanner(models.Model):
    title = models.CharField(max_length=255)
    bg = models.ImageField(upload_to="carusel/")
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="carusel")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Carusel Banner"
        verbose_name_plural = "Carusel Banners"