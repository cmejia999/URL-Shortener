from django.db import models
from .utils import create_shortened_url

# Create your models here.


class Shortener(models.Model):
    '''
    Crea una url corta basada en la larga
    created-> Hora y fecha en que se creo un acortador
    times_followed-> Veces en las que se ha seguido el enlace acortado
    url_long-> URL original
    url_short-> URL acortado https://domain/(short_url)
    '''
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)


'''
Importamos el modelo para iniciar, este modelo contiene toda la funcionalidad
que se necesita para crear un modelo Django.

Luego se definen todos los campos que tendra el modelo en la base de datos.
En el campo 'created' usamos la fecha y la hora que se crea el enlace abreviado
usamos 'auto_now_add=True' porque se quiere que el campo solo se modifique
cuando se cree la instancia.

'times_followed' refiere las veces que se ha utilizado la url abreviada
usamos PositiveIntegerField y le asignamos el valor de 0(cero), esto significa
que cada vez que sea creado el campo ese campo Django lo completara con 0(cero)

'url_long' se refiere a la URL que ingresa el usuario y es un campo URL.

'url_short' solo puede tener como maximo 15 caracteres, sera unico no puede haber
elementos repetidos.
'''

'''
Funcionalidad para generar un codigo aleatorio
Segunda funcionalidad obtener codigos aleatorios no repetido
Nos dirigimos a utils.py
'''
