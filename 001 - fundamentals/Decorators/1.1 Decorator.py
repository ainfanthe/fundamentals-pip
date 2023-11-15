# Decoradores: funciones que modifican el comportamiento de otras
# Permite complementar el código de una función con el código de otra

# def changeLetter(typeL):
#     def mayus(texto):
#         print(texto.upper())

#     def minus(texto):
#         print(texto.lower())

#     if typeL == 'may':
#         return mayus
#     elif typeL == 'min':
#         return minus

# op = changeLetter('may')
# op('Palabra')

def decorarSaludo(funcion):
    def otraFuncion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otraFuncion

# @decorarSaludo
def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayusculaDecorada = decorarSaludo(mayusculas)
mayusculaDecorada('Palabra')