from django.shortcuts import render
from models import AlkoEntry
from django.contrib.auth.models import User
from forms import BeerPenaltyForm

def home(request):
    penalties = AlkoEntry.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        submitted_form = BeerPenaltyForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
    form = BeerPenaltyForm()
    return render(request, 'olstraff.html', {'penalties': penalties, 'users': users, 'form': form})
