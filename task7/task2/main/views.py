from django.shortcuts import render

def index(request):
 
        

    content = {
        'melumat': melumat
    }
    return render(request,'index.html',{'content':content})

# Create your views here.
