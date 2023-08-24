from rest_framework import  viewsets
from .serializer import serializerprogrammer
from .models import programmer

class programmerViewSet(viewsets.ModelViewSet):#accedemos con la queryset a la orm q nos proporciona django--parecido a flask
    queryset=programmer.objects.all()#lista elementos de un modelo es decir de la tabla 
    serializer_class=serializerprogrammer
    ##vista ya creada
    

# Create your views here.
