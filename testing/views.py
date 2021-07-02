from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from testing.models import Questions


def index(request):
    return render(request, "testing.html")

def tester(request):
    question =Questions.objects.all()
    return render(request, "testingQ.html", {"questions": question})