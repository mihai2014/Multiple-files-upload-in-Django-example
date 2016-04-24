from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import random
import sys
import json
from upload.models import File

def index(request):
    data = {'media':settings.STATIC_URL}
    #return HttpResponse('hello')
    return render(request, 'upload/upload.html', data)

def randomStr(nr):
    str = []
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    nr = 6
    for k in range(1, nr+1):
        str.append(random.choice(chars))
    str = "".join(str)
    return(str)

def writeFile(file):
    home = settings.BASE_DIR

    fileName = file.name

    try:
        file_name = File.objects.get(name=fileName)
        fileNameSplit = fileName.split(".")
        name = fileNameSplit[0]
        ext = fileNameSplit[1]
        fileName = name + "_" + randomStr(6) + "." + ext
    except:
        pass

    path = home + "/upload/static/upload/documents/" + fileName

    try:
	#write file
        destination = open(path, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

        #write database record name
        newFile = File(name = fileName)
        newFile.save()
	return "ok"
    except Exception as e:
        return e



def send(request):
    state = "No files sent"
    msg = "Files received by the server:<br><br>"

    if request.POST:
        n = request.POST['n']
    else:
        return HttpResponse("only POST request allowed")

    if request.FILES:
        for n in range(int(n)):
            keyName = "file"+str(n)
            file = request.FILES[keyName]
            fileDescription = file.name + " " + str(file.size) + " bytes " + file.content_type
            msg += keyName+ " : " + fileDescription + "<br>"
            state = writeFile(file)

    if(state != 'ok'): msg = str(state)

    return HttpResponse(msg)

def list(request):
    files = File.objects.order_by('id')
    data = []
    for item in files:
        id = str(item.id)
        name = str(item.name)
        data.append({"id":id,"name":name})
    data = json.dumps(data)
    return HttpResponse(data)
      
