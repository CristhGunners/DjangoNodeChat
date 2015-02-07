from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from djangonodechat.apps.users.models import User

from .models import Comment

@csrf_exempt
def Add_Comment(request):
	user = User.objects.get(username=request.POST['user'])
	comment = Comment()
	comment.user = user
	comment.text = request.POST['text']
	comment.save()
	response = JsonResponse({
		'user': comment.user.full_name(),
		'avatar': comment.user.avatar,
		'date': comment.time(),
		'comment': comment.text,
	})
	return HttpResponse(response.content)

