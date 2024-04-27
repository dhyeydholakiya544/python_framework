from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializer import *

# Create your views here.

@api_view(['get'])
def viewdata(request):
    user_data = User.objects.all()
    ser_data =  UserSerializer(user_data,many=True)
    return Response({'data':ser_data.data})

@api_view(['post'])
def adddata(request):

    
    ser_data =  UserSerializer(data=request.data)
    if not ser_data.is_valid():
        return Response({"message":"something went wrong","errors":ser_data.errors})
    ser_data.save()
    return Response({"userdata":ser_data.data,"message":"User inserted"})

@api_view(['put'])
def updatedata(request,id):
    try:
        user_data = User.objects.get(id=id)
        ser_data = UserSerializer(user_data,request.data)
        if not ser_data.is_valid():
            return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"User Updated"})
    except Exception as e:
        print(e)
        return Response({"Error":"Id not found"})
    
@api_view(['delete'])
def deletedata(request,id):
    try:
        user_data = User.objects.get(id=id)
        user_data.delete()
        return Response({"message":"data deleted"})
    except Exception as e:
        print(e)
        return Response({"Error":"Id not found"})
    

class BookApi(APIView):
    def get(self,request):
        booksdata = Book.objects.all()
        bookser = BookSerializer(booksdata,many=True)
        return Response({"data":bookser.data})
    
    def post(self,request):

        ser_data =  BookSerializer(data=request.data)
       
        if not ser_data.is_valid():
          return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"Book inserted"})


    def put(self,request):
        try:

            book_data = Book.objects.get(id=request.data['id'])
            ser_data = BookSerializer(book_data,request.data)
            if not ser_data.is_valid():
                return Response({"message":"something went wrong","errors":ser_data.errors})
            ser_data.save()
            return Response({"bookdata":ser_data.data,"message":"Book Updated"})
        except Exception as e:
            print(e)
            return Response({"Error":"Id not found"})
        
    def delete(self,request):
        try:
            book_data = Book.objects.get(id=request.data['id'])
            book_data.delete()
            return Response({"message":"data deleted"})
        except Exception as e:
            
            return Response({"Error":"Id not found"})
        