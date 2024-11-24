def asteroid_collision(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack

x = input("Enter Input : ").split(",")
x = [int(i) for i in x]
print(asteroid_collision(x)) 
