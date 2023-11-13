part_max = int(input(" Por favor ingrese la cantidad de participantes -> "))
print("")
print(" El sistema ha sido configurado para aceptar",part_max," participantes a partir de ahora, el ordenador queda listo para recibirlos")
print("")

cant_part = 0

while(cant_part < part_max):
    nombre = input("Ingrese su nombre -> ")
    print("")
    email = input("Ingrese su email-> ")
    print("")
    print("Hola ",nombre," su email es ",email," desea confirmar la inscripción?")
    print("Para confirmar \"SI\", o escriba \"NO\" para rechazar")
    respuesta = input()
    respuesta = respuesta.lower()
    if respuesta == "si":
        print("")
        print("****************************************************")
        print("*Gracias, confirmamos su inscripción, lo esperamos!*")
        print("****************************************************")
        print("\n\n\n")
        print("SU NUMERO DE PARTICIPANTE ES: ", cant_part)
        cant_part += 1
    else:
        print("")
        print("*********************")
        print("*Operación cancelada*")
        print("*********************")

print("Cantidad máxima alcanzada")

"""
# LOOP FOR

part_max = int(input(" Por favor ingrese la cantidad de participantes -> "))
print("")
print(" El sistema ha sido configurado para aceptar",part_max," participantes a partir de ahora, el ordenador queda listo para recibirlos")
print("")

for x in range(part_max):
    nombre = input("Ingrese su nombre -> ")
    print("")
    email = input("Ingrese su email-> ")
    print("")
    print("Hola ",nombre," su email es ",email," desea confirmar la inscripción?")
    print("Para confirmar \"SI\", o escriba \"NO\" para rechazar")
    respuesta = input()
    respuesta = respuesta.lower()
    if respuesta == "si":
        print("")
        print("****************************************************")
        print("*Gracias, confirmamos su inscripción, lo esperamos!*")
        print("****************************************************")
        print("\n\n\n")
        print("SU NUMERO DE PARTICIPANTE ES: ",x)
    else:
        print("")
        print("*********************")
        print("*Operación cancelada*")
        print("*********************")

print("Cantidad máxima alcanzada")
"""