print("Hola")

variable = "@ana_gvillanueva" 
#Python es de tipado dinámico, no es necesario declarar el tipo de variable 

print(variable)
print(type(variable)) #Muestra el tipo de variable

#Nomenclatura snake_case 
first_name = "Ana"
last_name = 'Villanueva'

print(first_name)
print(last_name)

#Concatenación de cadenas
full_name = first_name + " " + last_name
print(full_name)

#Formateo de cadenas
full_name = f"{first_name} {last_name}"
print(full_name)

number = 100_000_000 #Python permite usar guiones bajos para mejorar la legibilidad de los números
print(number) 
print(type(number)) #Int es un tipo de dato que representa números enteros

pi = 3.1416
print(pi)
print(type(pi)) #Float es un tipo de dato que representa números decimales

#Booleanos
is_active = True #Mayuscula o minuscula no afecta el valor, pero se recomienda usar mayuscula
print(is_active)
print(type(is_active)) #Boolean es un tipo de dato que representa valores de verdad (True o False)

#CONSTANTES

VERSION = "1.0.0" #Convención de nomenclatura para constantes, fines de lectura y no cambiar su valor

print("Lista del supermercado $")
manzana = 55
pera = 32.20
pechuga = 120.50

gasto_total = manzana + pera + pechuga
print(f"Total supermercado: ${gasto_total:.2f}") #:.2f para mostrar dos decimales
print(f"Total supermercado: ${gasto_total}") #Sin formato de decimales

#Operadores relacionales, dan como resultado un booleano (True o False)
numero1 = 10
numero2 = 20

print(numero1 > numero2)  #Mayor que
print(numero1 < numero2)  #Menor que
print(numero1 >= numero2) #Mayor o igual que
print(numero1 <= numero2) #Menor o igual que
print(numero1 == numero2) #Igualdad
print(numero1 != numero2) #Desigualdad

#Operadores lógicos
#AND, OR, NOT
print("Operadores lógicos")
print(True and False)  #AND, True si ambos son True
print(True or False)   #OR, True si al menos uno es True
print(not True)        #NOT, invierte el valor booleano

