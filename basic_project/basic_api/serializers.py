from rest_framework import serializers
from basic_api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        ''' 
        fields = [
            'id', 
            'title',
            'author',
        ]
        '''
        fields = '__all__'