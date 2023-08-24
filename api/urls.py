from django.urls import path,include
from rest_framework import routers
from  . import views

# # creamos en rutador, este nos permite manejar varias rutas

router=routers.DefaultRouter()
router.register(r'programmer',views.programmerViewSet,basename='programmer')
# la base de este endpoint va a ser programmers pero recordemos q las rutas van a cambiar segun endpoint

urlpatterns = [
    path('',include(router.urls))
    
]