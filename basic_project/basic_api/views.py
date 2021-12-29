from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from basic_api.models import Article
from basic_api.serializers import ArticleSerializer


class ArticleListAPIView(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request):
        """
        Retrieve all instances.
        """
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new instance.
        """
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        """ 
        Retrieve an specific instance. 
        """
        try:
            return Article.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        """ 
        Return the specified instance.
        """
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        """ 
        Update all information of the specified object
        """
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete the specified object 
        """
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
