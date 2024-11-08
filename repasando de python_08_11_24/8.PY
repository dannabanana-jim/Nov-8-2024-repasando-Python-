#8.-Imprimir la tabla de multiplicar de un número almacenado en una variable utilizando rangos. 
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Almacenamos el número en una variable
numero = int(input("Ingresa el número para mostrar su tabla de multiplicar: "))

# Usamos un rango para imprimir la tabla de multiplicar del número
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


