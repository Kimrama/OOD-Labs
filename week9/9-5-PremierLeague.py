termi = input("Enter Input : ").split("/")
print("== results ==")


def _sort_(data) :
    stat = []
    for i in data :
        d = i.split(",")
        stat.append([d[0], {'points': 3 * int(d[1]) + int(d[3])}, {"gd": int(d[4]) - int(d[5])}])

    #sort points
    for i in range(len(stat)) :
        for j in range(len(stat) - i - 1) :
            if stat[j][1]["points"] < stat[j + 1][1]["points"] : 
                t = list(tuple(stat[j]))
                stat[j] = list(tuple(stat[j + 1]))
                stat[j + 1] = t
    #sort gp
    for i in range(len(stat)) :
        for j in range(len(stat) - i - 1) :
            if stat[j][1]["points"] == stat[j + 1][1]["points"] and stat[j][2]["gd"] < stat[j + 1][2]["gd"] : 
                t = list(tuple(stat[j]))
                stat[j] = list(tuple(stat[j + 1]))
                stat[j + 1] = t

    return stat
    

sorted_data = _sort_(termi)
for i in sorted_data :
    print(i)