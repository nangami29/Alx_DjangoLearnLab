from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)

    
    def __str__(self):
        return self.name
    #Extend the Book Model with Custom Permission
class Book(models.Model):
    title=models.CharField
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    class Meta:
        permissions = [
        ('can_add_book', 'Can add book'),
        ('can_change_book', 'Can change book'),
        ('can_delete_book', 'Can delete book'),
    ]


    
    

class Library(models.Model):
    name=models.CharField
    books=models.ManyToManyField(Book)

    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name=models.CharField
    library=models.OneToOneField(Library, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    
    #Step 1: Extend the User Model with a UserProfile
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member')
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField

    def __str__(self):
        return self.name
