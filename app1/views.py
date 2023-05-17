import email
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app1.models import *
import datetime
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

from django.views.decorators.csrf import ensure_csrf_cookie

from testing import denoise_image
def homepage(request):
    return render(request, 'Detection.html', {})





@ensure_csrf_cookie
def upload_files(request):
    global keywordslist
    print("yes")
    if request.method == "GET":
        return render(request, 'summarize.html', )
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        varimgnm=request.POST.get('varimgnm')
        print("imagename-->",varimgnm)
        
        data={}
       
        for f in files:
            handle_uploaded_file(f)
        
        denoise_image("testimage.jpg",varimgnm)
       
           
        data['msg']="yes"
        print (data)
        return JsonResponse(data,safe=False)
    else:
        return JsonResponse(data,safe=False)

def handle_uploaded_file(f):
    with open("testimage.jpg", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def Image_editor(request):
    return render(request, 'edit_image.html', {})
