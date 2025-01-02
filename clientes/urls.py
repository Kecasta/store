from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name = 'clientes'),
    path('ver/<int:id>', views.ver, name = 'clientes_ver'),
    path('editar/<int:id>', views.editar, name = 'clientes_editar'),
    path('crear/', views.crear, name = 'clientes_crear'),
    path('borrar/<int:id>', views.borrar, name='clientes_borrar')
]