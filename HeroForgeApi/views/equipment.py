"""View module for handling requests about equipment types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from HeroForgeApi.models import Equipment, Character, Equipped, Equipment, Proficient, ClassLevel, Race


class EquipmentView(ViewSet):
    """Level up equipment types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single equipment

        Returns:
            Response -- JSON serialized equipment
        """
        try:
            equipment = Equipment.objects.get(pk=pk)
            serializer = EquipmentSerializer(equipment)
            return Response(serializer.data)
        except Equipment.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all equipments

        Returns:
            Response -- JSON serialized list of equipments
        """
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized equipment instance
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            equipment = Equipment.objects.create(
                name=request.data['name'],
            )
            if request.data['armorType']: equipment.armorType=request.data['armorType']
            if request.data['armorBonus']: equipment.armorBonus=request.data['armorBonus']
            if request.data['shieldBonus']: equipment.shieldBonus=request.data['shieldBonus']
            if request.data['ACP']: equipment.ACP=request.data['ACP']
            if request.data['ASF']: equipment.ASF=request.data['ASF']
            if request.data['maxDex']: equipment.maxDex=request.data['maxDex']
            if request.data['weaponType']: equipment.weaponType=request.data['weaponType']
            if request.data['weaponUsage']: equipment.weaponUsage=request.data['weaponUsage']
            if request.data['mediumDamage']: equipment.mediumDamage=request.data['mediumDamage']
            if request.data['mediumWeight']: equipment.mediumWeight=request.data['mediumWeight']
            if request.data['finesse']: equipment.finesse=request.data['finesse']
            if request.data['reach']: equipment.reach=request.data['reach']
            if request.data['range']: equipment.range=request.data['range']
            if request.data['damageType']: equipment.damageType=request.data['damageType']
            if request.data['special']: equipment.special=request.data['special']
            serializer = EquipmentSerializer(equipment)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            equipment = Equipment.objects.get(pk=pk)
            equipment.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            equipment = Equipment.objects.get(pk=pk)
            if request.data['armorType']: equipment.armorType=request.data['armorType']
            if request.data['armorBonus']: equipment.armorBonus=request.data['armorBonus']
            if request.data['shieldBonus']: equipment.shieldBonus=request.data['shieldBonus']
            if request.data['ACP']: equipment.ACP=request.data['ACP']
            if request.data['ASF']: equipment.ASF=request.data['ASF']
            if request.data['maxDex']: equipment.maxDex=request.data['maxDex']
            if request.data['weaponType']: equipment.weaponType=request.data['weaponType']
            if request.data['weaponUsage']: equipment.weaponUsage=request.data['weaponUsage']
            if request.data['mediumDamage']: equipment.mediumDamage=request.data['mediumDamage']
            if request.data['mediumWeight']: equipment.mediumWeight=request.data['mediumWeight']
            if request.data['finesse']: equipment.finesse=request.data['finesse']
            if request.data['reach']: equipment.reach=request.data['reach']
            if request.data['range']: equipment.range=request.data['range']
            if request.data['damageType']: equipment.damageType=request.data['damageType']
            if request.data['special']: equipment.special=request.data['special']
            equipment.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
    
    @action(methods=['POST'], detail=False)
    def equip(self, request):
        """lets a character equip an item"""
        if (request.auth.user == Character.objects.get(pk=request.data['characterId']).user or request.auth.user.is_staff):
            equipped = Equipped.objects.create(
                character=Character.objects.get(pk=request.data['characterId']),
                equipment=Equipment.objects.get(pk=request.data['equipmentId'])
                )
            serializer = EquippedSerializer(equipped)
            return Response(serializer.data)
        else:
            return Response({'message': "how did you find this"}, status=403)
    
    @action(methods=['GET'], detail=False)
    def equipped(self, request):
        """gets a charcter's current equipment"""
        if (request.auth.user == Character.objects.get(pk=request.data['characterId']).user or request.auth.user.is_staff):
            equipped = Equipped.objects.filter(
                character=Character.objects.get(pk=request.data['characterId'])
                )
            serializer = EquippedSerializer(equipped, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "how did you find this"}, status=403)
        
    @action(methods=['DELETE'], detail=True)
    def unequip(self, request, pk):
        """lets a character unequip an item"""
        if (request.auth.user == Character.objects.get(pk=request.data['characterId']).user or request.auth.user.is_staff):
            equipped = Equipped.objects.get(pk=pk)
            equipped.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
        
    @action(methods=['DELETE'], detail=False)
    def unequipAll(self, request):
        """lets a character unequip all items"""
        if (request.auth.user == Character.objects.get(pk=request.data['characterId']).user or request.auth.user.is_staff):
            equipped = Equipped.objects.filter(character=Character.objects.get(pk=request.data['characterId']))
            for item in equipped:
                item.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
        
    @action(methods=["POST"], detail=False)
    def addRaceClassFeatProficiency(self, request):
        """ adds preset proficiencies to be gained upon picking a race or class"""
        proficient = Proficient.objects.create(equipment= request.data['equipment'])
        if request.data['class']: proficient.classLevel = ClassLevel.objects.get(classs=request.data['class'],level=1)
        if request.data['race']: proficient.race = Race.objects.get(pk = request.data['race'])
        serializer = ProficientSerializer(proficient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EquipmentSerializer(serializers.ModelSerializer):
    """JSON serializer for equipments
    """
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'armorType', 'armorBonus', 'shieldBonus', 'ACP', 'ASF', 'maxDex', 'weaponType', 'weaponUsage',
                  'mediumDamage', 'mediumWeight', 'finesse', 'reach', 'range', 'damageType', 'special')
class EquippedSerializer(serializers.ModelSerializer):
    """JSON serializer for current equipments
    """
    class Meta:
        model = Equipped
        fields = ('id', 'equipment','character')
        
class ProficientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proficient
        fields = ('id', 'classLevel','race','equipment')
        depth = 1