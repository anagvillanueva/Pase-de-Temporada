#Input siempre va retornar string 

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? ")) #Convertir a entero
estatura = float(input("¿Cuál es tu estatura? ")) #Convertir a decimal
status = input("¿Eres estudiante? (si/no) ") == 'si' #Convertir a booleano
grado = input("¿Cuál es tu grado? ")

print(f"Tu nombre es {nombre}, tienes {edad} años, mides {estatura} metros y tu estatus de estudiante es {status}.")

first_name, last_name, age = "Ana", 'Villanueva', 23  #Asignación múltiple
print(f"{first_name} {last_name} tiene {age} años.")