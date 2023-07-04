from django.urls import path
from . import views
urlpatterns = [
    path('', views.mark, name='mark'),   
    path('test/',views.test, name='test')    
]