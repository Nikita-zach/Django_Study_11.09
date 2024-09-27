from django.shortcuts import render
from .models import Category


# Create your views here.
def home_index(request):

    categories = Category.objects.filter(is_visible=True).order_by('sort')
    context = {
        "categories": categories,
    }
    return render(request, "index.html", context)