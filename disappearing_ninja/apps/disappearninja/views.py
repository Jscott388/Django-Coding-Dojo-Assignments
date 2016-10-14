from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render (request, 'disappearninja/index.html')

def showall(request):
    context = {'ninjas' : 'tmnt.png'}

    return render (request, 'disappearninja/ninjas.html', context)

def ninjas(request, color):
    if color == "blue":
        link = 'leonardo.jpg'
    elif color == "orange":
        link = 'michelangelo.jpg'
    elif color == "red":
        link = 'raphael.jpg'
    elif color == "purple":
        link = 'donatello.jpg'
    else:
        link = 'notapril.jpg'

    context = {'ninjas': link}

    return render (request, 'disappearninja/ninjas.html', context)
    
