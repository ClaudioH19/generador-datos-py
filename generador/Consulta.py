#Consulta (id, id_hora, id_paciente, estado, id_contacto, procedimiento, apoyo)
import random

def procedimiento(id,pacientes,id_paciente):
    tipo=["Consulta con fonasa", "Consulta Particular", "Consulta sin Costo",
          "Pabellon Plan A", "Pabellon Plan B", "Pabellon Plan C", "Pabellon Plan D"]

    if(id<=7199):
        return tipo[random.randint(3,6)]
    else:
        if(pacientes[id%40000].prevision=="Fonasa"):
            if (random.randint(0, 50000) == 0):
                return tipo[2]
            else:
                return tipo[random.randint(0,1)]
        else:
            if(random.randint(0,50000)==0):
                return tipo[2]
            else:
                return tipo[1]


def verapoyo(proccedimiento, Hora):
    tipo = ["Consulta con fonasa", "Consulta Particular", "Consulta sin Costo",
            "Pabellon Plan A", "Pabellon Plan B", "Pabellon Plan C", "Pabellon Plan D"]
    if(proccedimiento==tipo[3] or proccedimiento==tipo[4] or proccedimiento==tipo[5] or proccedimiento==tipo[6]):
        while(True):
            apoyo=random.randint(-1,9)
            if(apoyo==-1):
                apoyo=chr(92)+"N"
            if(Hora.medico!=apoyo):
                return apoyo
    else:
        return chr(92)+"N"

def generadorConsulta(Horas,pacientes):
    consultas=[]
    cad = chr(92)+"N"
    for id in range(0,109000):
        if(id<108000):
            consultas.append(Consulta(id,id,id,Horas[id],pacientes))
        else:
            consultas.append(Consulta(id,id,id,Horas[id],cad))
    return consultas

def sacarestado():
    num=random.randint(0,1000)
    if(num==500):
        return 0
    else:
        return 1
#0->anulada, 1->no anulada
class Consulta:

    def __init__(self, id, id_hora,id_contacto,Hora,pacientes):
        cad = chr(92) + "N"
        self.id=id
        self.id_hora=id_hora
        if(pacientes==cad):
            self.id_paciente=cad
        else:
            self.id_paciente=pacientes[id%40000].rut
        self.estado=sacarestado()
        if(id<108000):
            self.id_contacto=id_contacto
        else:
            self.id_contacto =cad
        if(pacientes!=cad):
            self.procedimiento= procedimiento(self.id,pacientes,self.id_paciente)
            self.apoyo = verapoyo(self.procedimiento, Hora)
        else:
            self.procedimiento=cad
            self.apoyo= cad
