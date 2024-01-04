from django.shortcuts import render,redirect
from .models import *
from .forms import TestForm, videoForm
from django.views.generic import DetailView
from django.db.models import Q
from django.core.files.storage import FileSystemStorage


# class Detail(DetailView):
#     template_name = "detail.html"
#     model = Table
#     context_object_name = "detail"
def order(request):
    data = Order.objects.all()
    return render(request,'order.html',{'data':data})
def erp(request):
    data = ERP.objects.all()
    return render(request,'erp.html',{'data':data})


def detail(request,id):
    fulldata = Table.objects.all() 
    data = Table.objects.filter(id=id)
    return render(request,'detail.html',{'data':data,'fulldata':fulldata})


def index(request):
    data = Table.objects.all()
    say = Table.objects.all().count()
    form = TestForm()
    return render(request,'index.html',{"data":data,"say":say,'form':form})

def post(request):
    data = Image.objects.all()
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
       
def postImg(request):
    data = Image.objects.all()
    if request.method == "POST":
        foto = request.FILES['imgfile']
        fs = FileSystemStorage()
        filename = fs.save(foto.name,foto)
        file = fs.url(filename)
       
        Image(img = filename).save()
        
        # img = request.FILES['imgfile']
        # Image(img = img).save()
        # request.FILES['imgfile'] = ''
        # data1 = request.POST["name"]
        # data2 = request.POST["surname"]
        # data = Table(name = data1, surname = data2)
        # data.save()
       
    return render(request,"image.html",{'data':data})


# def video(request):
#     data = Video.objects.all()
#     if request.method == "POST":
#         form = videoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = videoForm()   
#     return render(request,'video.html',{'data':data,'form':form})
def delete(request,id):
    data = Table.objects.get(id=id)
    data.delete()
    return redirect('index')

def delete_checkbox(request):
    for x in request.POST.getlist("x"):
        Table.objects.get(id=x).delete()   
    return redirect('index')

def edit(request,id):
    data = Table.objects.all()
    edit = Table.objects.get(id=id)
    form = TestForm()
    return render(request,'index.html',{'edit':edit,'data':data,'form':form})


def confirm(request,id):
    confirm = Table.objects.get(id=id)
    data = Table.objects.all().order_by("-id")

    return render(request,'index.html',{"confirm":confirm,"data":data})


def update(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST["surname"]
        data = Table.objects.get(id=id)
        data.name = name
        data.surname = surname
        data.save()


    return redirect("index")

def search(request):
    axtar = ''    
    if request.method == 'POST':
        search = request.POST['search']
        axtar = Table.objects.filter(Q(name__contains = search) | Q(surname__contains = 'R'))
    lenn = len(axtar)

    return render(request,'index.html',{'axtar':axtar,'len':lenn})
def image(request):
    data = Image.objects.all()

    return render(request,'image.html',{'data':data})

# Create your views here.


