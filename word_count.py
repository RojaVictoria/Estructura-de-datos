with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

caracteres = set(texto)
cuenta_car = len(caracteres)

palabras = set(texto.split(' '))
cuenta_pal = len(palabras)

print(f'El número de caracteres distintos es: {cuenta_car}')
print(f'El número de palabras distintas es: {cuenta_pal}')