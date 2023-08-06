class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(gird: List[List[str]], i: int, j: int, m: int, n: int) -> None:
            # skip this location, if it is out of grid
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            # skip this location, if it is not land
            if grid[i][j] != '1':
                return 

            # we set it to "*" to prevent dfs revisit and infinite loop
            gird[i][j] = "*"
            dfs(gird, i - 1, j, m, n)
            dfs(gird, i + 1, j, m, n)
            dfs(gird, i, j + 1, m, n)
            dfs(gird, i, j - 1, m, n)
            return 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    """
                    when find a new island, use dfs iterate whole island,
                    and set all "1" locations to new value "*"
                    """
                    dfs(grid, i, j, m, n)
                    res += 1
        return res 
