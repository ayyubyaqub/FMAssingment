from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer,VendorSerializer,Purchase_orderSerializer,Vendor_performance_HistorySerializer
# Create your views here.


# tokken 
from rest_framework_simplejwt.tokens import RefreshToken
def get_tokens_for_user(user):
       refresh = RefreshToken.for_user(user)
       return {
              "username": user.username,
              "refresh": str(refresh),
              "access": str(refresh.access_token)
              }




# login view
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
class LoginView(APIView):
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        res_data = get_tokens_for_user(User.objects.get(username=username))
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": res_data
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)


# user registeration

from django.contrib.auth.models import User
from rest_framework import status
class SignupView(APIView):
    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
                """If the validation success, it will created a new user."""
                serializer.save()
                res = { 'status' : status.HTTP_201_CREATED }
                return Response(res, status = status.HTTP_201_CREATED)
        res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
        return Response(res, status = status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import IsAuthenticated
# vendor management
class VendorView(APIView):
    
    permission_classes = [ IsAuthenticated ]
    def get(self,request,pk=None):
        if pk!=None:
            vendor=Vendor.objects.get(id=pk)
            serializer=VendorSerializer(vendor)
            return JsonResponse({'status':200,'data':serializer.data})
        vendors=Vendor.objects.all()
        serializer=VendorSerializer(vendors,many=True)
        return JsonResponse({'status':200,'data':serializer.data})
    def post(self,request):        
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':201,'msg':'Vendor Created','data':serializer.data})
        else:
            return JsonResponse({'status':500,'msg':'Error:'+str(serializer.errors)})
   
    def put(self,request,pk):
        vendor = Vendor.objects.get(id=pk)
        serializer = VendorSerializer(vendor, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':201,'msg':'Vendor updated','data':serializer.data}) 
        else:
            return JsonResponse({'status':500,'msg':'Error:'+str(serializer.errors)})
    def delete(self,request,pk):
        try:
            vendor = Vendor.objects.get(id=pk)
            vendor.delete()
            return JsonResponse({'status':200,'msg':'Vendor deleted'}) 
        except :
            return JsonResponse({"status":500,"msg":"something went wrong"})

class Purchase_orderView(APIView):
    
    permission_classes = [ IsAuthenticated ]
    
    def get(self,request,pk=None):
        if pk!=None:
            puchase_order=Purchase_order.objects.get(id=pk)
            serializer=Purchase_orderSerializer(puchase_order)
            return JsonResponse({'status':200,'data':serializer.data})
        puchase_orders=Purchase_order.objects.all()
        serializer=Purchase_orderSerializer(puchase_orders,many=True)
        return JsonResponse({'status':200,'data':serializer.data})
    def post(self,request):
        serializer=Purchase_orderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':201,'msg':'Purchase_order Created','data':serializer.data})
        else:
            return JsonResponse({'status':500,'msg':'Something went wrong'+str(serializer.errors)})

    def put(self,request,pk):
        purchase_order = Purchase_order.objects.get(id=pk)
        serializer = Purchase_orderSerializer(purchase_order, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':201,'msg':'Purchase_order updated','data':serializer.data}) 
        else:
            return JsonResponse({'status':500,'msg':'Error:'+str(serializer.errors)})
   
    def delete(self,request,pk):
        try:
            purchase_order = Purchase_order.objects.get(id=pk)
            purchase_order.delete()
            return JsonResponse({'status':200,'msg':'Purchase_order deleted'}) 
        except :
            return JsonResponse({"status":500,"msg":"something went wrong"})
            

class Vendor_performance_HistoryView(APIView):
    
    permission_classes = [ IsAuthenticated ]
    def get(self,request,pk=None):
        if pk!=None:
            vendor_performance_history=Vendor_performance_History.objects.filter(vendor_id=pk)
            serializer=Vendor_performance_HistorySerializer(vendor_performance_history,many=True)
            return JsonResponse({'status':200,'data':serializer.data})
        vendor_performance_history=Vendor_performance_History.objects.all()
        serializer=Vendor_performance_HistorySerializer(vendor_performance_history,many=True)
        return JsonResponse({'status':200,'data':serializer.data})


class VendorPerformance(APIView):
    permission_classes = [ IsAuthenticated ]
    def get(self,request,pk):
        try:
            vendor_performance=Vendor.objects.get(id=pk)
            serializer=VendorSerializer(vendor_performance)
            return JsonResponse({'status':200,"data":serializer.data})
        except Vendor.DoesNotExist:
            return JsonResponse({'status':404,"msg":"Vendor DoesNotExist"})
               

class PerchaseOrderAcknowledge(APIView):
    permission_classes = [ IsAuthenticated ]
    def post(self,request,pk):
        try:
            purchase_order=Purchase_order.objects.get(id=pk)
            purchase_order.acknowledgment_date=datetime.now()
            purchase_order.save()
            return JsonResponse({'status':201,'msg':'Purchase_order acknowledged'}) 
        except Vendor.DoesNotExist:
            return JsonResponse({'status':404,"msg":"Vendor DoesNotExist"})
               
