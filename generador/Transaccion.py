#Transacciones (id, id_personal, id_consulta, monto, estado, mediopago, boleta,
#bono, váucher)
#Tres tipos de consultas:
#1. Consulta con costo Fonasa = $18.500
#2. Consulta con costo particular = $47.000
#3. Consulta sin costo.
#o Cuatro tipos de pabellones:
#1. Plan A: $800.000
#2. Plan B: $670.000
#3. Plan C: $550.000
#4. Plan D: $500.000
import random


def encontrarPorcentaje(personal,encontrarId):
    for i in personal:
        if(i.id == encontrarId):
            return i.porcentaje

def montoPagar(medico,consulta,personal):
    tipo = ["Consulta con fonasa", "Consulta Particular", "Consulta sin Costo",
            "Pabellon Plan A", "Pabellon Plan B", "Pabellon Plan C", "Pabellon Plan D"]

    cadena=chr(92)+"N"
    Pagar=0
    if(consulta.procedimiento==tipo[0] and medico.fonasa==True):
        Pagar=18500


    elif(consulta.procedimiento==tipo[0] and medico.fonasa==False):
        Pagar=47000

    elif (consulta.procedimiento == tipo[1]):
        Pagar = 47000

    elif (consulta.procedimiento == tipo[2]):
        Pagar = 0

    elif(consulta.procedimiento==tipo[3]):
        Pagar = 800000



    elif(consulta.procedimiento==tipo[4]):
        Pagar=670000



    elif(consulta.procedimiento==tipo[5]):
        Pagar=550000


    elif(consulta.procedimiento==tipo[6]):
        Pagar=500000


    return Pagar




def MedioPago(hora):
    tipo=["Credito","Debito","Efectivo"]
    if(hora.web==False):
        return tipo[random.randint(0,2)]
    else:
        return tipo[random.randint(0, 1)]


def vaucher(medioPago,id):
    tipo = ["Credito", "Debito", "Efectivo"]
    if(medioPago==tipo[0] or medioPago==tipo[1]):
        return generarNum(id)
    else:
        return chr(92)+"N"
def generarNum(id):
    ruido=random.randint(0,1000000)
    numTicket=str(id)+str(ruido)

    return int(numTicket)


def boleta(medico,consulta,id):
    tipo = ["Consulta con fonasa", "Consulta Particular", "Consulta sin Costo",
            "Pabellon Plan A", "Pabellon Plan B", "Pabellon Plan C", "Pabellon Plan D"]
    if(consulta.procedimiento!=tipo[0] and consulta.procedimiento!=tipo[1]):
        return generarNum(id)
    else:
        return chr(92)+"N"
def bono(medico,consulta,id):
    tipo = ["Consulta con fonasa", "Consulta Particular", "Consulta sin Costo",
            "Pabellon Plan A", "Pabellon Plan B", "Pabellon Plan C", "Pabellon Plan D"]
    if(consulta.procedimiento==tipo[0] and medico.fonasa==True):
        return generarNum(id)
    else:
        return chr(92)+"N"

def devolverMedico(id, personal):
    for i in personal:
        if(id==i.id):
            return i

def sacarestado(consulta):
    if(consulta.estado==0):
        return False
    else:
        return True


def generadorTransaccion(consultas,personal,horas):
    transacciones=[]
    contId=0
    for id in range(0,108000):
        monto=montoPagar(devolverMedico(horas[id].medico,personal),consultas[id],personal)
        transacciones.append(Transaccion(contId, random.randint(10,17),id, int(monto), devolverMedico(horas[id].medico,personal), consultas[id], horas[id]))
        contId+=1
    return transacciones
#estado false->devolucion true->pago aceptado
class Transaccion:
    def __init__(self,id,id_personal,id_consulta,monto,medico,consulta,hora):
        self.id = id
        self.id_personal = id_personal
        self.id_consulta = id_consulta
        self.monto = monto
        self.estado = sacarestado(consulta)
        self.mediopago = MedioPago(hora)
        self.boleta = boleta(medico,consulta, id)
        self.bono= bono(medico,consulta, id)
        self.vaucher=vaucher(self.mediopago,id)


