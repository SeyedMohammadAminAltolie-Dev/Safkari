from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CarSerializer,CarOwnerSerializer
from .models import Car, CarOwner
# Create your views here.
class CarOwnersList(generics.ListCreateAPIView):
    serializer_class = CarOwnerSerializer
    queryset = CarOwner.objects.all()
    permission_classes = (IsAuthenticated,)


class CarOwnerEdit(generics.UpdateAPIView):
    serializer_class = CarOwnerSerializer
    queryset = CarOwner.objects.all()
    permission_classes = (AllowAny,)
    def update(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = CarOwner.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class CarsList(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)


class CarEdit(generics.UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Car.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

