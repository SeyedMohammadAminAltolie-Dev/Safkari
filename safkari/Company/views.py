from rest_framework import generics
from rest_framework.response import Response
from .serializers import CompanySerializer,BranchSerializer,WorkerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Company, Branch, Worker
# Create your views here.


class NewCompany(generics.CreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (AllowAny,)

class Companies_lists(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)

class CompanyEdit(generics.UpdateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)
    def update(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Company.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class NewBranch(generics.CreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (AllowAny,)

class Branches_lists(generics.ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsAuthenticated,)



class BranchEdit(generics.UpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsAuthenticated,)
    def update(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Branch.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class NewWorker(generics.ListCreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = (AllowAny,)

class Workers_list(generics.ListAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = (IsAuthenticated,)

class WorkerEdit(generics.UpdateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = (AllowAny,)
    def update(self, request, *args, **kwargs):
        pk = request.data["id"]
        user = Worker.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)