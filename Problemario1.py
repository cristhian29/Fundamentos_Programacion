import random

vector_numeros = []
for i in range(10):
    vector_numeros.append(random.randint(1,10))
cuadrado=[]
for i in vector_numeros:
    i**=2
    cuadrado.append(i)
cubo=[]
for i in vector_numeros:
    i**=3
    cubo.append(i)
x = zip(vector_numeros,cuadrado,cubo)
print("Vectores: ",tuple(x))
