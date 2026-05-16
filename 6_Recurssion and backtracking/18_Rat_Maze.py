def is_safe(x, y, maze, visited, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

def solve(x, y, maze, n, path, visited, result):
    # Base case: destination reached
    if x == n - 1 and y == n - 1:
        result.append(path)
        return

    # Mark current cell as visited
    visited[x][y] = True

    # Move Down
    if is_safe(x + 1, y, maze, visited, n):
        solve(x + 1, y, maze, n, path + 'D', visited, result)

    # Move Left
    if is_safe(x, y - 1, maze, visited, n):
        solve(x, y - 1, maze, n, path + 'L', visited, result)

    # Move Right
    if is_safe(x, y + 1, maze, visited, n):
        solve(x, y + 1, maze, n, path + 'R', visited, result)

    # Move Up
    if is_safe(x - 1, y, maze, visited, n):
        solve(x - 1, y, maze, n, path + 'U', visited, result)

    # Backtrack
    visited[x][y] = False

def find_paths(maze):
    n = len(maze)
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = []
    if maze[0][0] == 1:
        solve(0, 0, maze, n, "", visited, result)
    return result

# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1]
    ]
    paths = find_paths(maze)
    print("All possible paths:")
    for p in paths:
        print(p)