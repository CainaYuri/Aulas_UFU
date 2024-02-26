def fibonacci(n):

    if n<=1:

        return 1

        print("faça de novo")
    elif n>1:

        fib = fibonacci(n-1)+fibonacci(n-2)
        return fib

n= int(input("digite n:"))
print(fibonacci(n))
