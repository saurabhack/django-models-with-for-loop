from django.shortcuts import render
from django.http import HttpResponse
from .models import students

# Create your views here.
def index(request):
    std1=students()
    std1.name="viraj jagdale"
    std1.age=20
    std1.year="second"
    
    std2=students()
    std2.name="karan falke"
    std2.age=23
    std2.year="third"

    std3=students()
    std3.name="vidhi jagdale"
    std3.age=24
    std3.year="first"

    s=[std1,std2,std3]
    #productes=[product1,product2,product3]
    #adds=[first,first1,first2]
    return render(request,'index.html',{'s':s} )
#{'adds':adds}

def profile(request):
    text2=request.POST['text2']
    text3=request.POST['text3']
    return render(request,'profile.html' ,{'text2':text2 ,'text3':text3})


