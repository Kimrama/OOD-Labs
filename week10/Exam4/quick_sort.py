def quick_sort(arr) :
    if len(arr) <= 1 :
        return arr
    else :
        pivot = arr[0]

        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        mid = [x for x in arr if x == pivot]

        return quick_sort(left) + mid + quick_sort(right)
    
data = [15, 12, 33, 4, 84, 110, 2, 1]
data = quick_sort(data)
print(data)