from rest_framework import serializers
from .models import programmer

class serializerprogrammer(serializers.ModelSerializer): 
    class Meta:
        model=programmer #modelo con el cual vamos a trabajar
        fields=('fullname','nickname','age','is_active')# campos (columnas a mi entender)django genera automatic.pk a los campos
        # el id pk esta en la base de datos directamente con django
        
        
        
    
