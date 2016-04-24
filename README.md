# Multiple-files-upload-in-Django-example
Django example module with a photo gallery and input file with multiple selections.

1) Edit settings.py to add 'upload':

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ...
    'upload',
]

2)Run python manage.py migrate

3)Edit urls.py to add:

from upload import views as upload

urlpatterns = [
    ...
    url(r'^upload/$', upload.index),
    url(r'^upload/send/$', upload.send),
    url(r'^upload/list/$', upload.list),
]    

4) Access: 127.0.0.1:8000/upload/
