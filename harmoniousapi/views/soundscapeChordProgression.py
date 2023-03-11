# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from harmoniousapi.models import SoundscapeChordProgression, Soundscape, ChordProgression

class SoundscapeChordProgressionView(ViewSet):

    def retrieve(self, request, pk):

        try:
            soundscapeChordProgression = SoundscapeChordProgression.objects.get(pk=pk)
            serializer = SoundscapeChordProgressionserializer(soundscapeChordProgression)
            return Response(serializer.data)
        except SoundscapeChordProgression.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        soundscapeChordProgressions = SoundscapeChordProgression.objects.all()
        pk_query = request.query_params.get('pk', None)
        print(pk_query)
        if pk_query is not None:
            soundscapeChordProgressions = soundscapeChordProgressions.filter(soundscape=pk_query)
        
        detail_query = request.query_params.get('detail', None)
        serializer = SoundscapeChordProgressionserializer(soundscapeChordProgressions, many=True)
        if detail_query is not None:
            serializer = SoundscapeChordProgressionserializer2(soundscapeChordProgressions, many=True)
        return Response(serializer.data)

    def create(self, request):

        soundscapeChordProgression = SoundscapeChordProgression.objects.create(
            soundscape=Soundscape.objects.get(pk=request.data["soundscape"]),
            chordProgression=ChordProgression.objects.get(pk=request.data["chordProgression"]),
        )
        serializer = SoundscapeChordProgressionserializer(soundscapeChordProgression)
        return Response(serializer.data)

    def update(self, request, pk):

        soundscapeChordProgression = SoundscapeChordProgression.objects.get(pk=pk)
        soundscapeChordProgression.title=request.data["title"],
        soundscapeChordProgression.chordTexture=request.data["chordTexture"],
        soundscapeChordProgression.melodyNotes=request.data["melodyNotes"],
        soundscapeChordProgression.melodyTexture=request.data["melodyTexture"],
        # need to add if statement checking for permission to update
        soundscapeChordProgression.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        soundscapeChordProgression = SoundscapeChordProgression.objects.get(pk=pk)
        soundscapeChordProgression.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class SoundscapeChordProgressionserializer(serializers.ModelSerializer):
    class Meta:
        model = SoundscapeChordProgression
        fields = ('id', 'soundscape', 'chordProgression')
        depth = 0

class SoundscapeChordProgressionserializer2(serializers.ModelSerializer):
    class Meta:
        model = SoundscapeChordProgression
        fields = ('id','chordProgression')
        depth = 2
