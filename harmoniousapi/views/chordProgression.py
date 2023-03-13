from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from harmoniousapi.models import ChordProgression

class ChordProgressionView(ViewSet):

    def retrieve(self, request, pk):

        try:
            chordProgression = ChordProgression.objects.get(pk=pk)
            serializer = ChordProgressionserializer(chordProgression)
            return Response(serializer.data)
        except ChordProgression.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        chordProgressions = ChordProgression.objects.all()
        serializer = ChordProgressionserializer(chordProgressions, many=True)
        return Response(serializer.data)

class ChordProgressionserializer(serializers.ModelSerializer):
    class Meta:
        model = ChordProgression
        fields = ('name', 'firstChord', 'secondChord', 'thirdChord', 'fourthChord')
        depth = 0
