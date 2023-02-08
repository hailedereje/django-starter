from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),

    path('detail/<str:pk>/',views.detail, name = 'detail'),
    path('create/',views.create_student, name = 'create'),
    path('update/<str:pk>/',views.update_student,name = 'update'),
    path('delete/<str:pk>/',views.delete_student, name = 'delete')
    
]