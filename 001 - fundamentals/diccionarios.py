paciente1 = {"nombre":"Juan", "edad":42, "peso":70.5, "fuma":True, "clin":"Gripe"}
paciente2 = {"nombre":"Pedro", "edad":23, "peso":60.5, "fuma":False, "clin":"Resfrío"}
paciente3 = {"nombre":"Julia", "edad":13, "peso":50.5, "fuma":False, "clin":"Resfrío"}

pacientes = [paciente1,paciente2,paciente3]

demo = ['uno','dos','tres','cuatro','ultimo']

for x in range(len(pacientes)):
        print("")
        print("--------------------")
        print("- DICCIONARIO Nº",x+1,"-")
        print("--------------------")
        print("CLAVE\t\tVALOR\t\t<33\t\t\n")


        for clave, valor in pacientes[x].items():
                menor=""
                if (clave == "edad" and valor < 33):  
                        menor = "✅"
                print(clave,"\t\t",valor,"\t\t",menor)
                
                









"""
for clave, valor in paciente1.items():
    print("Clave -> ",clave," | Valor -> ",valor)
    print("**********************************\n")
    if (clave == "edad" and valor < 33):
        print("Encontramos un paciente con menos de 33")

"""





"""
for clave, valor in paciente1.items():
    print("Llave -> ",clave,"Valor -> ",valor)
"""


