from django.urls import path
from simple_orm import views

urlpatterns = [
    path('select/<str:table>/', views.SBaseSelectAll.as_view()),
    path('insert/<str:table>/', views.SBaseInsert.as_view()),
    path('update/<str:table>/', views.SBaseUpdate.as_view()),
    path('delete/<str:table>/', views.SBaseDelete.as_view())
]
