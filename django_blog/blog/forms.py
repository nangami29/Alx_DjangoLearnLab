from django import forms 
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio', 'profile_picture']

class TagWidget(forms.TextInput):
    template_name = 'tag_widget.html'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {'placeholder': 'Enter tags separated by commas'})
        super().__init__(*args, **kwargs)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields =['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(), }


#create comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['post', 'content']
        
class TagForm (forms.ModelForm):
    class Meta:
        model = Tag
        fields= ['name']

