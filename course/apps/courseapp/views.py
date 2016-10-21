from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Course, Comment


# Create your views here.
def index(request):
    all_courses = Course.objects.getAll()
    context = {
    'all_courses': all_courses
    }
    return render(request, 'courseapp/index.html', context)

def create (request):
    if request.method == 'POST':
        Course.objects.createCourse(name=request.POST['name'], description=request.POST['description'])
        print request.POST
        return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def show (request, id):
    course = Course.objects.get(id=id)
    comments = Comment.objects.getComments(id)
    context = {'course': course, 'comments': comments}
    return render(request, 'courseapp/show.html', context)

def edit (request, id):
    course = Course.objects.get(id=id)

    return render(request, 'courseapp/edit.html', {'course':course})

def update (request, id):
    if request.method == 'POST':
        edit = Course.objects.get(id=id)
        edit.name = request.POST['name']
        edit.description = request.POST['description']
        edit.save()

        return redirect(reverse('show', kwargs={'id':id}))
    else:
        return redirect(reverse('edit', kwargs={'id':id}))

def delete (request, id):
    Course.objects.deleteCourse(id)

    return redirect(reverse('index'))

def comment(request, id):
    if request.method == 'POST':
        course = Course.objects.get(id=id)
        Comment.objects.create(message=request.POST['comment'], course=course)
    return redirect(reverse('show', kwargs={'id':id}))
