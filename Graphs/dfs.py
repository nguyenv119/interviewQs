from typing import List

class Solution:

    check = set()
    # Intuition: A block of 1's is an island, what's a way to get all of consecutive ones? DFS
    # Idea: dfs across until all visited once (check if visited), once a block of 1's is finished, increment islands
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Recursively call dfs on each element in the grid, if it has not been visited
        When we see a 1, before calling dfs, we increment by 1
        Every 1 we mark as visited as to not revisit, we can add to set

        If it isnt in set(not visited), and is a 1, we visit, else, add to set
        Break out of dfs after its a 0, or out of bounds
        '''
        Solution.check = set()
        if grid == [[]]: return 0
        res = 0

        for rows in range(len(grid)):
            for col in range(len(grid[0])):
                if (rows, col) not in Solution.check:
                    if grid[rows][col] == "1":
                        res += 1
                        self.dfs(rows, col, grid)

        return res

    def dfs(self, rows: int, col: int, grid: List[List[str]]):
        if rows >= 0 and rows <= len(grid) - 1 and col >= 0 and col <= len(grid[0]) - 1:
            Solution.check.add((rows, col))
            if grid[rows][col] == "1":
                if (rows + 1, col) not in Solution.check: self.dfs(rows + 1, col, grid)
                if (rows, col + 1) not in Solution.check: self.dfs(rows, col + 1, grid)
                if (rows - 1, col) not in Solution.check: self.dfs(rows - 1, col, grid)
                if (rows, col - 1) not in Solution.check: self.dfs(rows, col - 1, grid)

    def test(self):
        grid = [[]]
        assert self.numIslands(grid) == 0

        grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]

        assert self.numIslands(grid) == 1
        grid = [
                ["1","0","1","0","1"],
                ["0","1","0","1","0"],
                ["1","0","1","0","1"],
                ["0","1","0","1","0"]
            ]
        assert self.numIslands(grid) == 10
        grid = [
                ["1","1","1","0","1"],
                ]
        assert self.numIslands(grid) == 2
        print("All Tests Passed Succesfully")

    def numIslandsBetter(self, grid: List[List[str]]) -> int:
        if grid is None: return 0
        islands = 0

        for rows in range(len(grid)):
            for columns in range(len(grid[rows])):
                if grid[rows][columns] == "1":
                    self.bfs(grid, rows, columns)
                    islands += 1
            
        return islands 

    def dfsBetter(self, grid: List[List[str]], rows: int, columns: int) -> None:
        if rows < 0 or rows >= len(grid) or columns < 0 or columns >= len(grid[0]):
            return None
        if grid[rows][columns] == "0":
            return None
        grid[rows][columns] = "0"
        # Coord is a 1, so we recursively pass again in all directions
        self.bfs(grid, rows - 1, columns) # top
        self.bfs(grid, rows, columns + 1) # right
        self.bfs(grid, rows + 1, columns) # bottom
        self.bfs(grid, rows, columns - 1) # left


Solution = Solution()
Solution.test()

