from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True).order_by('sort')
        for dish in dishes:
            yield dish

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.IntegerField()
    unit = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='dishes', blank=True, null=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

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

class Contact(models.Model):
    title= models.CharField(max_length=50)
    description = RichTextField()
    icon = models.ImageField(upload_to='contacts/', null=True, blank=True)

    sort = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    number_regex = RegexValidator(
        regex=r'^\+?3?8?\d{9,15}$',
        message="Phone number must be entered in the format: '+3899999999' or '999999999'. Up to 15 digits allowed."
    )

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, validators=[number_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    is_processed = models.BooleanField(default=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FooterItems(models.Model):
    item_title = models.CharField(max_length=50)
    item_description = models.TextField()
    item_icon = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_title