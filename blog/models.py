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
        
        


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="article/", null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    
    def __str__(self):
        return self.title
    
    
class ArticleMore(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    published_date = models.DateTimeField(auto_now_add=True)  
    photo = models.ImageField(upload_to='article/', null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="more_articles")
    title_topic = models.CharField(max_length=200)
    description_topic = models.TextField()
    photo_topic = models.ImageField(upload_to='article_topic/', null=False, blank=False)


    def __str__(self):
        return self.title
    
    
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.name}'