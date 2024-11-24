def bubble_sort(data) :
    l = len(data)

    for i in range(l) :
        for j in range(l - 1) :
            if data[j] > data[j + 1] :
                data[j], data[j + 1] = data[j + 1], data[j]

data = [15, 12, 33, 4, 84, 110, 2, 1]
bubble_sort(data)
print(data)