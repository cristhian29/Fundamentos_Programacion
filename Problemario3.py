import statistics

notas =[]
for i in range(5):
    calf = float(input("ingrese la calificación: "))
    if calf>=0 and calf<=10:
        notas.append(calf)
    else:
        print("ingrese un valor valido")
        quit()
print("Notas: ",notas)

media = statistics.mean(notas)
print("la media es: ",media)

print("la nota mas alta es: ",max(notas))
print("la nota mas baja es: ",min(notas))