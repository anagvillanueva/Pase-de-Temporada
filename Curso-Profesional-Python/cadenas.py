mensaje = "Hola Mundo"
print(mensaje)  

print(type(mensaje))

print(len(mensaje))

print('Hola' in mensaje) #True
print('Adiós' in mensaje) #False

print(mensaje[0])  # H
print(mensaje[-3])  # n

mensaje2 = mensaje[0:4]  # 'Hola'
print(mensaje2)

#Los strings son inmutables
#mensaje[0] = 'h'  # Esto generaría un error

#split -> divide una cadena en una lista
#join -> une una lista en una cadena

#Generar una lista a partir de un string
mensaje3 = "PHP es un lenguaje de programación"
palabras = mensaje3.split()  # Por defecto, divide por espacios 
print(palabras)  # ['Hola,', '¿cómo', 'estás?']
print(mensaje3) 

# Generar un string a partir de una lista
cursos = ["Python", "JavaScript", "Java", "C++" ]
mensaje4 = ", ".join(cursos)
print(mensaje4) 

#Generar nuevos strings
name = "Ana"
last_name = "Villanueva"
full_name = f"{name} {last_name}"  # f-string
print(full_name)  # Ana Villanueva

full_name2 = ' '.join([name, last_name])
print(full_name2)  # Ana Villanueva

full_name3 = 'El nombre completo es %s %s' % (name, last_name)
print(full_name3)  # Ana Villanueva

full_name4 = 'El nombre completo es {} {}'.format(name, last_name)
print(full_name4)  # Ana Villanueva

base = 'El nombre completo es {} {}. Su edad es: {}'
full_name5 = base.format(name, last_name, 24)
print(full_name5)  

base2 = 'El nombre completo es {1} {0}. Su edad es: {2}'
full_name6 = base2.format(last_name, name, 24)  
print(full_name6)

base3 = 'El nombre completo es {nombre} {apellido}. Su edad es: {edad}'
full_name7 = base3.format(nombre=name, apellido=last_name, edad=24) 

nombre = "Diego"
apellido = "Lechuga"

# f-string

#se recomienda usar f-strings, ya que son más legibles y eficientes 

print(f"El nombre completo es {nombre} {apellido}. Su edad es: {21}")
print(f"El nombre completo es {nombre.upper()} {apellido.lower()}. Su edad es: {21}")   

nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)

print('El nombre es:', nombre, apellido, sep="_") #El_nombre_es:_Diego_Lechuga