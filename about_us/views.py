from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_home(request):
    return render(request,'about_index.html')
    
