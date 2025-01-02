from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name = 'productos'),
    path('ver/<int:id>', views.ver, name = 'productos_ver'),
    path('editar/<int:id>', views.editar, name = 'productos_editar'),
    path('crear/', views.crear, name = 'productos_crear'),
    path('borrar/<int:id>', views.borrar, name='productos_borrar')
]