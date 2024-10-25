#Horas (id, fecha, hora, medico, personal, tipo, web, sobrecupo, estado)

import random

def generarTipo():
    tipo=["Consulta Medica","Pabellon"]
    return tipo[random.randint(0,len(tipo)-1)]
def generadorHoras():
    horas = str(random.randint(0, 23))
    if (len(horas) < 2):
        horas = "0" + horas
    horas += ":"

    minutos = str(random.randint(0, 59))
    if (len(minutos) < 2):
        minutos = "0" + minutos
    minutos += ":"

    segundos = str(random.randint(0, 59))
    if (len(segundos) < 2):
        segundos = "0" + segundos

    return horas + minutos + segundos


def sacarWeb(tipo):
    if (tipo == "Consulta Medica"):
        return bool(random.randint(0, 1))
    else:
        return 0

def definirsobrecupo(personal,medico):
    if(personal==medico):
        return bool(random.randint(0,1))
    else:
        return bool(0)


def generadorHora2(tuplas):

    arregloHoras = []
    medico=0
    for id in range(0, 109500):
        personal = random.randint(0, 19)
        fecha = tuplas[id][0]
        hora = tuplas[id][1]
        arregloHoras.append(Horas(id, tuplas[id][2], personal, hora, fecha))
        medico+=1
    return arregloHoras

def sacarestado(id):

    if(id>108000):
        return 0
    elif(id>109000):
        return 2
    else:
        return 1
class Horas:
    def __init__(self, id, medico,personal,hora,fecha):
        self.id=id
        self.fecha=fecha
        self.hora=hora
        self.medico=medico
        self.personal=personal
        self.tipo=generarTipo()
        self.web=bool(sacarWeb(self.tipo))
        self.sobrecupo=definirsobrecupo(self.personal,self.medico)
        self.estado=sacarestado(id)











