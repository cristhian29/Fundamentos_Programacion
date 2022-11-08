
vector =[]
for i in range(10):
    valor = int(input("ingrese el valor: "))
    if valor < 0:
        break
    else:
        vector.append(valor)
print(vector)