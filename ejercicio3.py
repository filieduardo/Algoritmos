cantidad=int(input("¿cuantos productos va a registrar?"))
lista=[]

for i in range(cantidad):
    num=str(i+1)
    nombre=input("ingrese el nombre del producto"+num+":")
    precio=float(input("ingrese el precio del procucto"+num+":"))
    categoria=input("ingrese la categoria del producto"+num+":")
    
    producto=[nombre,precio,categoria]
    lista.append(producto)

#cantidad delproductos en el catalogo
print(len(lista)) #print(cantidad)

#precio promedio del catalogo
suma=0
for producto in lista:
    suma=suma + producto[1]
promedio=suma/cantidad
print(" El prcio promedio es:",promedio)

#cantidad de productos que superan el precio promedio del catalogo
contador= 0
for producto in lista:
    if producto[1]>promedio:
        contador = contador + 1

print("cantidad de productosque superan el precio promedio",contador)

#producto mas caro
mas_caro=lista[0]

for producto in lista:
    if producto[1]>mas_caro[1]:
        mas_caro=producto
print("El producto mas caro es:",mas_caro)


#producto mas barato
mas_barato=lista[0]

for producto in lista:
    if producto[1]<mas_barato[1]:
        mas_barato=producto
print("el producto mas barato",mas_barato)

#categoria con mis produtos

