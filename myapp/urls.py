from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello, name="hello"),
    path("req_det", views.request_details),
    path("dishes/",views.menuitems),
    path("dishes/<str:dish>",views.menuitems)
]