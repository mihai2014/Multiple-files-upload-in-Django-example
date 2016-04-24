# Multiple-files-upload-in-Django-example
Django example module with a photo gallery and input file with multiple selections.

1) Add to INSTALLED_APPS in settings.py module 'upload'

2) Run python manage.py migrate

3) Add in urls.py:

    from upload import views as upload
  
    ...
    
    url(r'^upload/$', upload.index),
    url(r'^upload/send/$', upload.send),
    url(r'^upload/list/$', upload.list),

4)Access: 127.0.0.1:8000/upload/
