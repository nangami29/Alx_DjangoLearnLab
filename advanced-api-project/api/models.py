from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    # a foreign key linking to the Author model, establishing a one-to-many relationship from Author to Books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


