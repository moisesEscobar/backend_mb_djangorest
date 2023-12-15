from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .utils import sorting_algorithm
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserFilerAgeView(generics.ListCreateAPIView):
    def get(self, request,age, format=None):
        queryset = User.objects.filter(age=age)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class UserListNameView(generics.ListCreateAPIView):
    def get(self, request, format=None):
        queryset = User.objects.filter()
        users = sorting_algorithm(queryset, key=lambda user: user.name)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserListView(generics.ListCreateAPIView):
    def get(self, request, format=None):
        queryset = User.objects.filter()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class UserView(generics.ListCreateAPIView):
    def get_object(self, id):
        try:
            return User.objects.get(pk=id,)
        except User.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        user = self.get_object(id)
        if user != False:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        User.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        user = self.get_object(id)
        if user != False:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        #users = sorting_algorithm(users, key=lambda user: user.las_name)

class UserPdfListView(APIView):
    def get(self, request):
        queryset = User.objects.filter()
        users = queryset.order_by('name')  
        serializer = UserSerializer(users, many=True)

        # Crear el objeto de respuesta PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="usuarios.pdf"'

        # Crear el documento PDF
        p = canvas.Canvas(response)
        p.drawString(250, 800, "Lista de usuarios")

        # Agregar datos de usuarios al PDF
        y_position = 780
        for user_data in serializer.data:
            user_string = f"Nombre: {user_data['name']}, Apellidos: {user_data['last_name']} {user_data['last_name']}, Edad: {user_data['age']} , Telefono: {user_data['phone']}"
            p.drawString(45, y_position, user_string)
            y_position -= 15  # Espaciado entre usuarios
        p.showPage()
        p.save()
        return response