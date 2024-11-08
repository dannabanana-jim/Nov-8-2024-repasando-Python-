"""
2.-Dada una nota almacenada en una variable, imprime su equivalente:
• Mayor o igual a 0, pero menor que 5, SUSPENSO.
• Mayor o igual a 5, pero menor que 6, SUFICIENTE.
• Mayor o igual a 6, pero menor que 7, BIEN.
• Mayor o igual a 7, pero menor que 9, NOTABLE.
• Mayor o igual a 9, pero menor o igual a 10, SOBRESALIENTE.
En cualquier otro caso, imprimir el texto: NOTA NO VÁLIDA.
"""
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

nota = float(input("Ingresa la nota: "))

if 0 <= nota < 5:
    print("SUSPENSO")
elif 5 <= nota < 6:
    print("SUFICIENTE")
elif 6 <= nota < 7:
    print("BIEN")
elif 7 <= nota < 9:
    print("NOTABLE")
elif 9 <= nota <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")



