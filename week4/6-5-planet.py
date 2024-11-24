def asteroid_collision(asteroids):
    def collide(remaining):
        if len(remaining) < 2:
            return remaining
        
        first, second, *rest = remaining
        
        if first > 0 and second < 0:
            if first > abs(second):
                return collide([first] + rest)
            elif first < abs(second):
                return collide([second] + rest)
            else:
                return collide(rest)
        else:
            return [first] + collide([second] + rest)
    
    return collide(asteroids)
    

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(x)
print(asteroid_collision(x))