from typing import List

# input: a 2D array of 1's and 0's (strings)
# output: number of islands (1's connected)
# algorithm: use the DFS algorithm to solve this: iterate through the grid, when reaches 1, start a dfs scan from it to all the neighbors which
# are also 1, and change all of the to 0. when finished, updated counter  
OFFSETS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initizlize variables
        res = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(pos):
            """scan through neigbors which are 1 and in bounds"""
            # check all neighbors in a loop
            i, j = pos
            grid[i][j] = '0'
            for offset in OFFSETS:
                new_i, new_j = i + offset[0], j + offset[1] # calculate offset of operation
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == '1': # if found a neighbor in range
                    dfs(pos=(new_i, new_j))            

        # iterate throgh the grid until 1 is found
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == '1'):
                    dfs(pos=(i, j)) # scan the grid
                    res += 1 # update number of islands when done scanning

        return res
