data = [10, 5, 62, 45, 23, 77, 54, 2, 16, 9, 8]



def heapify(lst, n, i) :
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and lst[left] > lst[largest] : largest = left

    if right < n and lst[right] > lst[largest] : largest = right

    if largest != i : 
        lst[largest], lst[i] = lst[i], lst[largest]
        heapify(lst, n, largest)


def heap_sort(lst) :
    n = len(lst)

    for i in range((len(lst))//2 - 1, -1, -1) :
        heapify(lst, n, i) 


    for i in range(n - 1, 0, -1) :
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

heap_sort(data)
print(data)


    