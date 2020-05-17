class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        num_of_row = len(grid)
        num_of_column = len(grid[0])
        num_of_islands = 0
        neighbors = collections.deque()
        for i in range(num_of_row):
            for j in range(num_of_column):
                if grid[i][j] == '1':
                    neighbors.append((i,j))
                    grid[i][j] = '0'
                    num_of_islands += 1
                while neighbors:
                    a,b = neighbors.popleft()
                    for x,y in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
                        if num_of_row> x >=0 and num_of_column> y >=0 and grid[x][y]=='1':
                            grid[x][y] = '0'
                            neighbors.append((x,y))
        return num_of_islands