from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Shortener

from .forms import ShortenerForm
# Create your views here.

'''
Hay dos vistas para la aplicación de acortador de URL:

Vista de inicio: Esto muestra el formulario abreviado y la nueva URL si el formulario ya se ha enviado.
Vista de redireccionamiento: Esto redirige a la URL larga y agrega 1 a los tiempos seguidos.
'''


def home_view(request):
    template = 'urlshortener/home.html'

    context = {}

    # Formulario vacio
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri(
                '/') + shortened_object.short_url
            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


'''
Cuando el metodo HTTP es igual a GET se pasa como contexto la forma shortener
utilizada para crear los objetos cortos
Cuando el metodo HTTP es POST igual se pasa el formulario contexto
para que el usuario pueda ingresar la URL, pero esta pasando la solicitud a 
otro formulario que es el formuario utilizado
'''

# Vista de redireccionamiento


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()

        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Sorry this link is broken')


'''
'''
