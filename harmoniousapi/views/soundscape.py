# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from harmoniousapi.models import Soundscape, MelodyTexture, User

class SoundscapeView(ViewSet):

    def retrieve(self, request, pk):

        try:
            soundscape = Soundscape.objects.get(pk=pk)
            serializer = Soundscapeserializer(soundscape)
            return Response(serializer.data)
        except Soundscape.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        soundscapes = Soundscape.objects.all()
        uid_query = request.query_params.get('uid', None)
        print(uid_query)
        if uid_query is not None:
            soundscapes = soundscapes.filter(user__uid__contains=uid_query)
        serializer = Soundscapeserializer(soundscapes, many=True)
        return Response(serializer.data)

    def create(self, request):

        soundscape = Soundscape.objects.create(
            user=User.objects.get(uid=request.data["user"]),
            title=request.data["title"],
            chordTexture=request.data["chordTexture"],
            melodyNotes=request.data["melodyNotes"],
            melodyTexture=MelodyTexture.objects.get(pk=request.data["melodyTexture"]),
        )
        serializer = Soundscapeserializer(soundscape)
        return Response(serializer.data)

    def update(self, request, pk):

        soundscape = Soundscape.objects.get(pk=pk)
        soundscape.title = request.data["title"]
        soundscape.chordTexture = request.data["chordTexture"]
        soundscape.melodyNotes = request.data["melodyNotes"]
        soundscape.melodyTexture = MelodyTexture.objects.get(pk=request.data["melodyTexture"])
        # need to add if statement checking for permission to update?
        soundscape.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        soundscape = Soundscape.objects.get(pk=pk)
        soundscape.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class Soundscapeserializer(serializers.ModelSerializer):
    class Meta:
        model = Soundscape
        fields = ('id', 'user', 'title', 'chordTexture', 'melodyNotes', 'melodyTexture')
        depth = 0
