from django.shortcuts import render
#from django.http import HttpResponse

from django.http import JsonResponse
from . import models
from . import forms

def index(request):
    #Form Submission
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            print(request.POST)
            new_sugg = models.Suggestion()
            new_sugg.suggestion_field = form_instance.cleaned_data["suggestion_field"]
            new_sugg.save()
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    #initial page load
    if request.method == "GET":
        print("GET")
    i_list = models.Suggestion.objects.all()
    context = {
        "body":"CINS465 Hello World",
        "title":"Hello",
        "item_list":i_list,
        "form":form_instance,
    }
    return render(request,"page.html", context=context)

def suggestions_json(request):
    i_list = models.Suggestion.objects.all()
    resp_list = {}
    resp_list["suggestions"] = []
    for item in i_list:
        resp_list["suggestions"] += [{"suggestion":item.suggestion_field}]
    return JsonResponse(resp_list)
