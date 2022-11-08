

alumnos=[]
edad=[]
todos=[]
alumno=0
while alumno != "*":
    alumno = str(input("ingresa el nombre del alumno: "))
    if alumno == "*":
        break
    alumnos.append(alumno)
    eda= int(input("ingresa la edad: "))
    edad.append(eda)

todos = zip(alumnos, edad)
print("alumnos mayores de edad")
for i in todos:
    if i[1] >=18:
        print(i)

