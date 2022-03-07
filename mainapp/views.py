from django.shortcuts import redirect, render
from django.contrib import messages
from mainapp.models import *
# Create your views here.

def index(request):
    item_list = Item.objects.all() 
    context = {
        'item_list': item_list
    }
    return render(request, "mainapp/index.html", context)

def add_item(request):
    if request.method =="POST":
        name = request.POST['name']
        description = request.POST['description']
        item = Item(name = name, description= description)
        item.save()
        messages.info(request , "Item added")
    else:
        pass

    item_list = Item.objects.all() 
    context = {
        'item_list': item_list
    }
    return render(request, "mainapp/index.html", context)

def delete_item(request, myid):
    item = Item.objects.get(id=myid)
    item.delete()
    messages.info(request, "item deleted ")
    return redirect('home')

def edit_item(request, myid):
    sel_item = Item.objects.get(id=myid)
    item_list = Item.objects.all() 
    context = {
        'sel_item' : sel_item,
        'item_list' : item_list

    }
    return render(request, 'mainapp/index.html',context)

def update_item(request, myid):
    item = Item.objects.get(id = myid)
    item.name = request.POST['name']
    item.description = request.POST['description']
    item.save()
    messages.info(request, "Item updated successfully")
    return redirect('home')
