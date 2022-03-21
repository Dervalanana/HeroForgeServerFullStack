"""View module for handling requests about characters"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from django.contrib.auth.models import User
from HeroForgeApi.models import Level, Character, Level, CharacterFeat
from HeroForgeApi.models.classLevel import ClassLevel
from HeroForgeApi.models.classs import Classs
from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models.levelSkill import LevelSkill
from HeroForgeApi.models.skill import Skill


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
            characters = Character.objects.filter(user = User.objects.get(pk = request.auth.user))
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
        characters = Character.objects.create(
            name = request.data['name'],            
            campaign = request.data['campaign'],            
            str = request.data['str'],            
            dex = request.data['dex'],            
            con = request.data['con'],            
            int = request.data['int'],            
            wis = request.data['wis'],            
            cha = request.data['cha'],
            user = User.objects.get(pk=request.auth.user)            
        )
        serializer = CharactersSerializer(characters)
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
    
    # @action(methods=['PUT'], detail=True)
    # def changeClass(self, request, pk):
    #     """lets a character change characterss"""
    #     try:
    #         characterFeat = CharacterFeat.get(
    #             source = "classFeat",
    #             sourceId = pk
    #         )
    #         characterFeat.delete()
    #     finally:
    #         try:
    #             characterFeat = CharacterFeat.get(
    #                 source = "fixedFeat",
    #                 sourceId = pk
    #             )
    #             characterFeat.delete()
    #         finally:
    #             Characterss = Characters.objects.filter(
    #                 character = Character.objects.get(request.data['characterId']),
    #                 classs = Classs.objects.get(request.data['classs'])
    #             ) #determines how many characterss of a class a character currently has
    #             characters = Characters.objects.get(pk=pk) #grab the current characters
    #             characters.classs = Classs.objects.get(request.data['classs']) #set the class to the current class
    #             characters.charactersDetails = ClassCharacters.objects.get(
    #                 classs = Classs.objects.get(request.data['classs']),
    #                 characters = Characterss.len()+1
    #             ) #the next class characters that the character doesn't have is set as the current details
    #             if characters.charactersDetails.fixedFeat:
    #                 CharacterFeat.objects.create(
    #                     feat = Feat.objects.get(characters.charactersDetails.fixedFeat),
    #                     character = Character.objects.get(request.data['characterId']),
    #                     source = "fixedFeat",
    #                     sourceId = pk,
    #                     specificOption = None,
    #                     optionSource = ''
    #                 )

class CharactersSerializer(serializers.ModelSerializer):
    """JSON serializer for characterss
    """
    class Meta:
        model = Character
        fields = ('id', 'xp', 'name','campaign','str', 'dex','con','int','wis','cha', 
                  'race', 'proficiencies', 'equipment', 'level_set', 'characterfeat_set')
        depth = 2
