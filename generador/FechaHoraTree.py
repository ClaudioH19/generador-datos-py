from Horas import *
import math

import time
def conversorFechatoint(fecha: str):
    cadena = ""
    for i in fecha:
        if (i != "-"):
            cadena += i
    return int(cadena)


def conversorHoratoint(hora: str):
    veces = 0
    cadena = ""

    for i in hora:
        #if(i==":"):##esto ontrola que se se guarde hasta los minutos
        #    veces+=1
        #if(veces==1 and i==":"):
        #    return int(cadena)

        if (i != ":"):
            cadena += i
    return int(cadena)

def generadorFecha(i: int):
    cadena = ""
    d = str(random.randint(1, 31))
    if (len(d) < 2):
        d = "0" + d


    m = str(random.randint(1, 12))
    if (len(m) < 2):
        m = "0" + m

    if(int(m)<=7):

        if(int(m)%2 == 0 and d=="31"):
            d="30"
        if (m == "02" and (d == "31" or d == "30" or d == "29")):
            d = "28"


    else:
        if (int(m) % 2 != 0 and d == "31"):
            d = "30"

    if (i == 1):
        a= str(random.randint(1980, 2021))
    else:
        # 'Dom 20 de junio 23:21:05 1993'
        ##print(m, time.localtime().tm_mon)
        if int(m) < time.localtime().tm_mon:
            a= str(random.randint(2022, 2024))
        else:
            a= str(random.randint(2022, 2023))

    cadena=a+"-"+m+"-"+d
    return cadena






def generadorFechaTree():

    # optimo 0 --> 4000 | 1 --> 1000
    arrB=0
    arr = []


    while(len(arr)<300):
        root = node(generadorFecha(0))
        print("Arboles Fechas dropeados: ",arrB)
        for i in range(0, 4000):  # intenta 4000 veces generalmente salen como 400 fechas distintas
            root.insert(node(generadorFecha(0)))
        # root.print("")
        root.convertToarr(arr)

        if(len(arr)<300):
            print("Fechas en tree: ", len(arr))
            arr=[]
            arrB += 1

    #for i in range(0, 5000):  # intenta 4000 veces generalmente salen como 400 fechas distintas
    #    root.insert(node(generadorFecha(0)))
    #root.convertToarr(arr)

    return arr


def generadorHoraTreexcantFecha(fechas):
    ##genera cantidad mayor a largo necesario de horas distintas
    largoNecesario = math.ceil(108000 / len(fechas))
    arr = []
    cotaSup = int(largoNecesario)
    arrB=0

    while (len(arr) < largoNecesario):

        #print("Arboles Horas dropeados: ",arrB)
        root = nodeH(generadorHoras())
        for i in range(0, cotaSup):
            root.insert(nodeH(generadorHoras()))

        root.convertToarr(arr)
        # otra vuelta reiniciar
        if (len(arr) < largoNecesario):
            cotaSup += 200
            arr = []
        arrB+=1
    return arr



def generadorTuplas():
    tuplasFechaHora = []
    fechasTree = generadorFechaTree()
    cont = 0
    med=0
    cantHorasxfech=0
    for fecha in fechasTree:
        horas = generadorHoraTreexcantFecha(fechasTree)
        cantHorasxfech+=len(horas)
        for hora in horas:
            tuplasFechaHora.append([fecha, hora,med%10])
            med+=1
        cont += 1
        print(fecha, ": Cubierta con ", len(horas), " horas |", cont, " de ", len(fechasTree))

    print("Se generaron: ",len(fechasTree), "Fechas con : ",(cantHorasxfech/len(fechasTree))," Horas en promedio")
    print("Datos generados: ",len(tuplasFechaHora))
    return tuplasFechaHora


class node:

    def __init__(self, fecha):
        self.fecha = fecha
        self.leftnode = None
        self.rightnode = None

    def busqueda(self, node):
        # busqueda por irzquierda
        if (conversorFechatoint(self.fecha) < conversorFechatoint(node.fecha)):
            return self.leftnode.busqueda(node)
        # busqueda por derecha
        if (conversorFechatoint(self.fecha) > conversorFechatoint(node.fecha)):
            return self.rightnode.busqueda(node)
        # encontrado
        if (conversorFechatoint(self.fecha) == conversorFechatoint(node.fecha)):
            return self.horas
        # noencontrado
        return None

    def insert(self, node):
        # busqueda por irzquierda
        if (conversorFechatoint(self.fecha) < conversorFechatoint(node.fecha)):
            if (self.leftnode == None):
                self.leftnode = node
            else:
                self.leftnode.insert(node)

        # busqueda por derecha
        if (conversorFechatoint(self.fecha) > conversorFechatoint(node.fecha)):
            # insertar
            if (self.rightnode == None):
                self.rightnode = node
            else:
                self.rightnode.insert(node)

        # encontrado
        if (conversorFechatoint(self.fecha) == conversorFechatoint(node.fecha)):
            # print( "ya existe")
            return

    def print(self, esp):
        if (self.leftnode != None):
            self.leftnode.print("   " + esp)
        else:
            print(esp + "None")

        print(esp + self.fecha)

        if (self.rightnode != None):
            self.rightnode.print("   " + esp)
        else:
            print(esp + "None")

    def convertToarr(self, arr):
        if (self.leftnode != None):
            self.leftnode.convertToarr(arr)
        else:
            return

        arr.append(self.fecha)

        if (self.rightnode != None):
            self.rightnode.convertToarr(arr)
        else:
            return








class nodeH:

    def __init__(self, hora):
        self.hora = hora
        self.leftnode = None
        self.rightnode = None
        self.fechas = []

    def busqueda(self, node):
        # busqueda por irzquierda
        if (conversorHoratoint(self.hora) < conversorHoratoint(node.hora)):
            return self.leftnode.busqueda(node)
        # busqueda por derecha
        if (conversorHoratoint(self.hora) > conversorHoratoint(node.hora)):
            return self.rightnode.busqueda(node)
        # encontrado
        if (conversorHoratoint(self.hora) == conversorHoratoint(node.hora)):
            return self.hora
        # noencontrado
        return None

    def insert(self, node):
        # busqueda por irzquierda
        if (conversorHoratoint(self.hora) < conversorHoratoint(node.hora)):
            if (self.leftnode == None):
                self.leftnode = node
            else:
                self.leftnode.insert(node)

        # busqueda por derecha
        if (conversorHoratoint(self.hora) > conversorHoratoint(node.hora)):
            # insertar
            if (self.rightnode == None):
                self.rightnode = node
            else:
                self.rightnode.insert(node)

        # encontrado
        if (conversorHoratoint(self.hora) == conversorHoratoint(node.hora)):
            # print( "ya existe")
            return

    def print(self, esp):
        if (self.leftnode != None):
            self.leftnode.print("   " + esp)
        else:
            print(esp + "None")

        print(esp + self.hora)

        if (self.rightnode != None):
            self.rightnode.print("   " + esp)
        else:
            print(esp + "None")

    def convertToarr(self, arr):
        if (self.leftnode != None):
            self.leftnode.convertToarr(arr)
        else:
            return

        arr.append(self.hora)

        if (self.rightnode != None):
            self.rightnode.convertToarr(arr)
        else:
            return



