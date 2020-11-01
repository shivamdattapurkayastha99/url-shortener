
import random
from .models import *
from django.shortcuts import render,redirect
def index(request):
    if request.method=='POST':
        link=request.POST.get('url')
        short_link=""
        alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
        url=Url.objects.all()
        for i in url:
            if i.link==link:
                short_link=i.short_link
                break
        else:
                for i in range(1,7):
                    letters=random.randint(1,len(alpha)-1)
                    let=alpha[letters]
                    short_link+=let
        
                url=Url(link=link,short_link=short_link)
                url.save()
        new_url="http://127.0.0.1:8000/"+short_link
        return render(request,'index.html',{"new_url":new_url})
    return render(request,'index.html')
def shorten(request,id):
    url=Url.objects.filter(short_link=id)
    link=""
    for i in url:
        link=i.link
    return redirect(link)


    