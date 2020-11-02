# Análisis de texto 
> Análisis de un grupo de WhatsApp


```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


This file will become your README and also the index of your documentation.

## Install

`pip install hola_nbdev2`

## How to use

Algunos ejemplos:

#### startsWithDateAndTime
Verifica si la el texto inicia con fecha y hora

```python
x = '01/10/18 19:18 - Señora 5: Claudia, puedes reenviar los paquetes, por favor? 🙏🏼 Aún no estaba en el grupo'
startsWithDateAndTime(x)
```




    True



#### startsWithDateAndTime
Encuentra al autor del mensaje si está en alguno de estos formatos
- Nombre
- Nombre y apellido
- Nombre + 2 apellidos
- Número telefónico (México)
- Nombre y emoji
- Nombre genérico
