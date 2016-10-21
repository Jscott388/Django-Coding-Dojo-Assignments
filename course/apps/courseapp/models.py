from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def createCourse(self, **kwargs):
            course = self.create(name=kwargs['name'], description=kwargs['description'])
            return (True, course)

	def getAll(self):
		all_courses = self.all()
		return all_courses

	def getCourse(self, args):
		result = self.get(id=args)
		return result

	def deleteCourse(self, args):
		Course.objects.filter(id=args).delete()


class CommentManager(models.Manager):
	def makeComment(self, **kwargs):
		result = Comment.objects.create(message=kwargs['comment'], course=course)
		return result

	def getComments(self, id):
		comments = Comment.objects.all()
		return comments


class Course(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = CourseManager()

class Comment(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	message = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = CommentManager()
