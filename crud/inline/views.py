from django.shortcuts import render,redirect 
from .models import * 


def index(request):
    data = Test.objects.all()
    context = {
        'data': data
    }
    return render(request,'index.html',{"context":context})


def post(request):
    if request.method == "POST":
        data1 = request.POST["ad"]
        data2 = request.POST["soyad"]
        data = Test(ad = data1, soyad = data2)
        data.save()

    return redirect('index')

def delete(request,id):
    data = Test.objects.get(id=id)

    data.delete()
    return redirect("index")


# Create your views here.
