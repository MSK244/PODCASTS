from django.shortcuts import render

# Create your views here.
def Episodes(request):
    return render(request,'Episodes.html',{})