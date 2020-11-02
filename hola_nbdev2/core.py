# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'HelloSayer', 'startsWithDateAndTime', 'FindAuthor']

# Cell
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# Cell
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)

# Cell
# Inicio con fecha y hora
def startsWithDateAndTime(s):
    pattern = '^([0-9])+/([0-9])+/([0-9])+ ([0-9])+:([0-9])+ -'
    result = re.match(pattern, s)
    if result:
        return True
    return False

# Cell
def FindAuthor(s):
    patterns = [
        '([\w]+):',                        # Nombre
        '([\w]+[\s]+[\w]+):',              # Nombre y apellido
        '([\w]+[\s]+[\w]+[\s]+[\w]+.*):',  # Nombre + 2 apellidos
        '(\+52 1 \d{3} \d{3} \d{4}):',     # Número telefónico (México)
        '([\w]+)[\u263a-\U0001f999]+:',    # Nombre y emoji
        '([\w]+[\s]+[0-9]+):'              # Nombre genérico
    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False