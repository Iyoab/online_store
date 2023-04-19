from django.shortcuts import render
from item.models import Category,Item


def index(request):
    items=Item.objects.filter(availablity=True)[0:6]
    categories = Category.objects.all()

    return render(request, 'foundation/index.html', {
        'categories': categories,
        'items': items
    })


def contact(request):
    return render(request, 'foundation/contact.html')
