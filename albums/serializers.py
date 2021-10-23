from rest_framework import serializers

from albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Album

 # the fields to include in serialization
        fields = "__all__"
