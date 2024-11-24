print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.")
print("Separate each row with a comma (,).")
data_maze = input("Enter the maze: ").split(",")
maze = []
print("Your maze:")
for i in data_maze :
    print(i)
for line in data_maze :
    maze.append(list(line))

def dfs_recursive(maze, position, end, visited):
    x, y = position
    if position == end:
        return True
    if position in visited:
        return False
    
    visited.add(position)
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] in {'.', 'E'}:
            if dfs_recursive(maze, (nx, ny), end, visited):
                if maze[nx][ny] != 'E':
                    maze[nx][ny] = '*'
                return True
    
    return False

def find_start_end(maze):
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    return start, end


def solve_maze(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        raise ValueError("Maze must have exactly one start (S) and one end (E)")
    
    visited = set()
    if dfs_recursive(maze, start, end, visited):
        maze[start[0]][start[1]] = 'S'  
        maze[end[0]][end[1]] = 'E'
        return True
    return False


if solve_maze(maze):
    print("Solution found:")
    for row in maze:
        print(''.join(row))
else:
    print("No solution found")
