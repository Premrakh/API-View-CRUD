from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import JsonResponse
from rest_framework import status
from django.http import HttpResponse
import json
# Create your views here.

class GetData(APIView):
    def get(self,request):
        py_data=Info.objects.all()
        d1=DataCon(py_data, many=True)
        return Response(d1.data)                     # DRF Data
        # return JsonResponse(d1.data, safe=False)     #--> html format ma data 
    
class PostData(APIView):
    def post(self,request):
        d1=DataCon(data=request.data)
        if d1.is_valid():
            d1.save()
            return Response(d1.data)           
        else:
            return Response(d1.errors)        
        
class UpdateData(APIView):
    def put(self,request,pk):
        try:
            py_data=Info.objects.get(id=pk)
            d1=DataCon(py_data, data=request.data)
            if d1.is_valid():
                d1.save()
                py_data=Info.objects.all()
                d1=DataCon(py_data,many=True)
                return Response(d1.data)
            else:
                return Response(d1.errors) 
        except:
            data={'message':'id not found in data'}
            return Response(data,status=status.HTTP_404_NOT_FOUND)

class DelData(APIView):
    def delete(self,request,pk):
        try:
            py_data=Info.objects.get(id=pk)
            py_data.delete()
            py_data=Info.objects.all()
            d1=DataCon(py_data,many=True)
            return Response(d1.data)       
        except:
            data={'message':'id not found in data'}
            return Response(data,status=status.HTTP_404_NOT_FOUND)
        
class PatchData(APIView):
    def patch(self,request,pk):
        try:
            py_data=Info.objects.get(id=pk)
            d1=DataCon(py_data, data=request.data)
            if d1.is_valid():
                d1.save()
                py_data=Info.objects.all()
                d1=DataCon(py_data,many=True)
                return Response(d1.data)
        except:
                data = {'message': 'id not found in data'}
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(d1.errors)

