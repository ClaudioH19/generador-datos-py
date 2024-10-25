from Consulta import *
from FechaHoraTree import *
from Paciente import *
from Personal import *
from Horas import *
from Contacto import *
from Transaccion import *
from Ficha import *
#genera fechas al azar no repetidas
# por cada fecha genera horas no repetidas
#luego es tirar id's de med al azar
#




file = open ("Paciente.csv","w")
file = open ("Paciente.csv","a")

pacientes=generadorPaciente()

for i in pacientes:
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()



personal = generadorPersonal()

file = open ("Personal.csv","w")
file = open ("Personal.csv","a")
for i in personal:
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()



tuplas=(generadorTuplas())
#snapshot
for i in range(0,100):
    print(tuplas[i])
print("\n\n\n\n\n\n\n\n")
largo=len(tuplas)

for i in range (0,largo-1):
    idx=random.randint(0,largo-1)
    #cambio tuplas
    aux=tuplas[i]
    tuplas[i]=tuplas[idx]
    tuplas[idx]=aux

for i in range(0,100):
    print(tuplas[i])



horas= generadorHora2(tuplas)
file = open("Horas.csv", "w")
file = open("Horas.csv", "a")
for i in horas:
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()




consultas=generadorConsulta(horas,pacientes)
file = open("Consulta.csv", "w")
file = open("Consulta.csv", "a")
for i in consultas:
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()
print("Consultas Creadas")



file = open("Contacto.csv", "w")
file = open("Contacto.csv", "a")
for i in generadorContacto(tuplas):
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()
print("Contactos creados")


file = open("Transaccion.csv", "w")
file = open("Transaccion.csv", "a")
for i in generadorTransaccion(consultas,personal,horas):
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()
print("Transacciones creadas")
file = open("Ficha.csv", "w")
file = open("Ficha.csv", "a")

for i in generadorFicha(horas):
    j = 0
    for attr in vars(i).items():
        if(j<len(vars(i).items())-1):
            fila = str(attr[1]) + ","
            file.write(fila)
        else:
            fila = str(attr[1])
            file.write(fila)
        j+=1
    file.write("\n")
file.close()
print("Fichas creadas")













