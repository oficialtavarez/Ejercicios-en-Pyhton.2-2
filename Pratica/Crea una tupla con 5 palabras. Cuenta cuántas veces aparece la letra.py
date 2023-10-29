palabras_tupla = ("Azul", "perro", "gato", "Cafeterria", "Pera")
contador_a = 0
for palabra in palabras_tupla:
    contador_a += palabra.count('a')
print("Número de veces que aparece 'a':", contador_a)