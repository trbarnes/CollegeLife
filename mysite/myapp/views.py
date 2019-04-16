from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from . import models
from . import forms


@login_required(redirect_field_name='/', login_url="/login/")
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
        "body":"College Life",
        "title":"CollegeLife",
        "item_list":i_list,
        "form":form_instance,
    }
    return render(request,"page.html", context=context)


@login_required(redirect_field_name='/', login_url="/login/")
def suggestions_json(request):
    i_list = models.Suggestion.objects.all()
    resp_list = {}
    resp_list["suggestions"] = []
    for item in i_list:
        resp_list["suggestions"] += [{"suggestion":item.suggestion_field}]
    return JsonResponse(resp_list)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)
