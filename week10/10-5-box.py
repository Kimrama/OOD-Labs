def test_pack(items, max_weight, k):
    current_weight = 0
    box_count = 1
    
    for item in items:
        if current_weight + item > max_weight:
            box_count += 1
            current_weight = item
            if box_count > k:
                return False
        else:
            current_weight += item
            
    return True

def find_minimum_max_weight(items, k):
    low = max(items)
    high = sum(items)
    
    while low < high:
        mid = (low + high) // 2
        
        if test_pack(items, mid, k):
            high = mid
        else:
            low = mid + 1
            
    return low

input_str = input("Enter Input : ")
left, right = input_str.split("/")
items = list(map(int, left.split()))
k = int(right)

min_weight = find_minimum_max_weight(items, k)
print(f"Minimum weigth for {k} box(es) = {min_weight}")