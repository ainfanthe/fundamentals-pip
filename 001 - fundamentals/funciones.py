#función simple
def calcula():
    calculo = 43 * 12 * 80
    calculo = calculo / 7
    coeficiente = 45 * 3.1416
    calculo = calculo * coeficiente
    calculo = "El resultado es -> " + str(calculo)
    print(calculo)

# función recibe parámetros
def calcula_valor(mensaje, numero1, numero2):
    resultado = numero1 + numero2
    print(mensaje + str(resultado))


# función recibe y devuelve parámetros
def calcula_valor_2(numero1, numero2, comando):
    if comando=="-":
        resultado = numero1 - numero2
    if comando=="+":
        resultado = numero1 + numero2

    return resultado

res1 = calcula_valor_2(10,100,"+")

print(res1)








