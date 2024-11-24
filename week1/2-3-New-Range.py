print("*** New Range ***")
data = [float(i) for i in input("Enter Input : ").split()]

def new_range(data) :
    result = []
    if len(data) == 1 :
        start = 0.0
        while start < data[0] :
            result.append(start)
            start += 1
        
    elif len(data) == 2 :
        start = data[0]
        while start < data[1] :
            result.append(start)
            start += 1

    elif len(data) == 3 :
        start = data[0]
        while start < data[1] :
            result.append(start)
            start += data[2]
            start = float(f"{start:.5}")

    return result


print(tuple(new_range(data)))