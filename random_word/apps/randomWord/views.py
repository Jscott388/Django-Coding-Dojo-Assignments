from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    return render(request,'randomworld/index.html')

def word(request):
    if request.method == 'POST':
        request.session['word'] = get_random_string(length=14)
        request.session['counter'] += 1
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    request.session['counter'] = 1
    return redirect('/')
