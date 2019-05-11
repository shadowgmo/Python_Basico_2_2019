'''
Suponga que se tiene una lista de listas que se tiene diversas
cantidades por persona.
1. La primera columna con números representa la cantidad en miles de colones que
tienen en la cuenta del banco,
2. la segunda columna la cantidad en crédito en miles de colones y
3. la tercer columna en miles de colones en deuda.
'''

#hoja_calculo = {
#    'carlos':{'debito' : '54.54', 'credito' : '6.57', 'deuda':'3.64'},
#    'juan':{'debito' : '5.54', 'credito' : '9.57', 'deuda':'4.64'},
#    'luis':{'debito' : '9.54', 'credito' : '7.57', 'deuda':'1.64'},
#}

#Ejercicio #1
#Contruya un diccionario de funciones matematicas
#utilizando funciones lambda) entre todos los números de
#la lista tales como:

suma=lambda x,y:x+y
multiple=lambda x,y:x*y
average = lambda x, y: (x+y)/2

lista_matematica = {
    'suma' : suma,
    'multiplica' : multiple,
    'average' : average,
}

#Ejercicio #2
#Obtenga utilizando el diccionario de funciones:
#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en
#promedio todas las personas.
#2. La suma de todas las deudas
#3. la multiplicación de todos los crédito entre si

#1.

#2.
import statistics

hoja_calculo = {'': None, 'carlos': {'debito': 54.54,
                               'credito': 6.57,
                               'deuda': 3.64, },

           'juan': {'debito': 5.54,
                     'credito': 9.57,
                     'deuda': 4.64, },

            'luis': {'debito': 9.54,
                     'credito': 7.57,
                     'deuda': 1.64, }}

aveValue1 = statistics.mean(d['debito'] for d in hoja_calculo.values() if d)
sumValue2 = sum(d['deuda'] for d in hoja_calculo.values() if d)
#mulValue3 = multiple(d['credito'] for d in hoja_calculo.values() if d)

#meter lambda suma y average

print(aveValue1)
print(sumValue2)
#print(mulValue3)



pass