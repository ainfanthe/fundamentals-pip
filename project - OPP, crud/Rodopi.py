import sqlite3
from sqlite3 import Error #importa el manejo de errores
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

def conexionBD():
    try:
        con = sqlite3.connect('Base_Datos.db') #conexión al contenedor de la base de datos
        return con
    except Error:
        print(Error)

def cerrarBD(con):
    con.close()
miCon = conexionBD()
# Excepciones
def rec_act(con,id, id_un, campo):
    ''' Recibe un mensaje para solicitar identificador único, crea una lista de los 
        identificadores existentes, rectifica que el dato ingresado sea numérico
        y en caso de que el identificador a actualizar no exista, solicita nuevamente el 
        dato '''
    dato = actualizacion_datos(id)
    cursorObj = con.cursor()
    cursorObj.execute('SELECT '+id_un+' FROM '+campo) 
    filas = cursorObj.fetchall()
    if filas != []:
        while True:
            if (int(dato),) in filas:
                return dato
            else:
                print('El dato no existe, intenta nuevamente')
                dato = actualizacion_datos(id)
    else:
        return False

def rec_in(con,id, id_un, campo):
    ''' Recibe un mensaje para solicitar identificador único, crea una lista de los 
        identificadores existentes, rectifica que el dato ingresado sea numérico
        y en caso de que el identificador a actualizar no exista, solicita nuevamente el 
        dato '''
    dato = actualizacion_datos(id)
    cursorObj = con.cursor()
    cursorObj.execute('SELECT '+id_un+' FROM '+campo) 
    filas = cursorObj.fetchall()
    while True:
        if (int(dato),) not in filas:
            return dato
        else:
            print('El identificador único ya existe, intenta nuevamente')
            dato = actualizacion_datos(id)

def actualizacion_datos(entradas):
    ''' Recibe un mensaje para solicitar datos, lo "intenta" convertir en flotante para cersiorarse
        que el dato sea numérico o de lo contrario, lo solicita nuevamente.'''
    dato = input(entradas)
    while True:
        try:
            float(dato)
            return dato
        except:
            print('La entrada ingresada debe ser numérica')
            dato = input(entradas)

def comprobar_fecha(fecha_str):
    fecha_form = input(fecha_str)
    while True:
        try:
            datetime.strptime(fecha_form, '%d/%m/%Y').strftime('%d/%m/%Y')
            return fecha_form
        except ValueError:
            print("El formato debe ser DD/MM/AAAA, intenta nuevamente...")
            fecha_form = input(fecha_str)
# Datos
class datos:
    def insertar(self, con, tupla,tabla):
        try:
            cursorObj = con.cursor()
            while True:
                if len(tupla) == 9:
                    values = '(?,?,?,?,?,?,?,?,?)'
                elif len(tupla) == 6:
                    values = '(?,?,?,?,?,?)'
                elif len(tupla) == 4:
                    values = '(?,?,?,?)'
                ex = 'INSERT INTO '+ tabla +' VALUES '+values
                cursorObj.execute(ex, tupla)
                print('Añadido exitosamente')
                break
        except:
            print('No hay materias o estudiantes registrados')
        con.commit()


    def actualizar(self, con, tupla, tabla, dato):
        ''' Actualización: solictuplaita la entrada de la identificación y el dato por el cual se quiere actualizar el campo
            especificado, en esta situación, la calificación final obtenida por el estudiante; mediante la función UPDATE se realiza la actualización donde la identificación
            del estudiante coincida con la ingresada'''
        cursorObj = con.cursor()
        cursorObj.execute('UPDATE ' + tabla +'  SET ' +dato+ '= "' + tupla[0]  + '" WHERE '+ tupla[1])
        print(f'El dato a sido actualizado a: {tupla[0]}')
        con.commit()

    def consultar(self, con, tabla, dato):
        ''' Solicita entrada del identificador único, mediante la función SELECT realiza la consulta con la base
            de datos, mediante es * trae todos los campos en forma de lista registrados con el identificador único 
            ingresado y recorre la lista imprimiendo la información con el formato establecido'''
        cursorObj = con.cursor()
        consulta = rec_act(con,"Código o identificación: ", dato, tabla)
        if consulta == False:
            return print('La tabla no contiene datos para consultar')
        cursorObj.execute('SELECT * FROM ' + tabla +' WHERE ' + dato + ' ="' + consulta + '"')
        consultaTB = cursorObj.fetchall()
        contador = 1
        print(f'Información de {consultaTB[0][1]}:')
        print(" ")
        for row in consultaTB[0]:  
            print(str(contador), '. ', row)
            contador += 1
# Materias
class materias(datos):

    def __init__(self):
        self.__codigo = None
        self.__nombre = None
        self.__facultad = None
        self.__departamento = None
        self.__creditos = None
        self.__idioma = None

    def crearTbMat(self, con):
        ''' Crea la tabla en caso de que no exista, especificando los campos contenidos en la misma y el tipo de dato,
            La función "PRIMARY KEY" permite especificar cuál campo será el identificador único '''
        cursorObj = con.cursor()
        cursorObj.execute('CREATE TABLE IF NOT EXISTS materias(codigo integer PRIMARY KEY, nombre text, facultad text, departamento text, creditos integer, idioma text)')
        con.commit()

    def setMat(self,con):
        self.__codigo = rec_in(con,'Código: ', 'codigo', 'materias')
        self.__nombre = input('Nombre: ')
        self.__facultad = input('Facultad: ')
        self.__departamento = input('Departamento: ')
        self.__creditos = actualizacion_datos('Créditos: ')
        self.__idioma = input('Idioma: ')
        materia = (self.__codigo, self.__nombre, self.__facultad, self.__departamento, self.__creditos, self.__idioma)
        return materia

    def setupdate(self,con):
        self.__codigo = rec_act(con,'Código de la materia a actualizar: ', 'codigo', 'materias')
        if self.__codigo == False:
            return print('La tabla no contiene datos para consultar')
        self.__idioma = input('Actualizar el idioma en que se dicta: ')
        tupla = (self.__idioma, 'codigo = "'+ self.__codigo +'"')
        return tupla
    
# Estudiantes
class estudiante(datos):

    def __init__(self):
        self.__identificacion = None
        self.__nombre = None
        self.__apellido = None
        self.__carrera = None
        self.__nacimiento = None
        self.__ingreso = None   
        self.__procedencia = None
        self.__correo = None
        self.__matriculas = None  

    def crearTbEst(self, con):
        cursorObj = con.cursor()
        cursorObj.execute('CREATE TABLE IF NOT EXISTS estudiante(identificacion integer PRIMARY KEY, nombre text, apellido text, carrera text, fch_nacimientto text, fch_ingreso text, procedencia text, correo text, cant_matriculas integer)')
        con.commit()

    def setEst(self,con):
        self.__identificacion = rec_in(con,'Identificación: ', 'identificacion', 'estudiante')
        self.__nombre = input('Nombres: ')
        self.__apellido = input('Apellidos: ')
        self.__carrera = input('Carrera: ')
        self.__nacimiento = comprobar_fecha('Fecha nacimiento (DD/MM/AAAA): ')
        self.__ingreso = comprobar_fecha('Fecha ingreso (DD/MM/AAAA): ')
        self.__procedencia = input('ciudad de procedencia: ')
        self.__correo = input('E-mail: ')
        self.__matriculas = actualizacion_datos('Matrículas: ')
        estudiante = (self.__identificacion, self.__nombre, self.__apellido, self.__carrera, self.__nacimiento, self.__ingreso, self.__procedencia, self.__correo, self.__matriculas)
        return estudiante

    def setupdate(self,con):
        self.__identificacion = rec_act(con,'Identificación del estudiante a actualizar: ','identificacion', 'estudiante')
        if self.__identificacion == False:
            return print('La tabla no contiene datos para actualizar')
        self.__matriculas = actualizacion_datos('Actualizar cantidad de matrículas efectuadas: ')
        tupla = (self.__matriculas, 'identificacion = "'+ self.__identificacion +'"')
        return tupla

# Historia academica
class historia_académica(datos): # La clase obtiene como parametros los datos en función de lo digitado en la clase datos;
    # Creación tipo de dato historia_académica

    def __init__(self): # Se adiciona el método constructor __init__ adicionando el parametro especial self
        self.__codigo = None
        self.__identificacion = None
        self.__notaFinal = None
        self.__creditosCursados = None

    def crearTbCal(self, con):# Se llama al parametro self de la clase que emplea el metodo constructor junto al con (conexión a la base de datos)
        ''' Todas las funciones creas funcionan del modo explicado anteriormente
            NOTA = mediante la función CONSTRAINT se genera la restricción de clasificar tanto al codigo como la identificacion
                como llaves primarias o identificadores únicos'''
        cursorObj = con.cursor()
        cursorObj.execute('CREATE TABLE IF NOT EXISTS calificaciones (codigo integer, identificacion integer, nota_final text, creditos_cursados text, CONSTRAINT id PRIMARY KEY(codigo, identificacion))')
        con.commit()

    def setCalIDs(self,con):
        cursorObj = con.cursor()
        cursorObj.execute('SELECT codigo, identificacion FROM calificaciones') # El * me trae todos los campos
        cods = cursorObj.fetchall()
        self.__codigo = rec_act(con,'Código: ', 'codigo', 'materias')# Se obtienen datos digitados de la clase que emplea el metodo constructor y se asignan a la función rec_act
        if self.__codigo == False:
            return print('La tabla no contiene datos')
        self.__identificacion = rec_act(con,'ID: ', 'identificacion', 'estudiante')
        tup = (int(self.__codigo), int(self.__identificacion))
        while True:
            if tup in cods:
                return (self.__codigo, self.__identificacion)
            else:
                print('El dato no existe, intenta nuevamente')
                self.__codigo = rec_act(con,'Código: ', 'codigo', 'materias')
                if self.__codigo == False:
                    return print('La tabla no contiene datos para consultar')
                self.__identificacion = rec_act(con,'ID: ', 'identificacion', 'estudiante')
                tup = (int(self.__codigo), int(self.__identificacion))

    def setCal(self,con):
        cursorObj = con.cursor()
        cursorObj.execute('SELECT codigo, identificacion FROM calificaciones') # El * me trae todos los campos
        cods = cursorObj.fetchall()
        self.__codigo = rec_act(con,'Código: ', 'codigo', 'materias') # Se obtienen datos digitados de la clase que emplea el metodo constructor
        # Se le otorga formato de salida empleando la función rec_act
        if self.__codigo == False:
            return None
        self.__identificacion = rec_act(con,'ID: ', 'identificacion', 'estudiante')
        if self.__identificacion == False:
            return None
        tup = (int(self.__codigo), int(self.__identificacion))
        while True:
            if tup not in cods:
                break
            else:
                print('El identificador único ya existe, intenta nuevamente')
                self.__codigo = rec_act(con,'Código: ', 'codigo', 'materias')
                if self.__codigo == False:
                    return None
                self.__identificacion = rec_act(con,'ID: ', 'identificacion', 'estudiante')
                if self.__codigo == False:
                    return None
                tup = (int(self.__codigo), int(self.__identificacion))
        self.__notaFinal = actualizacion_datos('Nota final: ') # Se obtiene el dato de la nota final, y se imprime realizando un llamado a la función actualizacion_datos
        self.__creditosCursados = actualizacion_datos('Creditos cursados: ')
        hist = (self.__codigo, self.__identificacion, self.__notaFinal, self.__creditosCursados)
        return hist

    def setupdate(self,con):
        IDs = self.setCalIDs(con)
        self.__notaFinal = actualizacion_datos('Actualizar nota final a: ')
        tupla = (self.__notaFinal, 'codigo = "'+ IDs[0] +'" and identificacion = "'+ IDs[1] +'"')
        return tupla

    def consultarCal(self, con):
        ''' Consulta: solicita entrada de la identificación + el identificador unico de la materia, mediante la función SELECT realiza la consulta con la base
            de datos, mediante el * trae todos los campos en forma de lista registrados con el identificador único 
            ingresado y recorre la lista imprimiendo la información con el formato establecido'''
        cursorObj = con.cursor()
        IDs = self.setCalIDs(con)
        cursorObj.execute('SELECT * FROM calificaciones WHERE codigo = "'+ IDs[0] +'" AND identificacion = "'+ IDs[1] +'"') #el * me trae todos los campos
        consulta = cursorObj.fetchall()
        print(f'Información de {consulta[0][1]}:')
        print(" ")
        contador = 1
        for row in consulta[0]:  
            print(str(contador), '. ', row)
            contador += 1 # El contador enlistará cada uno de los elementos a imprimir en la consulta

    def eliminarCal(self, con):
        ''' Solicita los datos de identificadores únicos (codigo, identificacion) y realiza el borrado 
            de la información en donde los campos de indentificacion y codigo concuerden con los ingresados'''
        cursorObj = con.cursor()
        cod = rec_act(con,'Código: ', 'codigo', 'materias') # Se obtienen datos digitados de la clase que emplea el metodo constructor
        if cod == False:
            return print('No hay materias registradas')
        id = rec_act(con,'ID: ', 'identificacion', 'estudiante')
        if id == False:
            return print('No hay estudiantes registrados')
        cursorObj.execute('DELETE FROM calificaciones WHERE codigo = "'+ cod +'" and identificacion = "'+ id +'"')
        print('Eliminado exitosamente')
        con.commit()
        
# Clasificacion
class clasificacion:  # Creación tipo de dato clasificación

    def crearTbHistAcademica(self, con): # Se llama al parametro self, y asimismo la conexión a la base de datos
        cursorObj = con.cursor()
        cursorObj.execute('CREATE TABLE IF NOT EXISTS historia_academica (identificacion integer, nombre text, apellido text, mat_cursadas text, creditos_acum text, promedio_est text, CONSTRAINT id FOREIGN KEY (identificacion) REFERENCES estudiante(identificacion), CONSTRAINT id2 UNIQUE(identificacion))')
        con.commit()

    def borrarTb(self,con):
        ''' Crea la tabla en caso de que no exista, especificando los campos contenidos en la misma y el tipo de dato,
            La función "PRIMARY KEY" permite especificar cuál campo será el identificador único '''
        cursorObj = con.cursor()
        cursorObj.execute('DROP TABLE  historia_academica')
        con.commit()

    def promedio(self, con, identificacion): # Se llama al parametro identificacion que contendrá un tipo de dato para ser empleado en la ejecución posteriormente
        ''' Recibe como parámetro una identificacion y mediante la función "count" realiza el conteo de las notas finales
            con el mismo identificador único, en este caso, la identificación. Posteriormente mediante la función
            "sum" realiza la sumatoria de las notas finales con la misma identificación y finalmente guarda el 
            cálculo de la sumatoria de las notas finales dividido la cantidad de materias en la variable promedio
            y retorna este valor '''
        cursorObj = con.cursor()
        identificacion = str(identificacion) # Se realiza la conversión a tipo de dato string (caracteres)
        cursorObj.execute('SELECT count(nota_final) FROM calificaciones WHERE identificacion = "'+ identificacion +'"')
        cantmat = cursorObj.fetchall()
        cursorObj.execute('SELECT sum(nota_final) FROM calificaciones WHERE identificacion = "'+ identificacion +'"')
        suma = cursorObj.fetchall()
        promedio = suma[0][0]/cantmat[0][0]
        return promedio

    def creditosacum(self, con, identificacion):
        ''' Recibe como parámetro una identificacion y mediante la función "sum" realiza la consulta de la sumatoria
            de los créditos cursados con el mismo identificador único y retorna la cantidad de créditos acumulados'''
        cursorObj = con.cursor()
        identificacion = str(identificacion)
        cursorObj.execute('SELECT sum(creditos_cursados) FROM calificaciones WHERE identificacion = "'+ identificacion +'"')
        suma = cursorObj.fetchall()
        return suma[0][0]

    def cantmaterias(self, con, identificacion):
        ''' Recibe como parámetro una identificacion y mediante la función "count" realiza la consulta del conteo
            de las notas finales con el mismo identificador único y retorna la cantidad de materias cursadas'''
        cursorObj = con.cursor()
        identificacion = str(identificacion)
        cursorObj.execute('SELECT count(nota_final) FROM calificaciones WHERE identificacion = "'+ identificacion +'"')
        cantmat = cursorObj.fetchall()
        return cantmat[0][0]

    def insertarHistAcademica(self, con):
        ''' Realliza la consulta de identificación, nombre y apellido de la tabla estudiantes al igual que la consulta
            de identificación de la tabla calificaciones y crea una lista con estos datos, de este modo, se recorre 
            la lista de ids y si el estudiante no tiene calificaciones (no está en la lista _lista_ ), pasa a la siguiente 
            iteración, de lo contrario, se almacenan los datos de identificación, nombre, apellido, mat_cursadas
            (haciendo uso de la función cantmaterias) , creditos_acum (función creditosacum) y promedio_est (función 
            promedio) y se añade todo a una tupla para posteriormente insertar los valores en la tabla '''
        cursorObj = con.cursor()
        cursorObj.execute('SELECT identificacion, nombre, apellido FROM estudiante ')
        ids = cursorObj.fetchall()
        cursorObj.execute('SELECT identificacion FROM calificaciones ')
        ids_cal = cursorObj.fetchall()
        lista = []
        for i in ids_cal:
            lista.append(i[0])
        for row in ids:
            if row[0] not in lista:
                continue
            identificacion = int(row[0])
            nombre = row[1]
            apellido = row[2]
            mat_cursadas = self.cantmaterias(con,row[0])
            creditos_acum = self.creditosacum(con,row[0])
            promedio_est = self.promedio(con,row[0])
            hist_academica = (identificacion, nombre, apellido, mat_cursadas, creditos_acum, promedio_est)
            cursorObj.execute('''INSERT OR IGNORE INTO historia_academica VALUES(?,?,?,?,?,?)''', hist_academica)
            cursorObj.execute('UPDATE historia_academica SET mat_cursadas = "' + str(mat_cursadas) + '", creditos_acum = "' + str(creditos_acum) + '", promedio_est = "' + str(promedio_est) + '" WHERE identificacion = "'+ str(identificacion) +'"')
        con.commit()
        
    def consultarHistAcademica(self, con):
        ''' Consulta: solicita entrada de la identificación + el identificador unico de la materia, mediante la función SELECT realiza la consulta con la base
            de datos, mediante el * trae todos los campos en forma de lista registrados con el identificador único 
            ingresado y recorre la lista imprimiendo la información con el formato establecido'''
        cursorObj = con.cursor()
        cursorObj.execute('SELECT * FROM historia_academica')
        return cursorObj.fetchall()

def consultar(conexion):
    ventana.tblClasificacion.setRowCount(0)
    #ventana.pushButton.clicked.connect(salirVentana)
    indiceControl = 0 # Establecemos contador a fin de evaluar el número de indices necesarios para ser impresos

    cursor = conexion.cursor()                         # Crea un cursor
    cursor.execute('SELECT * FROM historia_academica')
    clasificacion = cursor.fetchall()
    '''Realizamos conexión desde el objeto clasificacion, y mediante un loop se ejecuta lectura de lo extraido por el objeto cursor, asimismo, lo imprimimos en función del indice establecido'''
    '''indiceControl, [posición de columna en interfaz], QTableWidgetItem(str(item[posición de columna en base de datos]))'''
    for item in clasificacion:
        ventana.tblClasificacion.setRowCount(indiceControl + 1)
        ventana.tblClasificacion.setItem(indiceControl,0, QTableWidgetItem(str(item[0]))) # Posición de la columna ID [indíce 0 en BD] en primera columna de la interfaz [indíce 0, también]
        ventana.tblClasificacion.setItem(indiceControl,1, QTableWidgetItem(str(item[1]))) #////
        ventana.tblClasificacion.setItem(indiceControl,2, QTableWidgetItem(str(item[2]))) #////
        ventana.tblClasificacion.setItem(indiceControl,3, QTableWidgetItem(str(item[3]))) #////
        ventana.tblClasificacion.setItem(indiceControl,4, QTableWidgetItem(str(item[4]))) #////
        ventana.tblClasificacion.setItem(indiceControl,5, QTableWidgetItem(str(item[5]))) #////

        indiceControl += 1 # Suma al contador por cada indíce enlistado en BD

def window(con):
    global ventana
    '''No se ha visto necesaria la conversión de .ui a .py empleando pyuic5'''
    aplicacion = QtWidgets.QApplication([])
    ventana = uic.loadUi("ventana.ui") # Carga de la interfaz .ui junto con sus propiedades
    ventana.show() # Lanzamiento de la interfaz
    consultar(con)

    '''Se establecen estilos y/o formas a la información empleando sintaxis propia del lenguaje de diseño CSS en la interfaz.
    Mediante setters al objeto tblClasificacion se otorgan los criterios a estilizar en las clases QTableWidget [tabla general], QTableView::item [celdas], y QHeaderView [celdas de encabezado]
    en la interfaz <ventana.ui>'''
    ventana.tblClasificacion.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellido', 'Materias', 'Créditos', 'Promedio']) #denominación de encabezado a cada columna
    ventana.tblClasificacion.setEditTriggers(QTableWidget.NoEditTriggers) # Inhabilita la edición de información
    ventana.tblClasificacion.setSortingEnabled(True) # Permite intercalar el orden de presentación [ascendente, descendente, etcétera] desde encabezado de columna
    ventana.tblClasificacion.setStyleSheet('''QTableWidget{color:black; border: 3px double black; padding:5px; border-radius: 10px} 
    QTableView::item::hover{background:black;color:white}''') # Establecemos diseño en la interfaz empleando lenguaje propio de estilo en cascada (CSS)
    #ventana.tblClasificacion.horizontalHeader().setStyleSheet("color:red"); | línea de prueba
    ventana.label_2.setStyleSheet('''background-color:black;color:white; border-radius: 10px; border: 4px double black''')
    ventana.tblClasificacion.horizontalHeader().setStyleSheet('''QHeaderView::section {background-color:black; color:white;}''')#Encabezado columnas hoja de estilo
    #ventana.tblClasificacion.horizontalHeader().setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) | línea de prueba
    ventana.tblClasificacion.verticalHeader().setStyleSheet('''QHeaderView::section {background-color:black; color:white;}''')#Encabezado filas hoja de estilo
    ventana.tblClasificacion.setGridStyle(QtCore.Qt.DashDotLine) #DashDotLine [.-.-.] en estilo de grid | celdas
    aplicacion.exec()
'''
def salirVentana(self):
    sys.exit()
'''

def menu(con):
    while True: # Crea un bucle infinito
        opcion = int(actualizacion_datos('''

==.:Menú principal:.==
======================
[1] - Materia
[2] - Estudiante
[3] - Historia A.
[4] - Clasificación
[5] - Finalizar
======================
Seleciona una opción >>:  '''))
        if opcion <1 or opcion >5: 
            print("Opción incorrecta, intenta nuevamente...") 
            # Valida la entrada de opción viendo que esté entre el rango de menus posibles
        elif opcion == 1:
            ma = materias()
            while True:
                opcion = int(actualizacion_datos('''

   ==.:Materia:.==
======================
[1] - Añadir materia
[2] - Consultar
[3] - Actualizar
[4] - Volver al principal
======================
Seleciona una opción >>:  '''))
                if opcion < 1 or opcion > 4:
                    print("Opción incorrecta, intenta nuevamente...")
                    # Valida la entrada de opción viendo que esté entre el rango de menus posibles
                elif opcion == 1:
                    ma.insertar(miCon,ma.setMat(miCon),'materias')
                elif opcion == 2:
                    ma.consultar(miCon,'materias','codigo')
                elif opcion == 3:
                    ma.actualizar(miCon,ma.setupdate(miCon),'materias','idioma')
                elif opcion == 4:
                    break
        elif opcion == 2:
            es = estudiante()
            while True:
                opcion = int(actualizacion_datos('''

  ==.:Estudiante:.==
======================
[1] - Añadir estudiante
[2] - Consultar
[3] - Actualizar
[4] - Volver al principal
======================
Seleciona una opción >>:  '''))
                if opcion < 1 or opcion > 4:
                    print("Opción incorrecta, intenta nuevamente...")
                elif opcion == 1:
                    es.insertar(miCon,es.setEst(miCon),'estudiante')
                elif opcion == 2:
                    es.consultar(miCon,'estudiante','identificacion')
                elif opcion == 3:
                    es.actualizar(miCon,es.setupdate(miCon),'estudiante','cant_matriculas')
                elif opcion == 4:
                    break
        elif opcion == 3:
            ha = historia_académica()
            while True:
                opcion = int(actualizacion_datos('''

  ==.:Historia A:.==
======================
[1] - Añadir historia
[2] - Consultar
[3] - Borrar materia
[4] - Actualizar nota
[5] - Volver al principal
======================
Seleciona una opción >>:  '''))
                if opcion < 1 or opcion > 5:
                    print("Opción incorrecta, intenta nuevamente...")
                elif opcion == 1:
                    ha.insertar(miCon,ha.setCal(miCon),'calificaciones')
                elif opcion == 2:
                    ha.consultarCal(miCon)
                elif opcion == 3:
                    ha.eliminarCal(miCon)
                elif opcion == 4:
                    ha.actualizar(miCon,ha.setupdate(miCon),'calificaciones','nota_final')
                elif opcion == 5:
                    break

        elif opcion == 4:
            cl = clasificacion()
            cl.borrarTb(miCon)
            cl.crearTbHistAcademica(miCon)
            cl.insertarHistAcademica(miCon)
            window(miCon) # Conecta a la BD, extrae los datos en tablas almacenados en la variable clas, y los exporta con el orden asignado en la variable ord


        elif opcion == 5:
            cerrarBD(con)
            break
def main(): 
    es = estudiante()
    ma = materias()
    ha = historia_académica()
    cl = clasificacion()
    es.crearTbEst(miCon)
    ma.crearTbMat(miCon)
    ha.crearTbCal(miCon)
    cl.crearTbHistAcademica(miCon)

main()
menu(miCon)


