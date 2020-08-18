from django.shortcuts import render
from django.http import JsonResponse
from shorterner.models import shorturl
from shorterner.serializers import shorturlSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .utlis import code_generator,create_shortcode
from django.conf import settings
import redis
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)
# Create your views here.
@api_view(['GET','POST'])
def shorturllist(request):
    short =shorturl.objects.all()
    if request.method =='GET':
        serializer=shorturlSerializers(short,many=True)
        return Response(serializer.data)
        
    elif request.method =='POST':
        serializer=shorturlSerializers(data=request.data,required=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def shorturlview(request,pk):
    try:
        short =shorturl.objects.get(pk=pk)
    except short.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer=shorturlSerializers(short)
        return Response(serializer.data)
        

    elif request.method =='PUT':
        serializer=shorturlSerializers(short,data=request.data,required=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        short.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'},status=status.HTTP_204_NO_CONTENT)

    
