from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerUser/', views.registerUser),
    path('editUser/<id>', views.editUser),
    path('updateUser/<id>', views.updateUser),
    path('deleteUser/<id>', views.deleteUser),
]