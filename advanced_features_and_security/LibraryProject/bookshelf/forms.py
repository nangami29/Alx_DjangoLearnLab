from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """Form for creating or editing Book objects securely."""
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
    
    def clean_title(self):
        """Extra validation for title to prevent malicious input."""
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid characters in title.")
        return title
