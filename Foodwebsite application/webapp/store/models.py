
from django.db import models
import datetime
import os
# Create your models here.

def static(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now.strftime("%y %m %d %h: %M: %s")
    filename = "%s %s" % (nowTime.original_filename)
    return os.path.join('images/', filename)



class Hotel(models.Model):
    slug = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=False, null=False)
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0-Default, 1-Hidden")
    Trending = models.BooleanField(default=False, help_text="0-Default, 1-Trending")
    location = models.CharField(max_length=100)
    hotel_id = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name



class MenuItem(models.Model):
    category = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    MenuItem_image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0-Default, 1-Hidden")
    Trending = models.BooleanField(default=False, help_text="0-Default, 1-Trending")
    Tag = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name


def __str__(self):
    return f'order: {self.created_on.strftime("%b %d %I: %M %p")}'

