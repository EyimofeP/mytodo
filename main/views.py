from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect

from main.models import Todo


# Returns todo items from database to home page
def home(request):
	lists = Todo.objects.order_by("-added_date")
	frontend_stuff = {
		"lists": lists
	}

	return render(request,"main/index.html",frontend_stuff)

#Form to adds todo items to database
@csrf_exempt
def addTo(request):
	currentdate = timezone.now()
	content = request.POST["content"]
	userid = request.user
	created_content = Todo.objects.create(added_date = currentdate, text = content)
	return HttpResponseRedirect("/")

#Form to delete todo items from database
@csrf_exempt
def deleteTo(request, todo_id):
	Todo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect("/")

def connect(request):
	return render(request,"main/connect.html")

