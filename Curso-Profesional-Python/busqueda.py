titulo = "El gran principio de la programación"

print(
    'curso' in titulo # False
)

print(
    'programación' in titulo # True    
)

print(
    'Programación' in titulo # False (mayúscula)    
)

print(
    'Programación'.lower() in titulo.lower() # True (ignorando mayúsculas)
)

# Cantidad de veces que aparece una subcadena

print(
    titulo.count('a') # 4   
)

print(
    titulo.startswith('El gran') # True     
)

print(
    titulo.endswith('programación') # True
)

#lower() -> convierte a minúsculas
#upper() -> convierte a mayúsculas 

print(titulo.find('o'))
print('100'.isnumeric())

mensaje = "Hola, ¿cómo estás?"
print('Adiós' in mensaje) #False

print(mensaje.capitalize())  # Hola, ¿cómo estás?
print(mensaje.upper())  # HOLA, ¿CÓMO ESTÁS?
print(mensaje.lower())  # hola, ¿cómo estás?

print(f'{mensaje[0].upper()}{mensaje[1:]}')  # Hola, ¿cómo estás?