from django.core import exceptions
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

from albums.serializers import AlbumSerializer
from .models import Album
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import response
from rest_framework import exceptions

# Create your views here.


def index(request):
    list = Album.objects.all
    context = {'albums': list}

    return render(request, 'albums/index.html', context)


class AlbumsListView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serialized_albums = AlbumSerializer(albums, many=True)
        return Response(serialized_albums.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        # Create an album instance from the request data
        album_to_add = AlbumSerializer(data=request.data)
        if album_to_add.is_valid():
            # Save album to database
            album_to_add.save()
            return response.Response(album_to_add.data, status=status.HTTP_201_CREATED)

        return response.Response(album_to_add.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(views.APIView):
    def get_album_by_id(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            raise exceptions.NotFound(detail="Album does not exist")

    def get(self, request, id):
        album = self.get_album_by_id(id)
        serialized_album = AlbumSerializer(album)
        return response.Response(serialized_album.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        album = self.get_album_by_id(id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        album = self.get_album_by_id(id)
        updated_album = AlbumSerializer(album, data=request.data)
        if updated_album.is_valid():
            updated_album.save()
            return response.Response(
                updated_album.data, status=status.HTTP_202_ACCEPTED
            )
        return response.Response(
            updated_album.errors, status=status.HTTP_400_BAD_REQUEST
        )
