from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import apimodel
from api.serializer import apiserializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = apimodel.objects.all()
        serializer = apiserializer(posts, many=True)
        return Response(serializer.data)




