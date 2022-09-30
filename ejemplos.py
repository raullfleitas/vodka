from asyncio.format_helpers import _format_callback_source
from pickle import FALSE
#preguntas
pregunta01 = "Cual es el nombre del programador"
pregunta02 = "Donde esta ubicado"
pregunta03 = "Que edad tiene"

pregunta = ["pregunta01,pregunta02,pregunta03"]
#respuestas
respuesta01 = "Lucas"
respuesta02 = "Polotic Misiones"
respuesta03 = "32"

pregunta = ["respuesta01,respuesta02,respuesta03"]
#entradas
entrada01 = input (f"pregunta 1 :{pregunta01}")
entrada02 = input (f"pregunta 2 :{pregunta02}")
entrada03 = input (f"pregunta 3 :{pregunta03}")
#aciertos
aciertos1 = False 
aciertos2 = False 
aciertos3 = False

if (entrada01 == respuesta01):
    aciertos1 = True
else:
    aciertos1 = False

if (entrada02 == respuesta02):
    aciertos2 = True
else:
    aciertos2 = False

if (entrada03 == respuesta03):
    aciertos3 = True
else:
    aciertos3 = False

print("\n")

if (aciertos1 == True):
    print("La pregunta 1 es correcta")
else:
    print ("pregunta 1 es incorrecta")

if (aciertos2 == True):
    print("La pregunta 2 es correcta")
else:
    print ("pregunta 2 es incorrecta")

if (aciertos3== True):
    print("La pregunta 3 es correcta")
else:
    print ("pregunta 3 es incorrecta")






