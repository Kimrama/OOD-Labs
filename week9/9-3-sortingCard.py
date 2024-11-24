sign_val = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
num_val = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

print("Have fun with sort card")
inp = input("Enter Input: ").split("/")
data = inp[0].split(",")
cmd = inp[1]

def validation(data) :

    if data[0] == '' : return []
    filter_list = []
    for i in data :
        if i[0] not in sign_val.keys() or i[1:] not in num_val.keys() :
            print(f"Error: {i} is an invalid card")
        else :
            if i not in filter_list :
                filter_list.append(i)
            else :
                print(f"Error: Duplicate card found - {i}")
    data = filter_list
    return data
def symbolFirst(data) :
    

    for i in range(1, len(data)) :
        j = i
        while j > 0 and sign_val[data[j - 1][0]] > sign_val[data[j][0]] :
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
        while j > 0 and sign_val[data[j - 1][0]] == sign_val[data[j][0]] and num_val[data[j - 1][1]] > num_val[data[j][1]] :
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1


def numFirst(data) :
    for i in range(1, len(data)) :
        j = i
        while j > 0 and num_val[data[j - 1][1]] > num_val[data[j][1]] :
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
        while j > 0 and num_val[data[j - 1][1]] == num_val[data[j][1]] and sign_val[data[j - 1][0]] > sign_val[data[j][0]] :
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1


if len(data) :
    if cmd == 'symbol' :
        symbolFirst(data)
    else : 
        numFirst(data)
    print("Sorted cards :", end=" ")
    for i in data :
        print(i, end=" ")
else :
    print("No valid cards to sort.")