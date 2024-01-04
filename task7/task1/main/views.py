from django.shortcuts import render
from django.http import HttpResponse,HttpRequest



def index(request):
    data = HttpRequest.META
    return render(request,'index.html',{'data':data})
    # ad = ''
    # melumat =''
    # if request.method == "POST":
    #     ad = request.POST['name']
    # if ad=="Aslan":
    #     melumat = 'Aslan emi ogludur'
    # elif ad == "Imran":
    #     melumat = 'Imran dayi ogludur'
    # elif ad=='Afaq':
    #     melumat = 'Afaq bibi qizidir'
    # elif ad=='Uzeyir':
    #     melumat = 'Uzeyir xala ogludur'
    # elif ad =='Shahin':
    #     melumat ='Shahin yaxin dostdur'
    # elif ad!='':
    #     melumat = ad +" kimdir? Men onu tanimadim"

    # content = {
    #     'melumat': melumat
    # }
    # return render(request,'index.html',{'content':content})

# Create your views here.
