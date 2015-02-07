from django import forms
from django.forms import ModelForm
from .models import Comment

class Form_Add_Comment(ModelForm):
	
	class Meta:
		model = Comment
		exclude = ('user',)