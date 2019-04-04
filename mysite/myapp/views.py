from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    context = {
        "body":"CINS465 Hello World",
        "title":"Hello",
    }
    return render(request,"base.html", context=context)
