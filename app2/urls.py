
from django.urls import path
from .import views
urlpatterns = [

    path('',views.test1fun,name='test1'),
    path('cyber',views.cyberfun,name='cyber'),
]
