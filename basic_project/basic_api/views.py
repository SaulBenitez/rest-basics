from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from basic_api.models import Article
from basic_api.serializers import ArticleSerializer

@csrf_exempt
def article_list(request):

    reqaux = str(request.method)
    #return HttpResponse(reqaux)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except:
        return HttpResponse(status=400)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)