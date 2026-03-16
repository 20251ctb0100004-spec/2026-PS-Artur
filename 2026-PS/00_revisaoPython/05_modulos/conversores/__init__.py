# conversores/__init__.py
# expoe a api publica do pacote

from .temperatura import celsius_para_fahrenheit, celsius_para_kelvin, kelvin_para_celsius
from .distancia import km_para_milhas, milhas_para_km, metros_para_pes


__all__ = [
    'celsius_para_fahrenheit', 'celsius_para_kelvin', 'kelvin_para_celsius',  
    'km_para_milhas', 'milhas_para_km', 'metros_para_pes',
]
