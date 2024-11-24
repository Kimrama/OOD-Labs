def insertion_sort(data) :
    l = len(data)
    for i in range(1, l) :
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j] :
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        
data = [15, 12, 33, 4, 84, 110, 2, 1]
insertion_sort(data)
print(data)