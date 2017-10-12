from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    public_date = models.DateField(null=True)
    icon = models.ImageField(null=True)

    class Meta:
        ordering = ['-id']

class Log(models.Model):
    LOG_TYPE_CHOICES = (
        ('DEL', 'DELETE'),
        ('UP', 'UPDATE'),
    )

    time = models.DateField()
    id_author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=LOG_TYPE_CHOICES)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    public_date = models.DateField()
    icon = models.ImageField()

