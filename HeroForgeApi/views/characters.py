"""View module for handling requests about characters"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from django.contrib.auth.models import User
from HeroForgeApi.models import Level, Character, Level, CharacterFeat, Race, ClassSkill
from HeroForgeApi.models.classLevel import ClassLevel
from HeroForgeApi.models.classs import Classs
from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models.levelSkill import LevelSkill
from HeroForgeApi.models.skill import Skill
from HeroForgeApi.views.levels import LevelSerializer


class CharactersView(ViewSet):
    """Character views"""

    def list(self, request):
        """Handle GET requests to get all characters

        Returns:
            Response -- JSON serialized list of characters
        """
        if request.auth.user.is_staff:
            characters = Character.objects.all()
        else:
            characters = Character.objects.filter(user = request.auth.user)
        serializer = CharactersSerializer(characters, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """handles get requests for individual characters

        returns: all the character details possible
        """
        character = Character.objects.get(pk = pk)
        serializer = CharactersSerializer(character)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized characters instance
        """
        #create the character
        character = Character.objects.create(
            name = request.data['name'],            
            campaign = request.data['campaign'],            
            str = request.data['str'],            
            dex = request.data['dex'],            
            con = request.data['con'],            
            int = request.data['int'],            
            wis = request.data['wis'],            
            cha = request.data['cha'],
            user = request.auth.user,            
        )
        #establish its initial level
        level = Level.objects.create(
            character=character,
            characterLevel = 1,
            HDRoll = 0,
        )
        #create the appropriate level skills
        skills = Skill.objects.all()
        for skill in skills:
            LevelSkill.objects.create(
                level = level,
                skill = skill,
                multiTypeName = ''
            )
        serializer = CharactersSerializer(character)
        return Response(serializer.data, status=201)
        
    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        characters = Character.objects.get(pk=pk)
        characters.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

    def update(self, request, pk):
        """Handle PUT requests for a characters, can only change stat increases and change to hd
        changes to feats are handled separately

        Returns:
            Response -- Empty body with 204 status code
        """
        character = Character.objects.get(pk=pk)
        if request.data['name']: character.name = request.data['name']
        if request.data['campaign']: character.campaign = request.data['campaign']
        if request.data['xp']: character.xp = request.data['xp']
        if request.data['str']: character.str = request.data['str']
        if request.data['dex']: character.dex = request.data['dex']
        if request.data['con']: character.con = request.data['con']
        if request.data['int']: character.int = request.data['int']
        if request.data['wis']: character.wis = request.data['wis']
        if request.data['cha']: character.cha = request.data['cha']
        if request.data['race']: character.race = Race.objects.get(pk=request.data['race'])
        character.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class CharacterFeatSerializer(serializers.ModelSerializer):
    class Meta:
        model= CharacterFeat
        exclude= ("specificOption","optionSource","character")
        depth=1

class CharactersSerializer(serializers.ModelSerializer):
    """JSON serializer for characterss
    """
    learnedFeats = CharacterFeatSerializer(many=True)
    level_set= LevelSerializer(many=True)
    class Meta:
        model = Character
        fields = ('id', 'xp', 'name','campaign','str', 'dex','con','int','wis','cha', 
                  'race', 'proficiencies', 'equipment', 'level_set',
                  'learnedFeats','user')

