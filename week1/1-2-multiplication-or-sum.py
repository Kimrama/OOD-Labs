print("*** multiplication or sum ***")
u_input = [int(i) for i in input("Enter num1 num2 : ").split(" ")]
print(f"The result is {u_input[0] + u_input[1]}") if (u_input[0] * u_input[1] > 1000) else print(f"The result is {u_input[0] * u_input[1]}")