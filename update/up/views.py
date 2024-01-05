from django.shortcuts import render
from .models import *

def index(request):
    data = Table.objects.all()

    return render(request,'index.html',{'data':data})

def edit(request,id):
    data = Table.objects.all()
    edit = Table.objects.get(id=id)

    return render(request,'index.html',{'edit':edit,'data':data})

# Create your views here.
