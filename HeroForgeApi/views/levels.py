"""View module for handling requests about level types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from HeroForgeApi.models import Level, Character, Level, CharacterFeat
from HeroForgeApi.models.classLevel import ClassLevel
from HeroForgeApi.models.classs import Classs
from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models.levelSkill import LevelSkill
from HeroForgeApi.models.skill import Skill
from HeroForgeApi.views.classes import ClassLevelSerializer, ClasssSerializer


class LevelsView(ViewSet):
    """Level up level types view"""

    def retrieve(self, request, pk):
        """Handle GET requests to get all levels

        Returns:
            Response -- JSON serialized list of levels
        """
        levels = Level.objects.filter(character=Character.objects.get(pk=pk))
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized level instance
        """
        # gets all the current levels for a character
        currentLevel = Level.objects.filter(
            character=request.data['character'])
        # add one to the length and make that the new level
        currentLevel = len(currentLevel)+1
        level = Level.objects.create(
            character=Character.objects.get(pk=request.data['character']),
            classs=Classs.objects.get(pk=1),
            characterLevel=currentLevel,
            HDRoll=0,
        )
        skills = Skill.objects.all()
        for skill in skills:
            LevelSkill.objects.create(
                skill=skill,
                level=level,
                points=0,
                multiTypeName=''
            )
        serializer = LevelSerializer(level)
        return Response(serializer.data, status=201)

    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        level = Level.objects.get(pk=pk)
        try:
            characterFeat = CharacterFeat.objects.get(
                source="classFeat", pk=pk,)
            characterFeat.delete()
        except:
            pass
        try:
            characterFeat = CharacterFeat.objects.get(
                source="fixedFeat", sourceId=pk)
            characterFeat.delete()
        except:
            pass
        try:
            characterFeat = CharacterFeat.objects.get(
                source="level", sourceId=pk)
            characterFeat.delete()
        except:
            pass
        finally:
            level.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """Handle PUT requests for a level, can only change stat increases and change to hd
        changes to feats are handled separately

        Returns:
            Response -- Empty body with 204 status code
        """
        level = Level.objects.get(pk=pk)
        print(request.data)
        if request.data['HDRoll']:
            level.HDRoll = request.data['HDRoll']
        level.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PUT'], detail=True)
    def change_class(self, request, pk):
        """lets a character change levels"""
        try:
            characterFeat = CharacterFeat.objects.get(
                source="classFeat", pk=pk,)
            characterFeat.delete()
        except:
            pass
        finally:
            try:
                characterFeat = CharacterFeat.objects.get(
                    source="fixedFeat", sourceId=pk)
                characterFeat.delete()
            except:
                pass
            finally:
                Levels = Level.objects.filter(
                    classs=request.data['classs'],
                    character=request.data['characterId'],
                )  # determines how many levels of a class a character currently has
                level = Level.objects.get(pk=pk)  # grab the current level
                # set the class to the current class
                level.classs = Classs.objects.get(pk=request.data['classs'])
                level.levelDetails = ClassLevel.objects.get(
                    classs=Classs.objects.get(pk=request.data['classs']),
                    level=len(Levels)+1
                )  # the next class level that the character doesn't have is set as the current details
                if level.levelDetails.fixedFeat:
                    CharacterFeat.objects.create(
                        feat=Feat.objects.get(level.levelDetails.fixedFeat),
                        character=Character.objects.get(
                            request.data['characterId']),
                        source="fixedFeat",
                        sourceId=pk,
                        specificOption=None,
                        optionSource=''
                    )
                level.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LevelSerializer(serializers.ModelSerializer):
    """JSON serializer for levels
    """
    # levelSkills = LevelSkillSerializer(many=True)
    classs = ClasssSerializer()
    levelDetails = ClassLevelSerializer()

    class Meta:
        model = Level
        fields = ('id', 'classs', 'characterLevel', 'HDRoll', 'statIncrease', 'feat',
                  'classFeat', 'levelDetails', "skillAssignment")
        depth = 1
