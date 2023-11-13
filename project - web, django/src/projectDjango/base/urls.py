from django.urls import path
from .views import listaPendientes, detalleTarea, crearTarea, editarTarea, eliminarTarea, logueo, paginaRegistro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', logueo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('registro/', paginaRegistro.as_view(), name="registro"),
    path('', listaPendientes.as_view(), name='tareas'),
    path('tarea/<int:pk>', detalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', crearTarea.as_view(), name='crear_tarea'),
    path('editar-tarea/<int:pk>', editarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>', eliminarTarea.as_view(), name='eliminar-tarea'),
]
