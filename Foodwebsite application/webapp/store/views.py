
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import *

# Create your views here.
# main page is where all the fonts and stylesheets are stored

def store(request):
    hotel = Hotel.objects.filter(status=0)
    context = {'hotel': hotel}

    return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/check-out.html', context)

def View(request):
	context = {}
	return render(request, 'store/view.html', context)

def About(request):
	context = {}
	return render(request, 'store/about.html', context)

def Help(request):
	context = {}
	return render(request, 'store/help.html', context)

def Services(request):
	context = {}
	return render(request, 'store/services.html', context)
def Maps(request):
	context = {}
	return render(request, 'store/maps.html', context)


# class restaurant(View):
def restaurant( request):
   hotel = Hotel.objects.filter(status=0)
   context = {'hotel': hotel}

   return render(request, 'store/restaurant.html', context)


def restaurantview(request, slug):

  if(Hotel.objects.filter(slug=slug, status=0)):
        menuitem = MenuItem.objects.filter(category__slug=slug)
        hotel = Hotel.objects.filter(slug=slug).first()
        context = {'menuitem': menuitem, 'hotel': hotel}
        return render(request, 'store/menu.html', context)

  else:
        messages.warning(request, "No such category found")
        return redirect('restaurant')



def menuitemview(request, MenuItem_id, Hotel_id):

    if (Hotel.objects.filter(id=Hotel_id, status=0)):

        if (MenuItem.objects.filter(id= MenuItem_id, status=0)):
                menuitem = MenuItem.objects.filter(id=MenuItem_id, status=0).first
                context = {'menuitem': menuitem}
        else:
           messages.error(request, "No such product found")
           return redirect('restaurant')
    else:
      messages.error(request, "No such product found")
      return redirect('restaurant')

    return render(request, 'store/view.html', context)




