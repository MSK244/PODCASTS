from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Menu(request):
    data={'text':["Hi"]*50}
    return render(request, 'Home_menu.html', data)