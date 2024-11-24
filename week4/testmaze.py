def parse_maze(maze_str):
    rows = maze_str.split(',')
    n = len(rows)
    maze = []
    start = None
    end = None
    
    for i in range(n):
        row = []
        for j in range(n):
            if rows[i][j] == 'S':
                start = (i, j)
                row.append(0)
            elif rows[i][j] == 'E':
                end = (i, j)
                row.append(0)
            elif rows[i][j] == '#':
                row.append(1)
            else:  # '.'
                row.append(0)
        maze.append(row)
    
    return maze, start, end

def is_safe(maze, x, y, solution):
    n = len(maze)
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and solution[x][y] == 0

def solve_maze_util(maze, x, y, end, solution):
    if (x, y) == end:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, solution):
        solution[x][y] = 1

        if solve_maze_util(maze, x + 1, y, end, solution):
            return True

        if solve_maze_util(maze, x, y + 1, end, solution):
            return True

        if solve_maze_util(maze, x - 1, y, end, solution):
            return True

        if solve_maze_util(maze, x, y - 1, end, solution):
            return True

        solution[x][y] = 0
        return False

    return False

def solve_maze(maze_str):
    maze, start, end = parse_maze(maze_str)
    if not start or not end:
        return "Invalid maze input"

    n = len(maze)
    solution = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve_maze_util(maze, start[0], start[1], end, solution):
        return "No solution exists"

    output_maze = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i, j) == start:
                row.append('S')
            elif (i, j) == end:
                row.append('E')
            elif solution[i][j] == 1:
                row.append('*')
            elif maze[i][j] == 1:
                row.append('#')
            else:
                row.append('.')
        output_maze.append(''.join(row))
    
    return '\n'.join(output_maze)

maze_str = "S...#,#.#.#,.#..E"
solution = solve_maze(maze_str)

if isinstance(solution, str):
    print(solution)
else:
    print(solution)
