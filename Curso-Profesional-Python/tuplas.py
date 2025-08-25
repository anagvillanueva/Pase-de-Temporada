#Tuplas en Python, son inmutables y se definen con paréntesis
settings = ("localhost", 8080, True)

print(type(settings)) # <class 'tuple'>

#Mediante indexación podemos acceder a los elementos de la tupla
print(settings[0]) # localhost
print(settings[1]) # 8080   

numeros = 1, 2, 3, 4, 5
print(type(numeros)) # <class 'tuple'>

cursos = ("Python", "Django", "Flask") 

var1 = cursos[0]
var2 = cursos[1]    

print(var1) # Python

vegetales = ("Tomate", "Lechuga", "Zanahoria")

#Desempaquetado de tuplas
v1, v2, v3 = vegetales
print(v1) # Tomate

frutas = ("Manzana", "Pera", "Naranja", "Banana")
#Si no queremos desempacar todos los elementos

f1, _, f3, _ = frutas #Estamos ignorando el segundo y cuarto elemento
print(f3) 

#agrupar con tuplas

animales = ("Perro", "Gato", "Loro", "Tortuga", "Pez")

a1, *a2, _, a3 = animales

print(a2) # ['Gato', 'Loro']
print(a3) # Pez

#Funcion Zip

users = ["user1", "user2", "user3"]
cities = ["Madrid", "Barcelona", "Valencia"]

response = list(zip(users, cities))
print(type(response)) # <class 'zip'>
print(response) # [('user1', 'Madrid'), ('user2', 'Barcelona'), ('user3', 'Valencia')]


numbers = [1, 2, 3, 4, 5]   
nombres = ["Juan", "Ana", "Luis", "Marta", "Lucia"]

#tupla de tuplas
response1 = tuple(zip(numbers, nombres))
print(type(response1)) # <class 'tuple'>  
print(response1) # ((1, 'Juan'), (2, 'Ana'), (3, 'Luis'), (4, 'Marta'), (5, 'Lucia'))      

print(sorted(nombres)) #Ordenamiento de forma ascendente
print(sorted(nombres, reverse=True)) #Ordenamiento de forma descendente

#Si un valor se encuentra en la tupla
print(numbers.count(3)) #Cuenta cuantas veces aparece el elemento 3 en la tupla 

print(3 in numbers) #True
print(10 in numbers) #False

#Donde se encuentra un elemento en la tupla
print(nombres.index("Marta")) #3, devuelve el índice del elemento 