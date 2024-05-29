from django.urls import path
from modulapp import views

urlpatterns = [
    path('', views.my_view,name='my_view'),

]