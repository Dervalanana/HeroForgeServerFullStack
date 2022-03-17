"""View module for handling requests about skill types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HeroForgeApi.models import Skill, Level, LevelSkill, Classs, ClassSkill


class SkillView(ViewSet):
    """Level up skill types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single skill
        
        Returns:
            Response -- JSON serialized skill
        """
        try:
            skill = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(skill)
            return Response(serializer.data)
        except Skill.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all skills

        Returns:
            Response -- JSON serialized list of skills
        """
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized skill instance
        """
        if request.auth.user.is_staff: #only admins can C-UD
            skill = Skill.objects.create(
                name=request.data['name'],
                trainedOnly=request.data['trainedOnly'],
                multiType=request.data['multiType'],
                attribute = request.data['attribute']
            )
            levels = Level.objects.all()
            classes = Classs.objects.all()
            #whenver you create a new skill, it needs to be linked to all existing levels and classes
            for level in levels:
                LevelSkill.objects.create(
                    level=level,
                    skill=skill,
                    points=0,
                    multiTypeName="" #same for this
                )
            for classs in classes:
                ClassSkill.objects.create(
                    classs=classs,
                    skill=skill,
                    value= False #you can always edit this at a later time
                )
            serializer = SkillSerializer(skill)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"},status=403)
        
    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff
        
        Returns
            Response --- 204 no content
        """
        if request.auth.user.is_staff: #only admins can C-UD
            skill = Skill.objects.get(pk=pk)
            skill.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)
        
    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        if request.auth.user.is_staff: #only admins can C-UD
            print(request.data['trainedOnly'])
            skill = Skill.objects.get(pk=pk)
            skill.name=request.data['name']
            skill.trainedOnly=request.data['trainedOnly']
            skill.multiType=request.data['multiType']
            skill.attribute = request.data['attribute']
            skill.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)

    
    
class SkillSerializer(serializers.ModelSerializer):
    """JSON serializer for skills
    """
    class Meta:
        model = Skill
        fields = ('id', 'name', 'trainedOnly','multiType','attribute')