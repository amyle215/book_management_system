from django.db import models

# Create your models here.
TYPE_BOOK_CHOICE = (
    (0, 'History'),
    (1, 'Novel'),
    (2, 'Physics'),
)
class Book(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices= TYPE_BOOK_CHOICE)

    class Meta:
        db_table = "book"
        ordering = ['-id']