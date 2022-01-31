from statistics import mode
from turtle import title
from django.db import models

# Create your models here.


class PostTest(models.Model):
    title= models.CharField(max_length=2020)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:20]


    class Meta:
        ordering = ['-updated']

