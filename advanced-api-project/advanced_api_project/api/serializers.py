from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

#custom validation for publication year
    def validate(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
       
class AuthorSerializer(serializers.ModelSerializer):
    name= serializers.CharField()
    # nested serializers
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']
