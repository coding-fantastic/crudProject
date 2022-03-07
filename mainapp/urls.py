from django.urls import path
from django.urls.conf import include 
from mainapp import views

urlpatterns = [
    path("", views.index , name='home'),
    path('add_item', views.add_item, name='add_item'),
    path('delete_item/<int:myid>/', views.delete_item, name='delete_item'),
    path('edit_item/<int:myid>/', views.edit_item, name='edit_item'),
    path('update_item/<int:myid>/', views.update_item, name='update_item'),
]