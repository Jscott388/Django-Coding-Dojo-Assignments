from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def createCourse(sel f, **kwargs):
        self.create(name=kwargs['name'])
        return (True)

class CommentManager(models.Manager):
    def createComment(self, **kwargs):
        course_id = Course.objects.get(id=kwargs['id'])
        comment = Comment.object.create(name=kwargs['comment'], course=course_id)
        return (True)

class DescriptionManager(models.Manager):
    def createDescription(self, **kwargs):
        course_id = Course.objects.get(id=kwargs['id'])
        description = Description.object.create(description=kwargs['description'], course=course_id)
        return (True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = CommentManager()

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = DescriptionManager()
