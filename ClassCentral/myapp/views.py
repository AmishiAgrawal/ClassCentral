from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'www.classcentral.com/index.html')

def myfunc(request,myparameter):
    directories = myparameter
    print('-------------------------------')
    # print(myparameter)
    # html_file ='www.classcentral.com/' + myparameter
    # print(html_file)
    return render(request,'www.classcentral.com/'+ myparameter)
  