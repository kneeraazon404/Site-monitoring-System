from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cement
from .serializers import CementSerializer


@api_view(["GET"])
def apiOverview(request, pk):
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
    Cements = Cement.objects.get(pk=pk)
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
    cement = Cement.objects.get(id=pk)
    serializer = CementSerializer(instance=cement, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def cementDelete(request, pk):
    cement = Cement.objects.get(id=pk)
    cement.delete()

    return Response("Item succsesfully deleted!")
