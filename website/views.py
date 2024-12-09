from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddFilmLogForm
from .models import FilmLog

def home(request):
	filmlogs = FilmLog.objects.all()

	# Check to see if logging in

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in, movie geek! May the force be with you.")
			return redirect('home')
		else: 
			messages.success(request, "There was an error logging in. Please try again, movie geek!")
			return redirect('home')
	else:
		return render(request, 'home.html', {'filmlogs':filmlogs})


def logout_user(request):
	logout(request)
	messages.success(request, "Hasta la vista, movie geek!")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "To infinity and beyond! Welcome, movie geek!")
			return redirect('home')

	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def movie_log(request, pk):
	if request.user.is_authenticated:
		# Look Up FilmLogs
		movie_log = FilmLog.objects.get(id=pk)
		return render(request, 'movielog.html', {'movie_log':movie_log})
	else:
		messages.success(request, "Hold up, movie geek! You Must Be Logged In To View That Page.")
		return redirect('home') 

def delete_filmlog(request, pk):
	if request.user.is_authenticated:
		delete_it = FilmLog.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Wingardium Leviosa! FilmLog Deleted")
		return redirect('home')
	else:
		messages.success(request, "Log in first, movie geek!")
		return redirect('home')

def add_filmlog(request):
	form = AddFilmLogForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_filmlog = form.save()
				messages.success(request, "FilmLog Added!")
				return redirect('home')
		return render(request, 'add_filmlog.html', {'form':form})
	else:
		messages.success(request, "Log in first, movie geek!")
		return redirect('home')

def add_filmlog(request):
	form = AddFilmLogForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_filmlog = form.save()
				messages.success(request, "It's alive! It's alive! FilmLog Added.")
				return redirect('home')
		return render(request, 'add_filmlog.html', {'form':form})
	else:
		messages.success(request, "Log in first, movie geek!")
		return redirect('home')

def update_filmlog(request, pk):
	if request.user.is_authenticated:
		movie_log = FilmLog.objects.get(id=pk)
		form = AddFilmLogForm(request.POST or None, instance=movie_log)
		if form.is_valid():
			form.save()
			messages.success(request, "My precious, FilmLog Updated!")
			return redirect('home')
		return render(request, 'update_filmlog.html', {'form':form})
	else:
		messages.success(request, "Log in first, movie geek!")
		return redirect('home')


def search_venues(request):
	if request.method == "POST":
		searched = request.POST.get('searched', '').strip()
		venues = FilmLog.objects.filter(film_title__icontains=searched)

		return render(request, 'events/search_venues.html', {'searched':searched, 'venues':venues})
	else:
		return render(request, 'events/search_venues.html', {})