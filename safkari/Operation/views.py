from .serializers import OperatorSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.

class Users_list(generics.ListAPIView):
    serializer_class = OperatorSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)

class NewUser(generics.ListCreateAPIView):
    serializer_class = OperatorSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

class UserEdit(generics.UpdateAPIView):
    serializer_class = OperatorSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    def patch(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = CustomUser.objects.get(pk=pk)
        serializer = self.get_serializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)