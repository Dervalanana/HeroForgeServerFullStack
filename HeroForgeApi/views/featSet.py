"""View module for handling requests about feat types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from HeroForgeApi.models import Feat, FeatSet, FeatOption
from HeroForgeApi.models.character import Character


class FeatSetView(ViewSet):
    """Level up featset types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single featset

        Returns:
            Response -- JSON serialized featset
        """
        try:
            featset = FeatSet.objects.get(pk=pk)
            serializer = FeatSetSerializer(featset)
            return Response(serializer.data)
        except FeatSet.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all featsets

        Returns:
            Response -- JSON serialized list of featsets
        """
        featsets = FeatSet.objects.all()
        serializer = FeatSetSerializer(featsets, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized featset instance
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            featset = FeatSet.objects.create(
                name=request.data['name'],
                )
            serializer = FeatSetSerializer(featset)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            featset = FeatSet.objects.get(pk=pk)
            featset.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            featset = FeatSet.objects.get(pk=pk)
            featset.name = request.data['name']
            featset.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
        
    @action(methods=['POST'], detail=True)
    def expandSet(self, request, pk):
        """lets a character learn a feat"""
        if (request.auth.user.is_staff):
            FeatOption.objects.create(
                feat = Feat.objects.get(pk=request.data["feat"]),
                featSet = FeatSet.objects.get(pk=pk)
            )
            featSet = FeatSet.objects.get(pk=pk)
            serializer = FeatSetSerializer(featSet)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"}, status=403)
    
    @action(methods=['DELETE'], detail=True)
    def reduceSet(self, request, pk):
        """lets a character learn a feat"""
        if (request.auth.user.is_staff):
            featOption = FeatOption.objects.get(
                feat = Feat.objects.get(pk=request.data["feat"]),
                featSet = FeatSet.objects.get(pk=pk)
            )
            featOption.delete()
            featSet = FeatSet.objects.get(pk=pk)
            serializer = FeatSetSerializer(featSet)
            return Response(serializer.data, status=204)
        else:
            return Response({'message': "how did you find this"}, status=403)



class FeatSetSerializer(serializers.ModelSerializer):
    """JSON serializer for featsets
    """
    class Meta:
        model = FeatSet
        fields = ('id', 'name', 'featOptions')
        depth = 1