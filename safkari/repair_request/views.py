from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .serializers import RepairRequestSerializer, RepairItemSerializer,AlbumSerializer,ImageSerializer,ExtraItemSerializer,PaymentSerializer
from .models import Repair_Request, RepairItem,Album,Image ,ExtraItems,Payment


# Create your views here.

class RepaireRequestList(generics.ListCreateAPIView):
    serializer_class = RepairRequestSerializer
    queryset = Repair_Request.objects.all()
    permission_classes = (IsAuthenticated,)

class RepaireRequestEdit(generics.UpdateAPIView):
    serializer_class = RepairRequestSerializer
    queryset = Repair_Request.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Repair_Request.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class RepaireItemList(generics.ListCreateAPIView):
    serializer_class = RepairItemSerializer
    queryset = RepairItem.objects.all()
    permission_classes = (IsAuthenticated,)

class RepaireItemEdit(generics.UpdateAPIView):
    serializer_class = RepairItemSerializer
    queryset = RepairItem.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = RepairItem.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class NewAlbum(generics.CreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = (IsAuthenticated,)

class AlbumList(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = (IsAuthenticated,)

class AlbumEdit(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Album.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class NewImage(generics.CreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = (IsAuthenticated,)

class ImageList(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = (IsAuthenticated,)

class ImageEdit(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Album.Image.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ExtraItemsList(generics.ListCreateAPIView):
    serializer_class = ExtraItemSerializer
    queryset = ExtraItems.objects.all()
    permission_classes = (IsAuthenticated,)

class ExtraItemsEdit(generics.UpdateAPIView):
    serializer_class = ExtraItemSerializer
    queryset = ExtraItems.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = ExtraItems.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class NewPayment(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)



class PaymentList(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

class PaymentEdit(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Payment.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


