from typing import List
def main():
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
           ]
    assert numIslands(grid) == 1

    grid = []
    assert numIslands(grid) == 0
    
    print("All Tests Passed Succesfully")




def numIslands(grid: List[List[str]]) -> int:
    if grid is None: return 0
    islands = 0

    for rows in range(len(grid)):
        for columns in range(len(grid[rows])):
            if grid[rows][columns] == "1":
                bfs(grid, rows, columns)
                islands += 1
        
    return islands 

def bfs(grid: List[List[str]], rows: int, columns: int) -> None:
    if rows < 0 or rows >= len(grid) or columns < 0 or columns >= len(grid[0]):
        return None
    if grid[rows][columns] == "0":
        return None
    grid[rows][columns] = "0"
    # Coord is a 1, so we recursively pass again in all directions
    bfs(grid, rows - 1, columns) # top
    bfs(grid, rows, columns + 1) # right
    bfs(grid, rows + 1, columns) # bottom
    bfs(grid, rows, columns - 1) # left

main()