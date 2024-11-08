"""
12 
Utilizando bucles for, imprimir el siguiente dibujo: 
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
*
"""
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Imprimir la parte ascendente del dibujo
for i in range(1, 6):
    print('*' * i)

# Imprimir la parte descendente del dibujo
for i in range(4, 0, -1):
    print('*' * i)

