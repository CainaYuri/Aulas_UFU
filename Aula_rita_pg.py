r = int(input("razão"))
n = int(input("termos"))
t1 = int(input("primiro termo"))

lista=[t1]
for i in range(0,n-1):
  lista.append(r*lista[i])

print(lista)