from django.shortcuts import render
from .models import PostTest
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset = PostTest.objects.all()

@api_view(["GET","POST"])
def ApiView(request):
    if request.method == 'GET':
        note = PostTest.objects.all()
        serializer = PostSerializer(note, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(["GET","PUT","DELETE"])
def strApi(request, pk):
    if request.method == 'GET':
        stu = PostTest.objects.get(id=pk)
        serializer = PostSerializer(stu)
        return Response(serializer.data)

    if request.method=="PUT":
        note = PostTest.objects.get(id=pk)
        serializer=PostSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method=="DELETE":
        data = PostTest.objects.get(id=pk)
        data.delete()
        return Response({"msg":'data Deleted'})
