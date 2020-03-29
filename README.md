# Note-Taker

My first Django project. A simple note taking app.

My Python environment dependencies:

asgiref==3.2.6

certifi==2019.11.28

Django==3.0.4

pytz==2019.3

sqlparse==0.3.1

wincertstore==0.2

Known bugs:
  Can't handle delete of notes if the title of the deleted note has a duplicate. It can be resolved by using a unique for each note and using that as reference for deleting.
