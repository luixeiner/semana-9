lista = []
n = int(input("Ingrese un numero "))
mayor = 0
menor = 0
i = 1
while (n > 0):
 numero = float(input("numero :"))
 lista.append(numero)
 i = i + 1
 n = n - 1 
mayor = max(lista)
menor = min(lista)
print (lista)
print (mayor)
print (menor)
