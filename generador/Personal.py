from FechaHoraTree import *
import random
import math


nombresDoc=["Sara","Juana","Manuel","Patricio","Camilo","Patricia","Millaray","Constanza","Rosa","Pamela"]
nombresCorto=["Sarita","Juanita","Manu","Pato","Cami","Paty","Milla","Coni","Rosita","Pame"]


apellidos=["mino","hernandez","martinez","aguilera","salazar","munoz","garrido","valdes","salas","soto","donoso","faundez",
           "diaz","mendoza","lopez","rojas","chacon","retamal","guerrero","campos","saavedra","garcia"]

vocales=["a","e","i","o","u"]
lodemas=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]


def generadorCorreos():    
    cadena=""
    for i in range(0, random.randint(1,10)):
        cadena+=lodemas[random.randint(0,20)]
        cadena+=vocales[random.randint(0,4)]
    
    for i in range(0,random.randint(0,5)):
        cadena=cadena+str(random.randint(0,9))
        
    cadena+="@gmail.com"
    return cadena


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





def generadorRut():
    cadena=""
    cadena+=str(random.randint(10000000,23000000))
    mult=[2,3,4,5,6,7]
    
    cadenainvert=""
    for c in cadena:
        cadenainvert=c+cadenainvert
    
    
    i=0
    suma=0
    for c in cadenainvert:
        suma+=int(c)*mult[i%6]
        i+=1
        
    division = math.floor(suma/11)
    multiplicacion=division*11
    digit=11-math.fabs(suma-multiplicacion)
    
    if(digit==10):
        return cadena+"-K"
    elif(digit==11):
        return cadena+"-0"
    else:
        return cadena+"-"+str(int(digit))

#2. Es posible que el Personal sea del tipo “médico”-0, “administrativo”-1, “jefatura”-2


#El personal tendrá por defecto el estado con valor “habilitado”

#Solo el Personal de tipo “médico” podrá tener un valor definido para el atributo porcentaje.


#La información de diez médicos encargados de hacer consultas médicas y/o pabellones.
#El personal administrativo corresponde a 10 usuarios (8 cajeros y 2 jefaturas)

#Personal (id, rut, nombre, apellido, teléfono, correo, nombre_corto, tipo, fecha_ing, estado, porcentaje, fonasa)


def generadorPersonal():
    arregloPersonal = []
    for i in range(0, 10):
        rut = generadorRut()
        telef = random.randint(100000000, 999999999)
        correo = generadorCorreos()

        j = 0

        while (j < i):
            if (rut == arregloPersonal[j].rut):
                rut = generadorRut()
                j = 0

            if (telef == arregloPersonal[j].telefono):
                telef = random.randint(100000000, 999999999)
                j = 0

            if (correo == arregloPersonal[j].correo):
                correo = generadorCorreos()
                j = 0
            j += 1

        cadena = str(random.randint(0, 0))
        cadena += "."
        cadena += str(random.randint(15, 20))

        #id,rut,telefono,correo,tipo,porcentaje fonasa
        personal = Personal(i, rut, telef, correo, 0, float(cadena), bool(random.randint(0, 1)))
        arregloPersonal.append(personal)

    for i in range(0, 10):
        rut = generadorRut()
        telef = random.randint(100000000, 999999999)
        correo = generadorCorreos()

        j = 0

        while (j < i):
            if (rut == arregloPersonal[j].rut):
                rut = generadorRut()
                j = 0

            if (telef == arregloPersonal[j].telefono):
                telef = random.randint(100000000, 999999999)
                j = 0

            if (correo == arregloPersonal[j].correo):
                correo = generadorCorreos()
                j = 0
            j += 1

        cadena = str(random.randint(0, 0))
        cadena += "."
        cadena += str(random.randint(45, 50))

        #id,rut,telefono,correo,tipo,porcentaje
        if (i == 8 or i == 9):
            personal = Personal(i + 10, rut, telef, correo, 2, float(0), False)
        else:
            personal = Personal(i + 10, rut, telef, correo, 1, float(0), False)

        arregloPersonal.append(personal)

    return arregloPersonal



class Personal:
    def __init__(self,id,rut,telefono,correo,tipo,porcentaje,fonasa):
        num=random.randint(0,9)
        self.id=id
        self.rut=rut
        self.nombre=nombresDoc[num]
        self.apellido=apellidos[random.randint(0,21)]
        self.telefono=telefono
        self.correo=correo
        self.nombre_corto=nombresCorto[num]
        self.tipo=tipo
        self.fecha_ing=generadorFecha(0)
        self.estado=True
        self.porcentaje=porcentaje
        self.fonasa=fonasa
        
        
