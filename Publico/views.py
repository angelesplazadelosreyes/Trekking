from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
from django.http import JsonResponse
from Trekking.settings import API_KEY

WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Mexico&appid='+ API_KEY

# Create your views here.

def inicio(request):

      from Administrador.models import Aviso
      aviso = Aviso.objects.all()

      return render(request, 'Publico/inicio.html', {'aviso':aviso})


def rutas(request):

      from Administrador.models import Ruta
      rutas = Ruta.objects.all()

      return render(request, 'Publico/rutas.html', {'rutas':rutas})


def ruta(request):

      return render(request, 'Publico/ruta.html')



def ruta1(request):

      return render(request, 'Publico/ruta1.html')



def calendario(request):

      clima = requests.get(WEATHER_API_URL).json()

      if resp.status_code != 200:
        return HttpResponse('ERROR GET ' + WEATHER_API_URL + ' {}'.format(resp.status_code))
      
      return render(request, 'Publico/calendario.html', {'clima':clima})


def galeria(request):

      from Administrador.models import Galeria
      images = Galeria.objects.all()

      return render(request, 'Publico/galeria.html', {'images': images})


def foro(request):

      from Administrador.models import Mensaje, Respuesta
      pregunta=Mensaje.objects.all()
      respuesta=Respuesta.objects.all()

      return render(request, 'Publico/foro.html',{'pregunta':pregunta, 'respuesta':respuesta})
     

def faq(request):

      from Administrador.models import Faq
      faq = Faq.objects.all()

      return render(request, 'Publico/faq.html', {'faq':faq})


def noticias(request):

      return render(request, 'Publico/noticias.html')


def noticia(request):

      return render(request, 'Publico/noticia.html')


def contacto(request):

      return render(request, 'Publico/contacto.html')

      
def acceso_registro(request):

      return render(request, 'Publico/acceso_registro.html')


def calendario(request):

      from Administrador.models import Calendario
      calendario = Calendario.objects.all()

      return render(request, 'Publico/calendario.html', {'calendario':calendario})

