from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import Course, Comment, Description

# Create your views here.
def index(request):
    return render(request, 'course/index.html')


def create(request):
    if request.method == 'POST':
        Course.objects.createCourse(name=request.POST['name'])
        # newdescription = Description.objects.createDescription(name=request.POST['description'])
        return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))


def show(reuqest, id):
    return render(request, 'course/show.html')

def edit(request, id):
    return render(request, 'course/edit.html')

def update(request, id):
    pass

def delete(request, id):
    pass
