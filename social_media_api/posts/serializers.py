from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']

class CommentSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only =True)
    class Meta:
        models = Comment
        fields = ['post', 'content', 'author']