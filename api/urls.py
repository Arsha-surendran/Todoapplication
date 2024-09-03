from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register("todos",views.TodosView,basename="todos")


urlpatterns = [
    path('register/',views.RegistrationView.as_view())


    
    ] + routers.urls