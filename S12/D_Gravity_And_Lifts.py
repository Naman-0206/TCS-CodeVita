import heapq

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0  
    
    prev = [[None] * cols for _ in range(rows)]
    
    pq = [(0, start[0], start[1])]  
    
    while pq:
        current_dist, x, y = heapq.heappop(pq)
        
        if current_dist > dist[x][y]:
            continue

        directions = []
        if x == rows - 1:  # bottom row
            if y > 0 and grid[x][y - 1] != 1:  # left
                directions += [(0, -1)]
            if y < cols - 1 and grid[x][y + 1] != 1:  # right
                directions += [(0, 1)]

        if x > 0 and grid[x - 1][y] == 1:  # lift above
            directions += [(-1, 0)]

        if x < rows - 1 and grid[x + 1][y] == 1:  # current cell is stable
            if y > 0 and grid[x][y - 1] != 1:  # left
                directions += [(0, -1)]
            if y < cols - 1 and grid[x][y + 1] != 1:  # right
                directions += [(0, 1)]

        if x < rows - 1 and grid[x][y] == 0 and grid[x + 1][y] != 1:  # current cell is unstable
            directions = [(1, 0)]

        if grid[x][y] == 1:  # in lift
            directions = [(-1, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_dist = current_dist + 1
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    prev[nx][ny] = (x, y)
                    heapq.heappush(pq, (new_dist, nx, ny))
    
    if dist[end[0]][end[1]] != float('inf'):
        return dist[end[0]][end[1]] - 1, prev
    return "Impossible", None

def reconstruct_path(prev, start, end):
    path = []
    at = end
    while at:
        path.append(at)
        at = prev[at[0]][at[1]]
    path.reverse()
    return path if path[0] == start else []

n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

if grid[end[0]][end[1]] == 1 or (end[0] < n - 1 and grid[end[0] + 1][end[1]] != 1):
    print("Impossible", end="")
    exit()

shortest_path, prev = dijkstra(grid, start, end)
if shortest_path == "Impossible":
    print("Impossible", end="")
else:
    print(shortest_path, end="")
    # path = reconstruct_path(prev, start, end)
    # print("Path:", path)
