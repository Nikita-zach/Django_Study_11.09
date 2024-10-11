from django.shortcuts import render, redirect
from .models import Category
from .models import Gallery
from .models import Event
from .models import Stuff
from .models import Contact
from .forms import ReservationForm
# Create your views here.
def home_index(request):
    if request.method == 'POST':
        book_table_form = ReservationForm(request.POST)
        if book_table_form.is_valid():
            book_table_form.save()
            return redirect(request, 'thanks.html')


    gallery = Gallery.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True).order_by('sort')
    events = Event.objects.filter(is_visible=True).order_by('sort')
    stuffs = Stuff.objects.filter(is_visible=True).order_by('sort')
    contacts = Contact.objects.filter(is_visible=True).order_by('sort')
    book_table_form = ReservationForm()
    for index, stuff in enumerate(stuffs):
        stuff.aos_delay = index * 100
    context = {
        "stuffs": stuffs,
        "categories": categories,
        "gallery" : gallery,
        "events": events,
        "contacts": contacts,
        "book_table_form": book_table_form
    }
    return render(request, "index.html", context)

def thanks(request):
    return render(request, 'thanks.html')
