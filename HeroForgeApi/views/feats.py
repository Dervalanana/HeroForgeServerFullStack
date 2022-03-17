"""View module for handling requests about feat types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HeroForgeApi.models import Feat, Classs


class FeatView(ViewSet):
    """Level up feat types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single feat

        Returns:
            Response -- JSON serialized feat
        """
        try:
            feat = Feat.objects.get(pk=pk)
            serializer = FeatSerializer(feat)
            return Response(serializer.data)
        except Feat.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all feats

        Returns:
            Response -- JSON serialized list of feats
        """
        feats = Feat.objects.all()
        serializer = FeatSerializer(feats, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized feat instance
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            feat = Feat.objects.create(
                name=request.data['name'],
                description=request.data['description'],
                strPR=request.data['strPR'],
                dexPR=request.data['dexPR'],
                conPR=request.data['conPR'],
                intPR=request.data['intPR'],
                wisPR=request.data['wisPR'],
                chaPR=request.data['chaPR'],
                fortPR=request.data['fortPR'],
                refPR=request.data['refPR'],
                willPR=request.data['willPR'],
                babPR=request.data['babPR'],
                classLevelPR=request.data['classLevelPR'],
            )
            if(request.data['classPR']):
                feat.classPR = Classs.objects.get(pk=request.data['classPR'])
            else:
                feat.classPR = None
            if(request.data['feat1PR']):
                feat.feat1PR = Feat.objects.get(pk=request.data['feat1PR'])
            else:
                feat.feat1PR = None
            if(request.data['feat2PR']):
                feat.feat2PR = Feat.objects.get(pk=request.data['feat2PR'])
            else:
                feat.feat2PR = None
            if(request.data['feat3PR']):
                feat.feat3PR = Feat.objects.get(pk=request.data['feat3PR'])
            else:
                feat.feat3PR = None
            if(request.data['feat4PR']):
                feat.feat4PR = Feat.objects.get(pk=request.data['feat4PR'])
            else:
                feat.feat4PR = None
            serializer = FeatSerializer(feat)
            return Response(serializer.data, status=201)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def destroy(self, request, pk):
        """Handle Delete operations submitted by staff

        Returns
            Response --- 204 no content
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            feat = Feat.objects.get(pk=pk)
            feat.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)

    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        if request.auth.user.is_staff:  # only admins can C-UD
            feat = Feat.objects.get(pk=pk)
            feat.name = request.data['name']
            feat.description = request.data['description']
            feat.strPR = request.data['strPR']
            feat.dexPR = request.data['dexPR']
            feat.conPR = request.data['conPR']
            feat.intPR = request.data['intPR']
            feat.wisPR = request.data['wisPR']
            feat.chaPR = request.data['chaPR']
            feat.fortPR = request.data['fortPR']
            feat.refPR = request.data['refPR']
            feat.willPR = request.data['willPR']
            feat.babPR = request.data['babPR']
            feat.classLevelPR = request.data['classLevelPR']
            if(request.data['classPR'] is not None):
                feat.classPR = Classs.objects.get(pk=request.data['classPR'])
            else:
                feat.classPR = None
            if(request.data['feat1PR'] is not None):
                feat.feat1PR = Feat.objects.get(pk=request.data['feat1PR'])
            else:
                feat.feat1PR = None
            if(request.data['feat2PR'] is not None):
                feat.feat2PR = Feat.objects.get(pk=request.data['feat2PR'])
            else:
                feat.feat2PR = None
            if(request.data['feat3PR'] is not None):
                feat.feat3PR = Feat.objects.get(pk=request.data['feat3PR'])
            else:
                feat.feat3PR = None
            if(request.data['feat4PR'] is not None):
                feat.feat4PR = Feat.objects.get(pk=request.data['feat4PR'])
            else:
                feat.feat4PR = None
            feat.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "how did you find this"}, status=403)


class FeatSerializer(serializers.ModelSerializer):
    """JSON serializer for feats
    """
    class Meta:
        model = Feat
        fields = ('id', 'name', 'description', 'strPR', 'dexPR', 'conPR',
                  'intPR', 'wisPR', 'chaPR', 'fortPR', 'refPR', 'willPR',
                  'babPR', 'classLevelPR', 'classPR', 'feat1PR', 'feat2PR',
                  'feat3PR', 'feat4PR')
