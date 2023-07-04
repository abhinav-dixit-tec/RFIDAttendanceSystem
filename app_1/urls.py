from django.urls import path
from . import views
urlpatterns = [
    path('', views.start, name='start'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_pass/',views.change_pass, name='change_pass')
]