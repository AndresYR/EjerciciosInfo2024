# Fibonacci

def fibo(n):
    fibo_list = [0,1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(1,n-1):
            siguiente = fibo_list[i-1] + fibo_list[i]
            fibo_list.append(siguiente)
        return fibo_list

for i in fibo(4):
    print(i,end=",")