from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.contrib import messages
from .models import post
from .forms import postform
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_create(request):
	
	form = postform(request.POST or None, request.FILES or None);
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request,"save!!", extra_tags='some-tag')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
def post_home(request):
	queryset_list= post.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 5)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	
	context = {
		"object_list":queryset,
		"title": "list",
		"page_request_var":page_request_var,
	}
	return render(request, "base.html", context)



def post_detail(request, id=None):
	instance = get_object_or_404(post, id=id)
	
	context={
		"title": instance.title,
		"instance": instance,
		

	}
	return render(request, "post_detail.html", context)


def post_update(request, id = None):
	instance = get_object_or_404(post, id= id)
	form = postform(request.POST or None,  request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request,"save!!", extra_tags='some-tag')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": instance.title,
			"instance": instance,
			"form": form,

		}
	return render(request, "post_form.html",context)

def post_delete(request, id=None):
	instance = get_object_or_404(post, id= id)
	instance.delete()
	messages.success(request,"save!!", extra_tags='some-tag')
	return redirect("post:home")