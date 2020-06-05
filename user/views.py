from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# View to create user
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()#Saving User data
			username = form.cleaned_data.get('username')#Pulling Username from database
			messages.success(request, f"New Guy Has Arrrived: Welcome {username} !!🥳🥳")#Sending message
			login(request, user)#Logging in user
			messages.info(request, f"Yo Wagwan Up {username} !! 😁😁")
			return redirect("main:home")#Redirecting to homepage
		else:#for message errors
			for msg in form.error_messages:
				print(request, f"{msg}: {form.error_messages[msg]}")
	#Creating user form
	form = UserCreationForm
	#Passing database to frontend
	frontend = {
		"form" : form
	}
	return render(request,"main/register.html",frontend)

#View to Login a user
def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)#Logging in user
				messages.info(request, f"Yo Wagwan {username} !! 😁😁")
				return redirect("main:home")
			else:
				messages.error(request,"Invalid Username or Password")
		else:
			messages.error(request,"Invalid Username or Password")

	form = AuthenticationForm()
	#Passing database to frontend
	frontend = {
		"form" : form
	}
	return render(request,"main/login.html",frontend)

#View to Logout a user
def signout(request):
	#Logging out user
	logout(request)
	#Sending message to user
	messages.info(request, "See you later alligator!!")
	return redirect("main:home")#Redirecting to homepage