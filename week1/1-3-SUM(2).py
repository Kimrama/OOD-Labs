data = [int(i) for i in input("Enter Your List : ").split()]
result = []

if len(data) < 3 : print("Array Input Length Must More Than 2")
else :
    for i in range(len(data)) :
        for j in range(1, len(data)) :
            for k in range(2, len(data)) :
                if i != j and i != k and j != k and data[i] + data[j] + data[k] == 5 :
                    temp_list = [data[i], data[j], data[k]]
                    temp_list.sort()
                    if temp_list not in result : result.append(list(tuple(temp_list)))


    print(result)