# Shell sort

def shell_sort(data) :

    l = len(data)
    gap = l // 2

    while gap > 0:
        for i  in range(gap, l) :
            temp = data[i]
            j = i

            while j >= gap and data[j - gap] > temp :
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp

        gap //= 2


data = [15, 12, 33, 4, 84, 110, 2, 1]
shell_sort(data)
print(data)