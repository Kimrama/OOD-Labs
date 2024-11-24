def fibo(i) :
    if i <= 1:
        return i
    else : return fibo(i - 1) + fibo(i - 2)

print(fibo(4))