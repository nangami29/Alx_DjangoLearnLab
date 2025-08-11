from django.db import models
    
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "can view book"),
            ("can_create", "can create book"),
            ("can_edit", "can edit book"),
            ("can_delete", "can delete book")
             
        ]
    
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
    

#creating a group
editors_group = Group.objects.create(name='Editors')
viewers_group= Group.objects.create(name='Viewers')
admin_group = Group.objects.create(name='Admins')



@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == 'app_name':  # replace with your app name
        content_type = ContentType.objects.get_for_model(Book)

        # Get permissions
        can_view = Permission.objects.get(codename='can_view', content_type=content_type)
        can_create = Permission.objects.get(codename='can_create', content_type=content_type)
        can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
        can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

        # Editors group
        editors, _ = Group.objects.get_or_create(name='Editors')
        editors.permissions.set([can_edit, can_create, can_view])

        # Viewers group
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        viewers.permissions.set([can_view])

        # Admins group
        admins, _ = Group.objects.get_or_create(name='Admins')
        admins.permissions.set([can_view, can_create, can_edit, can_delete])
