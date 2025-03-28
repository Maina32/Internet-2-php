from django.shortcuts import render, redirect
from .models import Obituary
from .forms import ObituaryForm

def submit_obituary(request):
    if request.method == "POST":
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html") 
    else:
        form = ObituaryForm()
    return render(request, "obituary_form.html", {"form": form})

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, "view_obituaries.html", {"obituaries": obituaries})
