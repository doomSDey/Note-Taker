# Note-Taker

My first Django project. A simple note taking app.

My Python environment dependencies:

asgiref==3.2.6

certifi==2019.11.28

Django==3.0.4

pytz==2019.3

sqlparse==0.3.1

wincertstore==0.2


We installed Django, now we can use Django to build all the starting files we
need for our web app. In your command line (again, in your project folder with
your environment activated):

```
$ django-admin.py startproject mysite
```

This is going to start a Django project in your currect directory.

* django-admin.py: The script we'll be running.
* startproject: The specific utility we're using.
* mysite: The name we're giving the project.
* . : The location where we're starting the project, with `.` denoting the
  current directory.

`startproject` will create these files and folders:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

The mysite folder is our top level folder.

* `manage.py`: We won't edit this file, but will use this file in the command line
  to interact with your project. 
* The inner `mysite` folder holds your project.
* `__init__.py`: Ignorable - tells Python that this is a Python package.
* `settings.py`: Aptly named - contains your settings.
* `urls.py`: URL declarations for the project. Important and we'll go over this
  soon.
* `wsgi.py`: Not needed at this point until you deploy your project.

### Create a Django app

A project can run many apps (all doing something distinct), but we're just going
to focus on having one for now.

In your top level folder (the one with *manage.py* in it), run this command:

```
$ django-admin.py startapp notes
```

Like before, `django-admin.py` is the script, `startapp` is the command, and
`notes` is the name we're giving the app, which you can change if you wish.

`startapp` will create an additional folder and a few files:

```
mysite/
    manage.py
    notes/
        __init__.py
        admin.py
        migrations/
        models.py
        tests.py
        views.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Note the additional "notes" folder in your project.

* `__init__.py`: Ignorable.
* `admin.py`: Contains admin codebits.
* `models.py`: Where you'll define the dynamic data that'll go in your database.
* `tests.py`: Tests you'll create to run to test your app automatically.
* `views.py`: Where the logic goes that powers your website.


### Add your new app to your settings file

We need to tell the project that we've added an app to it.  Open up your
`settings.py` file (which is under your `notes` folder, see the directory
tree above).

Find the `INSTALLED_APPS` and add the name of your app to the beginning of the list
(don't forget the trailing comma):

``` python
INSTALLED_APPS = (
    'notes', # this is the app we added
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
```

## Set up your database

We need to run the initial
migration before we start the app, so in your top level folder (the one with
*manage.py* in it), type this in:

```
$ python manage.py migrate
```

It's going to create your database automatically for you and port over some
information. 

## Start your Django web app
in notes folder (make sure you're in the folder with *manage.py*) and run
this command:

```
$ python manage.py runserver
```

...and you'll see the local Django development server starting, which'll serve
your project to your computer.

```
Validating models...

0 errors found
March 26, 2014 - 15:50:53
Django version 1.7.8, using s. http://127.0.0.1:8000/admin, Notes will appear on the page:ttings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now just head to your favorite web browser and visit
[http://127.0.0.1:8000](http://127.0.0.1:8000), where you'll see a "Welcome to
Django" page. Congrats on starting Django!

Now to deploy this project on your local server, just download the entire repo and paste it in your root directory (where the manage.py is present) and run the following commands:

```
$ python manage.py makemigrations notes
$ python manage.py migrate
$ python manage.py runserver
```
You can view the database using the link. http://127.0.0.1:8000/admin, Notes will appear on the page.

To login you need to first create a super user using the following command:
python manage.py createsuperuser

Known bugs:
  Can't handle delete of notes if the title of the deleted note has a duplicate. It can be resolved by using a unique for each note and using that as reference for deleting.
