data = list(map(int, input("Enter Input : ").split(" ")))

def bb_sort(data) :
    data = list(tuple(data))
    for i in range(len(data)) :
        for j in range(len(data) - 1) :
            if data[j] > data[j + 1] :
                t = data[j]
                data[j] = data[j + 1]
                data[j + 1] = t
    return list(data)

run_list = []
sort_run_list = []
for i in range(len(data)) :
    run_list.append(data[i])
    sort_run_list = bb_sort(run_list)
    if len(run_list) % 2 == 0 :
            left = sort_run_list[len(run_list) // 2 - 1]
            right = sort_run_list[len(run_list) // 2]
            print(f"list = {run_list} : median = {float((left + right) / 2):.1f}")
    else :
        print(f"list = {run_list} : median = {float(sort_run_list[(len(run_list) // 2)]):.1f}") 
