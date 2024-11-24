_input = [int(x) for x in input("Enter All Bid : ").split(" ")]
if (len(_input) == 1) : print("not enough bidder")
else :
    _input.sort(reverse=True)
    print("error : have more than one highest bid") if (max(_input) == _input[1]) else print(f"winner bid is {_input[0]} need to pay {_input[1]}")