from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    body = models.TextField(null=True, blank=True)	
    create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', default='dupa.jpg')

    

    def __str__(slef):
        return slef.title


class Meta:
    ordering = ['state']
