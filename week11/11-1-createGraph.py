data = input("Enter : ").split(",")
v = []
e = []
for i in data :
    a, b = i.split(" ")
    if a not in v : v.append(a)
    if b not in v : v.append(b)
    e.append((a, b))
v = sorted(v)
print("    " + "  ".join(v))
for i in v :
    print(f"{i} : ", end="")
    adj = []
    for j in v :
        if (i, j) in e : adj.append("1")
        else : adj.append("0")
    print(", ".join(adj))    
