import math
import random
vocales=["a","e","i","o","u"]
lodemas=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

def generadorCorreos(id):
    cadena = ""
    for i in range(0, random.randint(1, 10)):
        cadena += lodemas[random.randint(0, 20)]
        cadena += vocales[random.randint(0, 4)]

    for i in range(0, random.randint(0, 5)):
        cadena = cadena + str(random.randint(0, 9))

    cadena += str(hex(id))+"@gmail.com"
    return cadena


def generadorRut():
    cadena = ""
    cadena += str(random.randint(7000000, 12000000))
    mult = [2, 3, 4, 5, 6, 7]

    cadenainvert = ""
    for c in cadena:
        cadenainvert = c + cadenainvert

    i = 0
    suma = 0
    for c in cadenainvert:
        suma += int(c) * mult[i % 6]
        i += 1

    division = math.floor(suma / 11)
    multiplicacion = division * 11
    digit = 11 - math.fabs(suma - multiplicacion)

    if (digit == 10):
        return cadena + "-K"
    elif (digit == 11):
        return cadena + "-0"
    else:
        return cadena + "-" + str(int(digit))






class NodeT:
    def __init__(self,telef):
        self.telef = telef
        self.hi=None
        self.hd=None
        self.datos = 1

    def insert(self,nodo,root):

        ##buscar
        #IZQ
        if (self.telef<nodo.telef):
            if(self.hi!=None):
                self.hi.insert(nodo,root)

            else:
                self.hi=nodo
                root.datos += 1
                #print(root.datos)
        #Der
        if (self.telef>nodo.telef):
            if (self.hd != None):
                self.hd.insert(nodo,root)
            else:
                self.hd = nodo
                root.datos += 1
                #print(root.datos)

        if(self.telef==nodo.telef):
            return


    def convertToarr(self, arr):
        if (self.hi != None):
            self.hi.convertToarr(arr)
        else:
            return

        arr.append(self.telef)

        if (self.hd != None):
            self.hd.convertToarr(arr)
        else:
            return










class NodeR:
    def __init__(self,rut):
        self.rut = rut
        self.hi=None
        self.hd=None
        self.datos = 1

    def insert(self,nodo,root):

        ##buscar
        #IZQ
        if (convertRuttoNum(self.rut)<convertRuttoNum(nodo.rut)):
            if(self.hi!=None):
                self.hi.insert(nodo,root)
            else:
                self.hi=nodo
                root.datos += 1
                #print(root.datos)
        #Der
        if (convertRuttoNum(self.rut)>convertRuttoNum(nodo.rut)):
            if (self.hd != None):
                self.hd.insert(nodo,root)
            else:
                self.hd = nodo
                root.datos += 1
                #print(root.datos)

        if(convertRuttoNum(self.rut)==convertRuttoNum(nodo.rut)):
            return


    def convertToarr(self, arr):
        if (self.hi != None):
            self.hi.convertToarr(arr)
        else:
            return

        arr.append(self.rut)

        if (self.hd != None):
            self.hd.convertToarr(arr)
        else:
            return



















def convertRuttoNum(rut):
    cadena=""
    for i in rut:
        if(i!="-"):
            cadena+=i
        else:
            return int(cadena)

def generarData():
    arrRut=[]
    arrTelef = []
    arrCorreo = []
    rootR = NodeR(generadorRut());
    rootT = NodeT(random.randint(100000000, 999999999));

    arrB=0
    while(len(arrRut)<40000):
        print("Arboles RUT dropeados: ",arrB)
        #arrRut.append(rootR.insert(NodeR(generadorRut())))
        for i in range(0,100000):
            rootR.insert(NodeR(generadorRut()),rootR)
        rootR.convertToarr(arrRut)
        arrB+=1
        if (len(arrRut) < 40000):
            arrRut = []

    print(len(arrRut)," Rut Listos")

    while (len(arrTelef) < 40000):
        for i in range(0,500000):
            rootT.insert(NodeT(random.randint(100000000, 999999999)),rootT)
        rootT.convertToarr(arrTelef)
        if (len(arrTelef) < 40000):
            arrTelef = []

    print(len(arrTelef)," Telefonos Listos")

    for i in range(0,40000):
        arrCorreo.append(generadorCorreos(i))
    print(len(arrCorreo)," Correos listos")


    data=[]
    for i in range(0,40000):
        data.append([arrRut[i],arrTelef[i],arrCorreo[i]])
        #print([arrRut[i],arrTelef[i],arrCorreo[i]])

    print(len(data)," Pacientes Generados")
    return data



