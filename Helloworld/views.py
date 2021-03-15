from django.shortcuts import render, redirect	
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.
def index(request):
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save()
			name=request.POST.get('Name')
			return redirect('welcome', name)
	else:
		form=UserForm()
	return render(request, 'index.html', {'form':form})

def Welcome(request, slug):
	
	return render (request, "personalized_welcome.html", {'name': slug})