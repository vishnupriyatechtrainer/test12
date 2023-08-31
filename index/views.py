from django.http import HttpResponse
from django.shortcuts import render
from .models import aboutnew
from .models import visitor
from .models import client
def home(request):
    aboutdatanew=aboutnew.objects.get(id=3)
    
    clientdata=client.objects.all()
    visitordata=visitor.objects.all()
    #text={'name':'vishnupriya','email':'priya@gmail.com','friends':['sam','raj','john']}
    #return HttpResponse('this is a homepage')

    context={

        'aboutnew':aboutdatanew,
      
        'client':clientdata,
         'visitor':visitordata
    }





    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def service(request):
    return HttpResponse('this is a servicepage')



def product(request):
    return HttpResponse('this is a productpage')


