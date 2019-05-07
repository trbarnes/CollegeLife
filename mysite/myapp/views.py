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
            new_sugg.suggestion_author = request.user
            new_sugg.save()
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    #initial page load
    if request.method == "GET":
        print("GET")
    i_list = models.Suggestion.objects.all()
    context = {
        "title":"CollegeLife",
        "item_list":i_list,
        "form":form_instance,
        "comm_formm":forms.CommentForm()
    }
    return render(request,"page.html", context=context)


@login_required(redirect_field_name='/', login_url="/login/")
def suggestions_json(request):
    i_list = models.Suggestion.objects.all()
    resp_list = {}
    resp_list["suggestions"] = []
    for item in i_list:
        comments_list = []
        comm_list = models.Comment.objects.filter(comment_suggestion=item)
        for comm in comm_list:
            comments_list += [{
                "comment":comm.comment_field,
                "author":comm.comment_author.username,
                "id":comm.id,
                "created_on":comm.created_on
            }]
        resp_list["suggestions"] += [{
            "suggestion":item.suggestion_field,
            "author":item.suggestion_author.username,
            "id":item.id,
            "comments":comments_list,
            "created_on":item.created_on,
            "num_comments":len(comments_list)
        }]
    return JsonResponse(resp_list)

def logout_view(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url="/login/")
def page_view(request, page):
    i_list = []
    p_range = page*10
    for i in range(20*(page+1)):
        i_list += ["Item "+str(i)]
    context = {
        "body":"",
        "title":"",
        "item_list":i_list[p_range:p_range+10],
        "page":page,
        "next":page+1
    }
    return render(request, "page.html", context=context)

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

@login_required(login_url="/login/")
def comment_view(request, sugg):
    if request.method == "POST":
        form_instance = forms.CommentForm(request.POST)
        if form_instance.is_valid():
            sugg_instance = models.Suggestion.objects.get(id=sugg)
            new_comm = models.Comment()
            new_comm.comment_field = form_instance.cleaned_data["comment_field"]
            new_comm.comment_suggestion = sugg_instance
            new_comm.comment_author = request.user
            new_comm.save()
            return redirect("/")
    else:
        form_instance = forms.CommentForm()
    if request.method == "GET":
        print("GET")
    j_list = models.Comment.objects.all()
    context = {
        "title":"Comments",
        "item_list":j_list,
        "form":form_instance,
        "suggestion":sugg
    }
    return render(request, "comment.html", context=context)
