from email.mime import image

from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.CharField(null=True, blank=True, max_length="2038")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255)



    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
       #return reverse('article_detail', args=(str(self.id)))
       return reverse('home'),

