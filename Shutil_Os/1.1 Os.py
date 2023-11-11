import os
# print(os.getcwd())
# archivo = open('test.txt', 'w')
# archivo.write('Texto de testeo')
# archivo.close()

print(os.listdir())
ruta = 'C:\\Users\\ainfa\\Documents\\Python Total'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {ruta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arc in archivo:
        if arc.startswith('5'):
            print(f'\t{arc}')
    print('\n')