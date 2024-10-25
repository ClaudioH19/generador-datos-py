#Contacto (id, id_hora, fechahora, via_confirmado, id_personal)
import random


def viaConfirmado(hora,id):
    arreglo=["WhatsApp", "Llamada", "No confirmado"]

    if(id<7200):
        return arreglo[random.randint(1,2)]

    h=int(hora[0]+hora[1])

    if(random.randint(0,100)==0):
        return arreglo[2]
    else:
        if(h<14 and h>=8):
            return arreglo[0]
        else:
            return arreglo[1]



def restarFecha(fecha,id):
    #0123456789
    #XXXX-XX-XX
    a=fecha[0]+fecha[1]+fecha[2]+fecha[3]
    m=fecha[5]+fecha[6]
    d=fecha[8]+fecha[9]
    if(id<7200):
        d=int(d)-2
    else:
        d=int(d)-1

    if(d<=0):

        if(int(m)<=7):
            if((int(m))%2==0):
                d=31
                m = int(m) - 1
                if (int(m) <= 0):
                    a = int(a) - 1
                    m=12
                    d=31
            else:
                if(int(m)-1==2):
                    d=28
                else:
                    d=30
                m=int(m)-1
                if(int(m)<=0):
                    a=int(a)-1
                    m=12
                    d=31
        else:
            if((int(m))%2!=0):
                d=31
                m = int(m) - 1
                if (int(m) <= 0):
                    a = int(a) - 1
                    m=12
                    d=31
            else:
                d=30
                m=int(m)-1
                if(int(m)<=0):
                    a=int(a)-1
                    m=12
                    d=31


    cadena=str(a)+"-"+str(m)+"-"+str(d)
    return cadena



def generarHoraCont():
    h=str(random.randint(8,23))
    if (len(h) < 2):
        h = "0" + h
    m=str(random.randint(0,59))
    if (len(m) < 2):
        m = "0" + m
    s =str(random.randint(0, 59))
    if (len(s) < 2):
        s = "0" + s
    cadena= h+":"+m+":"+s
    return cadena


#fecha = fechasHora[id][0]
#hora = fechasHora[id][1]
def generadorContacto(fechasHora):
    contactos=[]

    for id in range(0,108000):
        fecha=restarFecha(fechasHora[id][0],id)
        hora= generarHoraCont()
        fh=fecha+" "+hora
        contactos.append(Contacto(id,id,random.randint(10,17),fh,viaConfirmado(hora,id)))

    return contactos

class Contacto:
    def __init__(self,id,id_hora,id_personal,fechahora,viaConfirmado):
        self.id=id
        self.id_hora=id_hora
        self.fechahora=fechahora
        self.via_confirmado = viaConfirmado
        self.id_personal=id_personal




