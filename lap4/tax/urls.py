from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name = "index"),
    path("taxrate",views.tR,name = "Calc"),
    path("<str:cost>",views.tC,name = "Calc"),
    
]