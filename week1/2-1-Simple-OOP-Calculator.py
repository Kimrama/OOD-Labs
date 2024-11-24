class Calculator :

    def __init__(self, value) :
        self.value = value

    def __add__(self, op):
        return self.value + op.value
    def __sub__(self, op):
        return self.value - op.value

    def __mul__(self, op):
        return self.value * op.value

    def __truediv__(self, op):
        if op.value == 0 : return ""
        return float(self.value / op.value)
    

x,y = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")