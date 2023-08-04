from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import actorSerializers
from .models import Actor
from rest_framework.response import Response

class ActorsList(APIView):

    def get(self, request):
        actors = Actor.objects.all()
        serialize = actorSerializers(actors, many=True)
        return Response(serialize.data)
