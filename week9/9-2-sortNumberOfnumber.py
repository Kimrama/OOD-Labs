data = list(map(int, input("Enter list  of numbers: ").split(" ")))
num_list = []
count_dict = {}

for i in data :
    if i not in num_list : num_list.append(i)

for i in num_list :
    count = 0
    for j in data :
        if i == j : count += 1
    count_dict.update({i: count})

sort_dict = {}
while len(count_dict) != 0 :
    highest_val = None
    for i in count_dict.items() : 
        if highest_val is None : 
            highest_val = i
        elif i[1] > highest_val[1] :
            highest_val = i
    sort_dict.update({highest_val[0]: highest_val[1]})
    count_dict.pop(highest_val[0])
        

for i in sort_dict.items() :
    print(f"number {i[0]}, total: {i[1]}")