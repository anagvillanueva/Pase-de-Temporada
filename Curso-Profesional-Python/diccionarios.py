# clave (key) : valor (value)

mi_diccionario = {
    'usuario': "admin",
    'edad': 25,
    'contrasena': "1234",
    10: "diez",
    (1,2): "una tupla"
}

# Los diccionarios son mutables
# Las claves son inmultables (strings, números, tuplas)
# Si agregamos una clave que ya existe, se sobreescribe el valor

print(mi_diccionario)

print('usuario' in mi_diccionario)  # True
print('admin' in mi_diccionario)  # False

print(mi_diccionario['usuario'])  # admin
print(mi_diccionario.get('usuario'))  # admin 

#Se recomienda usar get para evitar errores si la clave no existe
print(mi_diccionario.get('no_existe'))  # None
print(mi_diccionario.get('no_existe', 'No existe el valor que buscas'))  # Valor por defecto

#El segundo argumento de get es el valor por defecto si la clave no existe

# Agregar o modificar elementos
mi_diccionario['nuevo'] = 'Mapache' # Agregar un nuevo par clave-valor
print(mi_diccionario)

mi_diccionario['usuario'] = 'root' # Modificar el valor de una clave existente
print(mi_diccionario)

#Metodos de los diccionarios
print(mi_diccionario.keys())  # Devuelve las claves
print(mi_diccionario.values())  # Devuelve los valores
print(mi_diccionario.items())  # Devuelve pares (clave, valor)

print(list(mi_diccionario.keys()))  # Convertir a lista las claves
print(list(mi_diccionario.values()))  # Convertir a lista los valores

print(tuple(mi_diccionario.items()))  # Convertir a tupla los pares (clave, valor)

print(len(mi_diccionario))  # Número de pares  5

#Agregar más elementos
mi_diccionario['edad'] = 30
mi_diccionario['apellido'] = 'Perez'
print(mi_diccionario)
print(len(mi_diccionario))  # Número de pares 7

mi_diccionario.update({'usuario': 'superadmin', 'contrasena': 'abcd', 'nuevo2': 'Gato'})
print(mi_diccionario)

# Actualiza los valores de las claves existentes y agrega nuevas claves si no existen
mi_diccionario.setdefault('pais', 'Argentina')  # Agrega la clave 'pais' con valor 'Argentina' si no existe
print(mi_diccionario)

# Eliminar elementos
mi_diccionario.pop('nuevo2')  # Elimina la clave 'nuevo2' y su valor
del mi_diccionario['apellido']  # Elimina la clave 'apellido' y su valor
print(mi_diccionario)

mi_diccionario.popitem()  # Elimina el último par (clave, valor) agregado
print(mi_diccionario)   


mi_diccionario['age'] = mi_diccionario.pop('edad', 'No existe la clave edad')
print(mi_diccionario)  # Mueve el valor de 'edad' a 'age',


#Limpiar el diccionario
mi_diccionario.clear()
print(mi_diccionario)  