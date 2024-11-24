data = list(map(int, input("Enter Input : ").split(" ")))

sort = True
for i in range(len(data) - 1) :
    if data[i] > data[i + 1] :
        sort = False
        break

if sort : print("Yes") 
else : print("No") 