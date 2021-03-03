from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task= forms.CharField(label = "New Task")


def index(request):
    if "task" not in request.session:
        request.session['task']= []
    return render(request, 'task/index.html' ,{
        'task':request.session['task']
    })


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            item=form.cleaned_data['task']
            request.session['task'] += [item]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'task/add.html',{
            'form':form
            })
    return render(request, 'task/add.html',{
        "form" : NewTaskForm()
    })
