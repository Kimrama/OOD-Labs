def odd_list(al):
    temp_list = []
    for element in al :
        if (element % 2 != 0) : temp_list.append(element)
    return temp_list


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)