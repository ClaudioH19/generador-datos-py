import random
from FechaHoraTree import *
from pacienteTree import *
import re
import math

nombresazar=["juan","maria","antonio","catalina","sofia","jaime","pablo","mateo","benjamin","rodrigo",
             "matias","bastian","camila","fernando","fernanda","renato","francisca","francisco","renata"
             ,"claudio","claudia","alexander","macarena"]

apellidos=["mino","hernandez","martinez","aguilera","salazar","munoz","garrido","valdes","salas","soto","donoso","faundez",
           "diaz","mendoza","lopez","rojas","chacon","retamal","guerrero","campos","saavedra","garcia"]

vocales=["a","e","i","o","u"]
lodemas=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]




def generadorDirec():
    
    av=["avenida","calle","pasaje","callejon","villa"]
    cadena=""
    
    cadena+=av[random.randint(0,4)]+" "
    
    for i in range(0, random.randint(1,7)):
        cadena+=lodemas[random.randint(0,20)]
        cadena+=vocales[random.randint(0,4)]
    
    cadena+=" "
    
    for i in range(0,random.randint(1,3)):
        cadena=cadena+str(random.randint(0,9))
    return cadena


def generadorPrev():
    if random.randint(0,1)>=1:
        return "Fonasa"
    else:
        return "Isapre"



def generadorPaciente():
    arregloPaciente = []
    data = generarData()
    for i in range(0, 40000):
        arregloPaciente.append(Paciente(data[i][0],data[i][1],data[i][2]))

    return arregloPaciente


class Paciente:
    def __init__(self,rut,telefono,correo):
        self.rut=rut
        self.nombre=nombresazar[random.randint(0,22)]
        self.apellido_p=apellidos[random.randint(0,21)]
        self.apellido_m=apellidos[random.randint(0,21)]
        self.telefono=telefono
        self.correo=correo
        self.direccion=generadorDirec()
        self.prevision=generadorPrev()
        self.fecha_n=generadorFecha(1)
        self.fecha_reg=generadorFecha(0)