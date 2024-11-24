data = [int(i) for i in input("Enter Input : ").split(" ")]
def find_min(data_list, index=0, curr_min=None) :
    if index == len(data_list) - 1 : 
        print(f"Min : {curr_min}")
        return
    if index == 0 : 
        curr_min = data_list[index]
    else :
        if data_list[index] < curr_min :
            curr_min = data_list[index]
    find_min(data_list, index+1, curr_min)

        
find_min(data)
