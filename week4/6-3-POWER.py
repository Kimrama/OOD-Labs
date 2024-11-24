data = [int(i) for i in input("Enter Input a b : ").split(" ")]

def power(a, b, i=0) :
    if b == 0 : return 1
    if b - 1 == i : return a
    else : return a * power(a, b, i + 1)
 

print(power(data[0], data[1]))