from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from tasks.models import Collection, Tasks


def index(request):
    collection = Collection.get_default_collection()
    context = {'collections': Collection.objects.order_by('name')}
    return render(request, "tasks/index.html", context)


def add_collection(request):
    collection_name = escape(request.POST.get('collection-name'))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("Collection already exists", status=409)
    return HttpResponse(f'<h2>{collection_name}</h2>')


def add_task(request):
    collection = Collection.objects.get(slug=Collection.default_name)
    description = request.POST.get("task-description")
    Tasks.objects.create(description=description, collection=collection)
    return HttpResponse(description)