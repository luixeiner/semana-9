numeros=[]
n=int(input("Ingrese el límite: "))
for i in range(n):
    mi_numero=int(input("Ingrese un número: "))
    numeros.append(mi_numero)
suma = 0
contador=0
while contador < n:
    suma += numeros[contador]
    contador+=1
promedio=suma/len(numeros)
print("La suma es",suma)
print("El promedio es",promedio)
print("El mayor número es:",max(numeros))
print("El menor número es:",min(numeros))