import random
#Clase empleado
class Empleado():
    idd = ""
    nombre = ""
    apellido = ""
    edad = 0
    cedula = ""
    direccion = ""
    salario = 0.0
    puesto = ""

    def __init__(self, idd, nom, ape, ed, ced, direc, salr, pu):
        self.idd = idd
        self.nombre = nom
        self.apellido = ape
        self.edad = ed
        self.cedula = ced
        self.direccion = direc
        self.salario = salr
        self.puesto = pu

    def InformacionDelEmpleado(self):
        print("Nombre: {} {} ".format(self.nombre, self.apellido))
        print("Cedula: ", self.cedula)

    def Supervisor(self):
        if(self.puesto == "Supervisor"):
            return True

#Clase administrativo
class Administrativo(Empleado):
    numOficina = ""
    numTelefono = ""
    
    def __init__(self, idd, nom, ape, ed, ced, direc, salr, pu, numOfic, numTel):
        super().__init__(idd, nom, ape,  ed, ced, direc, salr, pu)
        self.numOficina = numOfic
        self.numTelefono = numTel

#Clase tecnico
class Tecnico(Empleado):
    tipo = ""
    idUnidad = ""
    estado = ""

    def __init__(self, idd, nom, ape, ed, ced, direc, salr, pu, tipo, idUnid, estd):
        super().__init__(idd, nom, ape,  ed, ced, direc, salr, pu)
        self.tipo = tipo
        self.idUnidad = idUnid
        self.estado = estd

    def get_Estado(self):
        print("Estado actual del tecnico: ", self.estado)

    def set_Estado(self):
        self.estado = input("Indique el nuevo estado del tecnico --> ")

#Clase jefe
class Jefe(Empleado):
    adminAsignado = []
    numTelefono = ""
    nombreDespacho = ""
    tecsAsignados = []

    def __init__(self, idd, nom, ape,  ed, ced, direc, salr, pu, admAsig, numTel, nomDesp, tecs):
        super().__init__(idd, nom, ape,  ed, ced, direc, salr, pu)
        self.adminAsignado = list(admAsig)
        self.numTelefono = numTel
        self.nombreDespacho = nomDesp
        self.tecsAsignados = list(tecs)
          

    def get_Colaboradores(self):
        l = self.tecsAsignados + self.adminAsignado
        return l
      
      
    def get_Admin(self):
        return self.adminAsignado

#Asignar tecnicos
def AsignarTecs(lTecns, lAsignados):
    n = 0
    l = []
    while(n <3):
        x = random.choice(lTecns)
        if(not x in lAsignados):
            lAsignados.append(x)
            l.append(x)
            n += 1
    return l

#Imprimir informacion de los tecnicos
def Info_tecs(lTecs):
    for x in range(0, len(lTecs)):
        print("Tecnico #", (x+1))
        lTecs[x].InformacionDelEmpleado()
        print("Tipo: ", lTecs[x].tipo)
        print("ID de unidad: ", lTecs[x].idUnidad)
        print("Estado: ", lTecs[x].estado)
        print("")

#Imprimir Informacion de administrativos
def Info_administrativos(lAdms):
    for x in range(0, len(lAdms)):
        print("Administrativo #", (x+1))
        lAdms[x].InformacionDelEmpleado()
        print("Numero de oficina: ", lAdms[x].numOficina)
        print("")
        
#Imprirmir informacion de los jefes
def Info_jefes(lJefes):
    for x in range(0, len(lJefes)):
        print("Jefe #", (x+1))
        lJefes[x].InformacionDelEmpleado()
        lEmp = lJefes[x].get_Colaboradores()
        adminAsignado = list(lJefes[x].get_Admin())
        print("Administrativo asignado")
        adminAsignado[0].InformacionDelEmpleado()
        print("Informacion de todos los colaboradores a su cargo")
        for y in range(0, len(lEmp)):
            print("Empleado #", (y+1))
            lEmp[y].InformacionDelEmpleado()
            print("")
        print("")

#Programa principal
adm1 = Administrativo("ad-01", "Jorge", "Gonzalez", 37, "8-548-2014", "Panama, Juan Diaz, Calle 4", 950.35, "Supervisor", "Adm-546", "268-1578")
adm2 = Administrativo("ad-002", "Laura", "Huertas", 35, "8-456-123", "Panama, Loceria, Calle 25", 950.35, "Supervisor", "Adm-548", "268-4587")
tec1 = Tecnico("tec-001", "Juan", "Herrera", 25, "8-654-321", "La Chorrera, ave. Central", 756.25, "Soporte tecnico", "Sistemas", "it-01", "en caso")
tec2 = Tecnico("tec-002", "Esteban", "Murillo", 24, "8-634-541", "Panama, San Miguelito", 750.25, "Soporte", "infraestructura", "infra-01", "en espera")
tec3 = Tecnico("tec-003", "Hugo", "Leira", 23, "8-987-122", "Arraijan, Vacamonte", 750.25, "Soporte", "Infraestructura", "infra-01", "en espera")
tec4 = Tecnico("tec-004", "Melissa", "Guzman", 29, "8-487-785", "Panama, Villa Zaita", 756.25, "Mantenimiento", "Electrico", "elec-01", "en caso")
tec5 = Tecnico("tec-005", "Julio", "Urriola", 32, "8-741-852", "Panama, Pedregal", 756.25, "Soporte en redes", "Sistemas", "it-02", "en caso")
tec6 = Tecnico("tec-001", "Fabio", "Kranick", 27, "8-753-951", "Panama, Bethania", 850.25, "Software", "Sistemas", "it-03", "en espera")

lTecns = [tec1, tec2, tec3, tec4, tec5, tec6]
lAsignados =[]

lTecnsJf1 = AsignarTecs(lTecns, lAsignados)
lTecnsJf2 = AsignarTecs(lTecns, lAsignados)
adm1P =[]
adm2P =[]
adm1P.append(adm1)
adm2P.append(adm2)
lAdmins = adm1P + adm2P

jef1 = Jefe("jef-01", "George", "Moreno", 45, "8-159-357", "Panama, El Cangrejo", 1250.25, "Jefe", adm2P, "268-5287", "Asuntos Administativos", lTecnsJf1)
jef2 = Jefe("jef-02", "Ruben", "Diaz", 42, "8-138-792", "Panama, San Miguelito", 1250.25, "Jefe", adm1P, "268-5879", "Asuntos Tecnicos", lTecnsJf2)
lJefes = []
lJefes.extend([jef1, jef2])

print("*******Informacion de los tecnicos*********")
Info_tecs(lTecns)
print("////////////////////////////////////////////////////")
print("Informacion de los administrativos")
Info_administrativos(lAdmins)
print("////////////////////////////////////////////////////")
print("Informacion de los jefes")
Info_jefes(lJefes)

