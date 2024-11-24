def merge_sort(arr) :
    if len(arr) > 1 :

        mid = len(arr) // 2

        sub_left = arr[:mid]
        sub_right = arr[mid:]

        merge_sort(sub_left)
        merge_sort(sub_right)

        i = j = k = 0

        while i < len(sub_left) and j < len(sub_right) :
            if sub_left[i] < sub_right[j] :
                arr[k] = sub_left[i]
                i += 1

            else :
                arr[k] = sub_right[j]
                j += 1

            k += 1

        while i < len(sub_left) :
            arr[k] = sub_left[i]
            i += 1
            k += 1

        while j < len(sub_right) :
            arr[k] = sub_right[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array is:", arr)