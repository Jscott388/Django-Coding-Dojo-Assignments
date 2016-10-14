from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render (request, 'surveyform/index.html')

def process(request):
    if request.method == 'POST':
        print (request.POST)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        return redirect ('/results')
    else:
        return redirect('/')

def results(request):
    return render (request, 'surveyform/results.html')
