def fatorial(n):
    if n ==0:
        return 1
    elif n > 0:
        r = n*fatorial(n-1)
    return r
    print(r)

n = int(input("n:"))
fat = fatorial(n)
print ("valor do fatorial é",fat)