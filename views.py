from django.shortcuts import render, redirect, HttpResponseRedirect
from Dairy.models import Member #models.py
from .forms import mytext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
 
# Create your views here.
def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
 
def login(request):
	# if request.method == 'POST':
	# 			if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
	# 				member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])

	# 				return render(request, 'form.html', {'member': member})
	# 			else:
	# 				context = {'msg': 'Invalid username or password'}
	# 				return render(request, 'login.html', context)  
    return render(request, 'login.html')
 
# def home(request):
# 			if request.method == 'POST':
# 				if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
# 					member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])

# 					return render(request, 'form.html', {'member': member})
# 			else:
# 				context = {'msg': 'Invalid username or password'}
# 				return render(request, 'login.html', context)  

def user_logout(request):

	if request.method == "POST":

		logout(request)
		return redirect('/')

	# return HttpResponseRedirect(reverse('login'))
	# response = redirect('login.html')
	# return response
	# return redirect('/')
	# return render(request, 'login.html', {})


# Create your views here.
def myform(request):
    # form = textForm()
	# if request.method == "POST":
	# 	if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
	# 		member = Member.objects.filter(username=request.POST['username'], password=request.POST['password'])
	# 		return render(request, 'form.html', {'member': member})
	# else:
	# 	context = {'msg': 'Invalid username or password'}
	# 	return render(request, 'login.html', context)
		form = mytext(request.POST or None)
		if form.is_valid():
			form.save()
			form = mytext()
		context = {
			'form': form
		}
		return render(request, 'form.html', context)
