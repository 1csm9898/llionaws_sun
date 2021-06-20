from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("<str:id>",detail,name="detail"),
    path("create/",create,name="create"),
    path("new/",new,name="new"),
    path("edit/<str:id>",edit,name="edit"),
    path("update/<str:id>",update,name="update"),
    path("delete/<str:id>",delete,name="delete"),

]
