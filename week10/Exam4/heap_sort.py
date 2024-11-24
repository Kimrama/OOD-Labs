# siftDown(list, parent, idx, upper) :
#     repeat :
#         if parent has two children :
#             if parent > both children :
#                 end subroutine
#             else :
#                 swap parent with the greatest child :
#                 set parent idx to child idx
#         else if parent has one child :
#             if parent > child :
#                 end subroutine
#             else :
#                 swap parent with greater child
#                 set parent idx to child idx
#         else :
#             parent has no child, end subroutine
# headpsort(list) :
# heapify(list)
# for (end = 0, end > 0, end--) :
#     swap(list, 0, end)
#     shifDown(list, 0, end)

def heapify(arr, n, i) :
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest] :
        largest = left

    if right < n and arr[right] > arr[largest] :
        largest = right

    if largest != i :
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heap_sort(arr) :
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1) :
        heapify(arr, n , i)

    for i in range(n - 1, -1, -1) :
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


data = [15, 12, 33, 4, 84, 110, 2, 1]
heap_sort(data)
print(data)