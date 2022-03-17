"""View module for handling requests about race types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HeroForgeApi.models import Race


class RaceView(ViewSet):
    """Level up race types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single race
        
        Returns:
            Response -- JSON serialized race
        """
        try:
            race = Race.objects.get(pk=pk)
            serializer = RaceSerializer(race)
            return Response(serializer.data)
        except Race.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all races

        Returns:
            Response -- JSON serialized list of races
        """
        races = Race.objects.all()
        serializer = RaceSerializer(races, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized race instance
        """
        if request.auth.user.is_staff: #only admins can C-UD
            race = Race.objects.create(
                name=request.data['name'],
                racialBonus=request.data['racialBonus'],
                special=request.data['special'],
                altSpeedType=request.data['altSpeedType'],
                altSpeed=request.data['altSpeed'],
                feat=request.data['feat'],
                featSet=request.data['featSet'],
                speed = request.data['speed']
            )
            serializer = RaceSerializer(race)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"},status=403)
        
    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff
        
        Returns
            Response --- 204 no content
        """
        if request.auth.user.is_staff: #only admins can C-UD
            race = Race.objects.get(pk=pk)
            race.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
        
    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        if request.auth.user.is_staff: #only admins can C-UD
            race = Race.objects.get(pk=pk)
            race.name=request.data['name']
            race.racialBonus=request.data['racialBonus']
            race.special=request.data['special']
            race.altSpeedType=request.data['altSpeedType']
            race.altSpeed=request.data['altSpeed']
            race.special=request.data['special']
            race.feat=request.data['feat']
            race.featSet=request.data['featSet']
            race.speed = request.data['speed']
            race.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)

    
    
class RaceSerializer(serializers.ModelSerializer):
    """JSON serializer for races
    """
    class Meta:
        model = Race
        fields = ('id', 'name', 'racialBonus','racialPenalty','special','altSpeedType',
                    'altSpeed','special','feat','featSet','speed')