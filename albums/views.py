from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Album


# Create your views here.


def index(request):
    list = Album.objects.all
    context = {'albums': list}

    return render(request, 'albums/index.html', context)


# api handerlers
def albums(request):
    if request.method == "GET":
        return read(request)
    if request.method == "POST":
        return create(request)


def album(request):
    if request.method == "GET":
        return read_one(request)
    if request.method == "PATCH":
        return update(request)
    if request.method == "DELETE":
        return delete(request)


# crud time


def create(request):
    return HttpResponse('create')


def read():
    return HttpResponse('READ')


def update(request):

    return HttpResponse('UPDATE')


def delete(request):

    return HttpResponse('DELETE')
