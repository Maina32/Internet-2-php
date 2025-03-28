from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Obituary
from .forms import ObituaryForm

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/obituary_form.html', {'form': form})

def view_obituaries(request):
    obituaries_list = Obituary.objects.all().order_by('-submission_date')
    paginator = Paginator(obituaries_list, 10)  # Show 10 obituaries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'obituaries/obituary_list.html', {'page_obj': page_obj})