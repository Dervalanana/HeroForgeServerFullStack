"""View module for handling requests about feat types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from HeroForgeApi.models import Feat, Classs, Skill, FeatSet, ClassLevel, ClassSkill



class ClasssView(ViewSet):
    """Level up classs types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single classs

        Returns:
            Response -- JSON serialized classs
        """
        try:
            classs = Classs.objects.get(pk=pk)
            classs.classLevels = ClassLevel.objects.filter(classs=classs)
            serializer = ClasssSerializer(classs)
            return Response(serializer.data)
        except Classs.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all classss

        Returns:
            Response -- JSON serialized list of classss
        """
        classss = Classs.objects.all()
        serializer = ClasssSerializer(classss, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized classs instance
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            classs = Classs.objects.create(
                name=request.data['name'],
                skillPoints=request.data['skillPoints'],
                HD=request.data['HD']
            )
            skills = Skill.objects.all()
            for skill in skills:
                ClassSkill.objects.create(
                    value=False,
                    classs=classs,
                    skill=skill
                )
            levelCounter = 1
            while levelCounter < 21:
                classLevel = ClassLevel.objects.create(
                    classs=classs,
                    level=levelCounter,
                    features='',
                    fixedFeat=None,
                    featSet=None,
                    BAB=1,
                    Fort=0,
                    Ref=0,
                    Will=0
                )
                if (request.data['BAB'] == 2):
                    classLevel.BAB = 0 if (((levelCounter+3) % 4) == 0) else 1
                if (request.data['BAB'] == 1):
                    classLevel.BAB = 1 if ((levelCounter % 2) == 0) else 0
                if (request.data['Fort'] == 2):
                    classLevel.Fort = 2 if (levelCounter == 1) else 1 if (
                        (levelCounter % 2) == 0) else 0
                if (request.data['Fort'] == 1):
                    classLevel.Fort = 1 if ((levelCounter % 3) == 0) else 0
                if (request.data['Ref'] == 2):
                    classLevel.Ref = 2 if (levelCounter == 1) else 1 if (
                        (levelCounter % 2) == 0) else 0
                if (request.data['Ref'] == 1):
                    classLevel.Ref = 1 if ((levelCounter % 3) == 0) else 0
                if (request.data['Will'] == 2):
                    classLevel.Will = 2 if (levelCounter == 1) else 1 if (
                        (levelCounter % 2) == 0) else 0
                if (request.data['Will'] == 1):
                    classLevel.Will = 1 if ((levelCounter % 3) == 0) else 0
                classLevel.save()
                levelCounter = levelCounter+1
            serializer = ClasssSerializer(classs)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            classs = Classs.objects.get(pk=pk)
            classs.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            classs = Classs.objects.get(pk=pk)
            levelCounter = 1
            while levelCounter < 21:
                classLevel = ClassLevel.objects.get(
                    classs=classs,
                    level=levelCounter
                )
                
                if request.data['features']: classLevel.features=request.data['features']
                if request.data['fixedFeat']: classLevel.fixedFeat=Feat.objects.get(pk = request.data['fixedFeat'])
                if request.data['featSet']: classLevel.featSet=FeatSet.objects.get(pk = request.data['featSet'])
                if (request.data['BAB'] == 3):
                    classLevel.BAB = 1
                if (request.data['BAB'] == 2):
                    classLevel.BAB = 0 if (((levelCounter+3) % 4) == 0) else 1
                if (request.data['BAB'] == 1):
                    classLevel.BAB = 1 if ((levelCounter % 2) == 0) else 0
                if (request.data['Fort'] == 2):
                    classLevel.Fort = 2 if (levelCounter == 1) else 1 if (
                        (levelCounter % 2) == 0) else 0
                if (request.data['Fort'] == 1):
                    classLevel.Fort = 1 if ((levelCounter % 3) == 0) else 0
                if (request.data['Ref'] == 2):
                    classLevel.Ref = 2 if (levelCounter == 1) else 1 if (
                        (levelCounter % 2) == 0) else 0
                if (request.data['Ref'] == 1):
                    classLevel.Ref = 1 if ((levelCounter % 3) == 0) else 0
                if (request.data['Will'] == 2):
                    classLevel.Will = 2 if (levelCounter == 1) else 1 if (
                        (levelCounter % 2) == 0) else 0
                if (request.data['Will'] == 1):
                    classLevel.Will = 1 if ((levelCounter % 3) == 0) else 0
                classLevel.save()
                levelCounter = levelCounter+1
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
    
    @action(methods=['PUT'], detail=True)
    def updateClassSkills(self, request, pk):
        """lets a character learn a feat"""
        if (request.auth.user.is_staff):
            for skill in request.data:
                classSkill = ClassSkill.objects.get(classs=pk, skill=skill)
                classSkill.value = skill.value
                classSkill.save()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)


class ClasssSerializer(serializers.ModelSerializer):
    """JSON serializer for feats
    """
    class Meta:
        model = Classs
        fields = ('id', 'name', 'skillPoints', "HD",
                  "classSkills", "levelDetails")
        depth = 1
