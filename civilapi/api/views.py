from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CementSerializer

from .models import Cement


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/cement-list/",
        "Detail View": "/cement-detail/<str:pk>/",
        "Create": "/cement-create/",
        "Update": "/cement-update/<str:pk>/",
        "Delete": "/cement-delete/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def cementList(request):
    Cements = Cement.objects.all().order_by("-id")
    serializer = CementSerializer(Cements, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def cementDetail(request, pk):
    Cements = Cement.objects.get(id=pk)
    serializer = CementSerializer(Cements, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def cementCreate(request):
    serializer = CementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def cementUpdate(request, pk):
    Cement = Cement.objects.get(id=pk)
    serializer = CementSerializer(instance=Cement, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def cementDelete(request, pk):
    Cement = Cement.objects.get(id=pk)
    Cement.delete()

    return Response("Item succsesfully delete!")
