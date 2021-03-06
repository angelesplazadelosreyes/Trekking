from django.urls import path
from Publico import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('rutas', views.rutas, name="Rutas"),
    path('ruta', views.ruta, name="Ruta"),
    path('ruta1', views.ruta1, name="Ruta1"),
    path('calendario', views.calendario, name="Calendario"),
    path('galeria', views.galeria, name="Galeria"),
    path('foro', views.foro, name="Foro"),
    path('faq', views.faq, name="Faq"),
    path('noticias', views.noticias, name="Noticias"),
    path('noticia', views.noticia, name="Noticia"),
    path('contacto', views.contacto, name="Contacto"),
    path('acceso_registro', views.acceso_registro, name="Acceso_Registro"),
]