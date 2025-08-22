mi_lista = ["Ana", 23, 1.65, True, "Estudiante"]
print(type(mi_lista)) # Imprime el tipo de dato de list 

#Lo ideal es que todos los elementos de la lista sean del mismo tipo

cursos = ["Python", "Java", "JavaScript", "C++"]
numeros = [1, 2, 3, 4, 5]

print(cursos)
print(numeros)

print(cursos[0])  # Imprime el primer elemento de la lista
print(cursos[1])  # Imprime el segundo elemento de la lista

print(
    len(cursos)  # Imprime la longitud de la lista cursos
)

print(
    cursos[-1] # Imprime el último elemento de la lista cursos
)

#Python permite acceder a los elementos de una lista usando índices negativos
print(cursos[-2])  # Imprime el penúltimo elemento de la lista cursos

cursos[0] ="Golang" # Modifica el primer elemento de la lista cursos

print(cursos)

#Sublistas
nueva_lista = []

#Slicing, extrae una parte de la lista
# [inicio:fin]

nueva_lista = cursos[0:2] #Podemos omitir el cero
print(nueva_lista)  # Imprime los elementos desde el índice 0 hasta el 1 (excluyendo el 2)


#            0      1       2         3         4
musica = ["Rock", "Pop", "Jazz", "Reggae", "Hip Hop"]
playlist = musica[1:4]  # Extrae los elementos desde el índice 1 hasta el 3 (excluyendo el 4)
print(playlist)  # Imprime la sublista de música


gatos = ["Persa", "Siames", "Bengala", "Sphynx"]
mascotas = gatos[:]  # Crea una copia superficial de la lista gatos
print(mascotas)  # Imprime la copia de la lista gatos

#              0          1          2         3         4
verduras = ["tomate", "lechuga", "cebolla", "pepino", "zanahoria"]
supermercado = verduras[:4]
print(supermercado)  # Imprime los primeros 4 elementos de la lista verduras


#            0          1          2         3         4
frutas = ["manzana", "pera", "naranja", "plátano", "kiwi"]
supermercado = frutas[::-2]  # Extrae los elementos a partir del final, con un paso de -2
print(supermercado)  # Imprime los elementos en posiciones pares de la lista frutas

#[inicio:fin:paso]