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

mensaje3 = "PHP es un lenguaje de programación"
palabras = mensaje3.split()  # Por defecto, divide por espacios 
print(palabras)  # ['Hola,', '¿cómo', 'estás?']
print(mensaje3)