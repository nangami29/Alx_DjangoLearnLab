from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Integrate Tagging Functionality
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') 
    #tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    tags = TaggableManager(blank=True)
    
    def __str__(self):
        return self.title
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio= models.TextField(blank=True, null=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    def __str_(self):
        return f"{self.user.username}'s Profile"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()

