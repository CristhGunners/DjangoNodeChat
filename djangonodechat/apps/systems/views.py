from django.shortcuts import render,redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangonodechat.apps.comments.models import Comment
from djangonodechat.apps.comments.forms import Form_Add_Comment

from datetime import datetime,date,time

class Login(TemplateView):
	template_name = "systems/login.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('systems:home')
		return super(Login, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(Login, self).get_context_data(**kwargs)
		return context

class Home(TemplateView):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(Home, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		today_min = datetime.combine(date.today(), time.min)
		today_max = datetime.combine(date.today(), time.max)
		comments = Comment.objects.filter(creation__range=(today_min, today_max)).order_by('-creation')
		data = {
			'form':Form_Add_Comment,
			'comments':comments,
		}
		return render(request,'systems/home.html',data)

	def post(self, request, *args, **kwargs):
		Comment.objects.create(
			user=request.user,
			text = request.POST['text']
		)
		return redirect('systems:home')