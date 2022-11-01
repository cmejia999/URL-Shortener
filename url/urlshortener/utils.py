from django.conf import settings
from random import choice
from string import ascii_letters, digits

# Intenta obtener el valor del módulo de configuración
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAILABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAILABLE_CHARS):
    # Crea una cadena aleatoria con el tamaño predeterminado
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


'''
getattr() es una función incorporada que permite obtener
el valor de un atributo indicando su nombre como una cadena.
'''


def create_shortened_url(model_instance):
    random_code = create_random_code()
    # Obtiene la clase de modelo

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)
    return random_code


'''
La función toma como argumento una instancia del modelo "Acortador". 
Primero, la función genera un código aleatorio usando el 
create_random_code. Entonces se pone el modelo clase y comprueba 
si hay algún otro objeto que tenga el mismo short_url. Si lo hace, 
se ejecuta solo una vez más, pero si todo está bien, devuelve el 
código_aleatorio.
'''
