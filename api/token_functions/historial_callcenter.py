from datetime import datetime
from typing import List
import re
import json

def leerHistorial(historial):
    conversaciones = []
    conversacion = []

    for linea in range(len(historial)):

        if historial[linea] != '':
            conversacion.append(historial[linea])

            if linea == len(historial)-1:
                conversaciones.append(conversacion)

        elif historial[linea] == '' and len(conversacion) != 0:
            conversaciones.append(conversacion)
            conversacion = []
    
    return conversaciones


def obtenerPuntaje(conversacion: List[str]) -> int:
    puntaje = 0
    palabras = {
        'urgente': 0,
        'excelente': 0,
        'servicio': 0
    }

    for line in conversacion:
        palabras['urgente'] += len(re.findall('urgente', line.lower()))
        palabras['excelente'] += len(re.findall('excelente servicio', line.lower()))
        palabras['servicio'] += len(re.findall('muchas gracias|gracias|buena atención', line.lower()))
        
    puntaje += 20 if len(conversacion)-1 <= 5 else 10
    puntaje -= 5 if palabras['urgente'] <= 2 else 10
    
    if palabras['excelente'] > 0:
        puntaje += 100
        return puntaje
    
    puntaje += palabras['servicio']*10

    puntaje -= 100 if len(conversacion)-1 == 1 else 0

    inicio = datetime.strptime(conversacion[1].split()[0],'%H:%M:%S')
    fin = datetime.strptime(conversacion[-1].split()[0],'%H:%M:%S')

    puntaje += 50 if (fin-inicio).seconds < 60 else 25

    return puntaje


def obtenerCalificacion(puntaje: int) -> int:
    calificacion = 0

    if puntaje < 0:
        calificacion = 0
    elif puntaje < 25:
        calificacion = 1
    elif 25 <= puntaje < 50:
        calificacion = 2
    elif 50 <= puntaje < 75:
        calificacion = 3
    elif 75 <= puntaje < 90:
        calificacion = 4
    elif 90 <= puntaje:
        calificacion = 5
    
    return calificacion


def historialJson(texto: str):
    conversaciones = leerHistorial(texto.splitlines())
    puntajes = [[x[0], obtenerPuntaje(x), obtenerCalificacion(obtenerPuntaje(x))] for x in conversaciones]
    json_puntajes = json.dumps(puntajes)
    json_array = json.loads(json_puntajes)
    return json_array