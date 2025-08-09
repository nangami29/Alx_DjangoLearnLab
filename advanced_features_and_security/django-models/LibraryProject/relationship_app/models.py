from django.db import models

from django.conf import settings

user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

from django.contrib.auth.models import User, AbstractUser

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
    
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth=None, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, date_of_birth, password, **extra_fields)


# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


