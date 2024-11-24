print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.")
print("Separate each row with a comma (,).")
data_maze = input("Enter the maze: ").split(",")
maze = []
print("Your maze:")
for i in data_maze :
    print(i)
for line in data_maze :
    maze.append(list(line))

def find_start_pos(maze) :
    diameter_row = len(maze)
    diameter_col = len(maze[0])

    for row in range(diameter_row) :
        for col in range(diameter_col) :
            if maze[row][col] == 'S' : return (row, col)
    return None

def is_there_has_start(maze) :
    for row in maze :
        for col in row :
            if col == 'S' : return col
    return False
def is_there_has_end(maze) :
    for row in maze :
        for col in row :
            if col == 'E' : return col
    return False

def is_safe(maze, row, col, solution) :
    diameter_row = len(maze)    
    diameter_col = len(maze[row])    
    return 0 <= row < diameter_row and 0 <= col < diameter_col and maze[row][col] == '.' and solution[row][col] == '.'

def solve_maze_util(maze, row, col, solution) :

    diameter_row = len(maze)    
    diameter_col = len(maze[row]) 

    if 0 <= row < diameter_row and 0 <= col < diameter_col and maze[row][col] == 'E' : return True

    if is_safe(maze, row, col, solution) :

        maze[row][col] = '*'
        
        #N
        if solve_maze_util(maze, row - 1, col, solution) :
            return True

        #E
        if solve_maze_util(maze, row, col + 1, solution) :
            return True
        
        #S
        if solve_maze_util(maze, row + 1, col, solution) :
            return True
        
        #W
        if solve_maze_util(maze, row, col - 1, solution) :
            return True
        
        maze[row][col] = '.'
        return False
    return False

def solve_maze(maze) :

    solution = list(tuple(maze))
    start = find_start_pos(maze)


    if not is_there_has_end(maze) or not is_there_has_start(maze) : return None

    solution[start[0]][start[1]] = '.'
    if not (solve_maze_util(maze, start[0], start[1], solution)) :  
        solution[start[0]][start[1]] = 'S'
        
        return None
    solution[start[0]][start[1]] = 'S'

    return solution

sol = solve_maze(maze)

if sol == None : print("No solution found")
else :
    print("Solution found:")
    for i in sol :
        print("".join(i))


