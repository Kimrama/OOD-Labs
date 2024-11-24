results = []
def generate_combinations(numbers, current=""):
    if current and int(current) not in results:
        results.append(int(current))
    
    for i in range(len(numbers)):
        generate_combinations(numbers[:i] + numbers[i+1:], current + str(numbers[i]))

def validate_and_generate(numbers):
    if not all(isinstance(num, int) for num in numbers):
        print("Invalid input")
        return
    for i in numbers :
        if i >= 10 : 
            print("Invalid input")
            return
    results.clear()
    generate_combinations(numbers)
    return sorted(set(results))


data = [a for a in input("Enter digits : ").split(" ")]
new_data = []
for i in data :
    if i.isnumeric() : new_data.append(int(i))
    else : new_data.append(i)
output1 = validate_and_generate(new_data)
if output1 != None : print("Output :",output1)