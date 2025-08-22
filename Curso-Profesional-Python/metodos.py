
#            0        1         2         3         4
cursos = ["Python", "Java", "JavaScript", "C++", "Ruby"]

cursos.append("Go")  # Agrega "Go" al final de la lista cursos
print(cursos)  # Imprime la lista actualizada de cursos

cursos.insert(2, "C#")  # Inserta "C#" en la posición 2 de la lista cursos
print(cursos)  # Imprime la lista actualizada de cursos

nuevos_cursos = ["Swift", "Kotlin"]
cursos.extend(nuevos_cursos)  # Agrega los elementos de nuevos_cursos a la lista cursos
print(cursos)  # Imprime la lista actualizada de cursos

print("Java" in cursos)  # Verifica si "Java" está en la lista cursos
print("PHP" in cursos)  # Verifica si "PHP" está en la lista cursos

print(cursos.index("JavaScript"))  # Imprime el índice del elemento "JavaScript" en la lista cursos

#Si el valor no está en la lista, se genera un error

cursos.remove("JavaScript")  # Elimina "C++" de la lista cursos
print(cursos)  # Imprime la lista actualizada de cursos

ultimo_curso = cursos.pop()  # Elimina (retorna) el último elemento de la lista cursos
print(cursos)  # Imprime la lista actualizada de cursos
print(ultimo_curso)  # Imprime el último curso eliminado

# cursos.clear()  # Elimina todos los elementos de la lista cursos
# print(cursos)  # Imprime la lista vacía

copia_cursos = cursos[:] # Crea una copia superficial de la lista cursos Shallow copy
copia_cursitos = cursos.copy()  # Crea una copia superficial de la lista cursos usando el método copy()

copia_cursos = cursos[::-1]  # Crea una copia superficial de la lista cursos en orden inverso
copia_cursitos.reverse()  # Invierte el orden de los elementos en la copia de cursos
print(copia_cursitos)  # Imprime la lista de cursos invertida

copia_cursitos.sort()  # Ordena alfabéticamente la lista de cursos
print(copia_cursitos)  # Imprime la lista de cursos ordenada alfabéticamente