def counting_sort(arr, exp, base=10):
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        index = abs(arr[i] // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = abs(arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    rounds = 0
    positive_numbers = [num for num in arr if num >= 0]
    negative_numbers = [-num for num in arr if num < 0]

    max_positive = max(positive_numbers) if positive_numbers else 0
    max_negative = max(negative_numbers) if negative_numbers else 0

    exp = 1
    while max_positive // exp > 0 or max_negative // exp > 0:
        rounds += 1
        print("------------------------------------------------------------")
        print(f"Round : {rounds}")

        if max_positive // exp > 0:
            count = [[] for _ in range(10)]
            for num in positive_numbers:
                index = (num // exp) % 10
                count[index].append(num)
            for i in range(10):
                print(f"{i} : {' '.join(map(str, count[i]))}")

            counting_sort(positive_numbers, exp)

        if max_negative // exp > 0:
            count = [[] for _ in range(10)]
            for num in negative_numbers:
                index = (num // exp) % 10
                count[index].append(-num)
            for i in range(10):
                print(f"{i} : {' '.join(map(str, count[i]))}")

            counting_sort(negative_numbers, exp)
            negative_numbers = [-num for num in negative_numbers]

        exp *= 10

    arr[:] = negative_numbers[::-1] + positive_numbers
    print("------------------------------------------------------------")
    return rounds

input_str = input("Enter Input : ")
arr = list(map(int, input_str.split()))
original_arr = arr.copy()

print("------------------------------------------------------------")
rounds = radix_sort(arr)

print(f"{rounds} Time(s)")
print("Before Radix Sort :", " -> ".join(map(str, original_arr)))
print("After  Radix Sort :", " -> ".join(map(str, arr)))
