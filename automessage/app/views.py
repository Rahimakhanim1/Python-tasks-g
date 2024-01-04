from django.shortcuts import render

def index(request):
    data = ''
    name=''
    if request.method == "POST":
        data = request.POST['messagetText']
        name = request.POST['name']
    return render(request,"index.html",{'data':data,'name':name})


def edit(request):
    data = ''
    name=''
    if request.method == "POST":
        data = request.POST['messagetText']
        name = request.POST['name']


    return render(request,"index.html",{'data':data,'name':name})


# Create your views here.
