numeros = []
suma = 0
for i in range (5):
    lista = int(input("ingrese un numero: "))
    numeros.append(lista)
for numero in numeros:
    suma += numero
promedio = suma / len(numeros)
print("suma: ",suma)
print("promedio: ",promedio)
print("mayor: ",max(numeros))
print("menor: ",min(numeros))