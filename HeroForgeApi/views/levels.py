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


class LevelsView(ViewSet):
    """Level up level types view"""

    def list(self, request):
        """Handle GET requests to get all levels

        Returns:
            Response -- JSON serialized list of levels
        """
        levels = Level.objects.filter(character= Character.objects.get(pk=request.data['characterId']))
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized level instance
        """
        level = Level.objects.create(
            character=Character.objects.get(request.data['character']),
            classs=Classs.objects.get(request.data['classs']),
            characterLevel=request.data['characterLevel'],
            HDRoll = 0,            
        )
        skills = Skill.objects.all()
        for skill in skills:
            LevelSkill.objects.create(
                skill = skill,
                level = level,
                points = 0,
                multiTypeName = ''
            )
        serializer = LevelSerializer(level)
        return Response(serializer.data, status=201)
        
    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        level = Level.objects.get(pk=pk)
        level.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

    def update(self, request, pk):
        """Handle PUT requests for a level, can only change stat increases and change to hd
        changes to feats are handled separately

        Returns:
            Response -- Empty body with 204 status code
        """
        level = Level.objects.get(pk=pk)
        if request.data['statIncrease']: level.statIncrease=request.data['statIncrease']
        if request.data['HDRoll']: level.HDRoll=request.data['HDRoll']
            
    
    @action(methods=['PUT'], detail=True)
    def changeClass(self, request, pk):
        """lets a character change levels"""
        try:
            characterFeat = CharacterFeat.get(
                source = "classFeat",
                sourceId = pk
            )
            characterFeat.delete()
        finally:
            try:
                characterFeat = CharacterFeat.get(
                    source = "fixedFeat",
                    sourceId = pk
                )
                characterFeat.delete()
            finally:
                Levels = Level.objects.filter(
                    character = Character.objects.get(request.data['characterId']),
                    classs = Classs.objects.get(request.data['classs'])
                ) #determines how many levels of a class a character currently has
                level = Level.objects.get(pk=pk) #grab the current level
                level.classs = Classs.objects.get(request.data['classs']) #set the class to the current class
                level.levelDetails = ClassLevel.objects.get(
                    classs = Classs.objects.get(request.data['classs']),
                    level = Levels.len()+1
                ) #the next class level that the character doesn't have is set as the current details
                if level.levelDetails.fixedFeat:
                    CharacterFeat.objects.create(
                        feat = Feat.objects.get(level.levelDetails.fixedFeat),
                        character = Character.objects.get(request.data['characterId']),
                        source = "fixedFeat",
                        sourceId = pk,
                        specificOption = None,
                        optionSource = ''
                    )

class LevelSerializer(serializers.ModelSerializer):
    """JSON serializer for levels
    """
    class Meta:
        model = Level
        fields = ('id', 'classs', 'characterLevel','HDRoll','statIncrease', 'feat', 
                  'levelSkills', 'classFeat', 'levelDetails')
        depth = 1
