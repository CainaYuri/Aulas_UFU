r = int(input("razão"))
n = int(input("termos"))
t1 = int(input("primiro termo"))

li=[t1]
for i in range(0,n-1):
  li.append(r+li[i])

print(li)