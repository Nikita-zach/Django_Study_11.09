from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='events/')
    text = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Stuff(models.Model):
    name = models.CharField(max_length=50, unique=True)
    profession = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='stuffs/')
    text = models.TextField()

    sort = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class StuffList(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    stuffs = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Gallery(models.Model):
    photo = models.ImageField(upload_to='galleries/')

    sort = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.photo.name

class ContactInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    info = models.TextField()
    icon = models.ImageField(upload_to='contacts/')

    sort = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name