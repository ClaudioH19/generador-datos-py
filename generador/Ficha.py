# Ficha (id, id_consulta, fechahora, registro)
import random


def dejarRegistro():
    anotaciones_medicas = [
        "Paciente presenta fiebre de 38.5 grados.",
        "Presion arterial: 120 sobre 80 mmHg.",
        "Ritmo cardiaco regular a 75 bpm.",
        "Nivel de glucosa en sangre: 90 mg por dL.",
        "Saturacion de oxigeno: 0.98.",
        "Paciente refiere dolor en el pecho.",
        "Exploracion fisica sin hallazgos anormales.",
        "Prescripcion de paracetamol 500 mg cada 8 horas.",
        "Se solicita analisis de sangre completo.",
        "Paciente con antecedentes de hipertension.",
        "Aplicacion de vacuna contra la influenza.",
        "Resultado de rayos X: sin signos de fractura.",
        "Paciente refiere mareos ocasionales.",
        "Diagnostico: infeccion del tracto urinario.",
        "Prescripcion de antibiotico amoxicilina 500 mg cada 12 horas.",
        "Se recomienda reposo y aumento de ingesta de liquidos.",
        "Historia familiar de diabetes mellitus.",
        "Exploracion abdominal: blando y depresible.",
        "Paciente con alergia conocida a la penicilina.",
        "Se ordena electrocardiograma.",
        "Paciente presenta dificultad para respirar.",
        "Evaluacion neurologica normal.",
        "Indice de masa corporal: 24.",
        "Se realiza sutura en herida de 3 cm.",
        "Paciente refiere insomnio.",
        "Se recomienda consulta con especialista en cardiologia.",
        "Examen de orina: presencia de proteinas.",
        "Paciente con tos persistente de 2 semanas de evolucion.",
        "Auscultacion pulmonar: sin ruidos anormales.",
        "Plan de manejo: control de seguimiento en 1 semana.",
        "Prescripcion de ibuprofeno 400 mg cada 6 horas.",
        "Paciente refiere dolor articular.",
        "Resultado de resonancia magnetica: hernia discal.",
        "Paciente con historia de tabaquismo.",
        "Se realiza prueba de funcion pulmonar.",
        "Paciente presenta nauseas y vomitos.",
        "Exploracion dermatologica: sin lesiones visibles.",
        "Diagnostico: migrana.",
        "Se ordena ecografia abdominal.",
        "Paciente con antecedentes de cirugia apendicular.",
        "Paciente refiere perdida de apetito.",
        "Nivel de colesterol: 180 mg por dL.",
        "Se recomienda dieta baja en sodio.",
        "Evaluacion psiquiatrica: paciente orientado en espacio y persona.",
        "Prescripcion de metformina 850 mg cada 12 horas.",
        "Paciente con sintomas de ansiedad.",
        "Se realiza prueba de funcion hepatica.",
        "Paciente con antecedentes de asma.",
        "Resultado de biopsia: negativo para malignidad.",
        "Paciente refiere vision borrosa.",
        "Paciente no asiste."
    ]
    return anotaciones_medicas[random.randint(0, len(anotaciones_medicas) - 1)]


def generadorFicha(horas):
    fichas=[]
    for id in range(0,108000):
        fichas.append(Ficha(id,horas))
    return fichas

class Ficha:
    def __init__(self,id,Horas):
        self.id = id
        self.id_consulta = id
        self.fechaHora=Horas[id].fecha+" "+Horas[id].hora
        self.registro=dejarRegistro()