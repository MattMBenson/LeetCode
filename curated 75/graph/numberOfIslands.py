from typing import *
def numberIslands(grid: List[List[str]]) -> int:
    count = 0
    for i in range(0,len(grid)):
        for j in range (0,len(grid[i])):
            if grid[i][j] == "1":
                count += 1
                BFS(grid, i, j)
    
    return count

def BFS(grid, i, j):
    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0"):
        return

    grid[i][j] = "0"
    BFS(grid, i+1, j)
    BFS(grid, i-1, j)
    BFS(grid, i, j+1)
    BFS(grid, i, j-1)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numberIslands(grid))

