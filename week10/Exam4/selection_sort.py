def selection_sort(data) :
    l = len(data)

    for i in range(l) :

        min_index = i
        for j in range(i, l) :
            if data[min_index] > data[j] : min_index = j

        data[i], data[min_index] = data[min_index], data[i]

        
data = [15, 12, 33, 4, 84, 110, 2, 1]
selection_sort(data)
print(data)