from django.shortcuts import render, redirect
from django.contrib.auth import logout

def Logout(request):
	logout(request)
	return redirect('/')