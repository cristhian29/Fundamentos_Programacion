
algebra=[]
calculo=[]


num=int(input("ingresa el nnumero de alumnos \nde la clase de algebra:"))
for i in range(num):
    nombre=str(input("ingresa el nombre del alumno:"))
    algebra.append(nombre)
num2=int(input("ingresa el numero de alumnos de la clase de calculo:"))
for i in range(num2):
    nombre2=str(input("ingresa el nombre del alumno:"))
    calculo.append(nombre2)
print("======================CLASE DE ALGREBRA======================")
for i in algebra:
    print(i)
print("=======================CLASE DE CALCULO======================")
for i in calculo:
    print(i)

print("====================ALUMNOS COMUNES EN LAS DOS CLASES")
todos=[]
for i in algebra:
    for x in calculo:
        if i == x:
            todos.append(x)
print(todos)
rep=len(todos)
print("NUMERO DE ALUMNOS COMUNES:",rep)





