# Django-Coding-Dojo-Assignments

### Setup Project

(py2DjangoEnv)>django-admin startproject PROJECTNAME

(py2DjangoEnv)>cd PROJECTNAME

(py2DjangoEnv)>mkdir apps

(py2DjangoEnv)>cd apps

(py2DjangoEnv)>nul> __init_.py OR touch __init__.py

(py2DjangoEnv)>python ../manage.py startapp APPNAME

> python manage.py runserver

###Key Terms
* request.POST
  * Data from POST request
* request.GET
  * Data from GET request
* request.method
  * Returns the method/HTTP verb associated with the request
* {% csrf_token %}
  * Prevents cross-site request forgery (place it in a form on the HTML/template side of your project)
  
### Sessions
> python manage.py makemigrations

> python manage.py migrate

request.session - It's a dictionary, so you can attach key/value pairs

###Useful session methods:
* request.session['key']
  * This will retrieve (get) the value stored in key
* request.session['key'] = 'value'
  * Set the value that will be stored by key
* del request.session['key']
  * Deletes a session key if it exists, throws a keyError if it doesn’t. Use along with try and except since it’s better to ask for forgiveness than permission
* 'key' in request.session
  * Returns a boolean of whether a key is in session or not
* {{ request.session.name }}
  * Use dot notation (.) to access request.session keys from templates since square brackets ([]) aren’t allowed there

