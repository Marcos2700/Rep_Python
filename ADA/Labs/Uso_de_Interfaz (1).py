import datetime
import random
#Interfaz
class Estudiante:
    def __init__():
        pass

    def DeclarararDatosEstudiante(self, nombre, edad, domic, escuela, bach, promGen):
        self.nombre = nombre
        self.edad = edad
        self.domicilio = domic
        self.escuela = escuela
        self.bachiller = bach
        self.premedioGeneral = promGen

    def DeclararInteresIngreso(self, u, carrera, facultad, puntaje):
        self.universidad = u
        self.carreraAsp = carrera
        self.facultad = facultad
        self.puntosPrueba = puntaje
#Clase      
class Participante(Estudiante):
    def __init__(self, nombre, edad, domic, escuela, bach, promGen, u, carrera, facultad, puntaje, id, date):
        super().DeclarararDatosEstudiante(nombre, edad, domic, escuela, bach, promGen)
        super().DeclararInteresIngreso(u, carrera, facultad, puntaje)
        self.id = id
        self.fecha = date

    #Validar si el estudiante aprobo o reprobo
    def VerificarAprobacion(self):
        if self.puntosPrueba >= 900:
            return "Prueba de ingreso aprobada"
        else:
            return "Prueba de ingreso reprobada"

    #Crear dictionary con los atributos
    def __iter__(self):
        lista = []
        for atri, valor in self.__dict__.items():
            lista.append(valor)
        return lista

    #Verificar si los datos de la interfaz son datos vacios o no
    def Vacio(self):
        i = 0
        j = 0
        lista = self.__iter__()
        for x in range(len(lista)):
            if lista[x]:
                i += 1
        if i == len(lista):
            return "Objeto completo"
        else:
            return "Objeto vacio"

#Crear nombres aleatorios
def Nombres():
    nombre = ""
    apellido = ""
    nombres = ["Juan", "Pedro", "Michel", "Luisa", "Oscar", "Brenda"]
    apellidos = ["Osorio", "Perez", "Lopez", "Madrid", "Jimenez", "Kranick"]
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    return nombre+" "+apellido
#Bachiller aleatorio
def Bachiller():
    b =  ["B. en ciencias", "B. en comercio", "B. en humanidades", "B. en turismo", "B. en informatica", "Tecnico"]
    return random.choice(b)
#Promedio general aleatorio
def Promedio():
    return round(random.uniform(2,5),2)
#Puntaje aleatorio
def Puntaje():
    return random.randint(300, 2000)

#Imprimir informacion del estudiante
def Informacion(participante):
    for x, valor in participante.__dict__.items():
        print("{} : {}".format(x, valor))
    print("______________________________________________________________")

#PROGRAMA PRINCIPAL
part1 = Participante(Nombres(), 18, "Panama, El Dorado", "Instituto Nacional", Bachiller(), Promedio(), "UTP", "Ing. Industrial", "FII", Puntaje(), "156-eq", datetime.date.today())
part2 = Participante(Nombres(), 19, "Panama, Juan Diaz", "Instituto Jose Dolores Moscote", Bachiller(), Promedio(), "UTP", "Ing. en sistemas u computacion", "FISC", Puntaje(), "157-eq", datetime.date.today())
part3 = Participante(Nombres(), 18, "Panama, San Miguelito", "Instituto America", Bachiller(), Promedio(), "UTP", "Ing. Civil", "FIC", Puntaje(), "158-eq", datetime.date.today())

lista = [part1, part2, part3]

for x in range(0, len(lista)):
    print("Participante #", (x+1))
    Informacion(lista[x])