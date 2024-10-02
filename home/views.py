from django.shortcuts import render
from .models import Category
from .models import Gallery
from .models import Event
from .models import Stuff
from .models import Contact
# Create your views here.
def home_index(request):
    gallery = Gallery.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True).order_by('sort')
    events = Event.objects.filter(is_visible=True).order_by('sort')
    stuffs = Stuff.objects.filter(is_visible=True).order_by('sort')
    contacts = Contact.objects.filter(is_visible=True).order_by('sort')
    for index, stuff in enumerate(stuffs):
        stuff.aos_delay = index * 100
    context = {
        "stuffs": stuffs,
        "categories": categories,
        "gallery" : gallery,
        "events": events,
        "contacts": contacts
    }
    return render(request, "index.html", context)