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