
from django.urls import path
from . import views,delete_menu_item

urlpatterns = [
path('', views.home, name='home'),
path('menu/', views.home, name='about'),
path('delete/<int:item_id>/', delete_menu_item, name='delete_menu_item')
 ]