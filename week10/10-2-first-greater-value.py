inp = input("Enter Input : ")
left = sorted(list(map(int, (inp.split("/")[0].split(" ")))))
right = list(map(int, (inp.split("/")[1].split(" "))))


for i in right :
    find = False
    for j in left :
        if j > i : 
            print(j)
            find = True
            break
    if not find : print("No First Greater Value")