from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    print("*"*50)
    return render(request,'randomworld/index.html')

def word(request):
    if request.method == 'POST':
        print (request.POST)
        print ('*'*50)
    else:
        return redirect('/')
