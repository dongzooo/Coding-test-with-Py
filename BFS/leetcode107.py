class Solution:
    # 클래스 멤버변수 선언
    grid: List[List[str]]  
    n_row: int
    n_col: int

    def BFS(self, start_i, start_j):
        queue = deque()
        queue.append((start_i, start_j))
        while queue:
            i, j = queue.popleft()
            self.grid[i][j] = '0'
            # 현재 위치에서 상하좌우 탐색해서 갈 수 있는 위치를 queue에 insert
            if i-1 >= 0 and self.grid[i-1][j] == '1' and (i-1, j) not in queue:
                queue.append((i-1, j))  # up
            if i+1 < self.n_row and self.grid[i+1][j] == '1' and (i+1, j) not in queue:
                queue.append((i+1, j))  # down
            if j-1 >= 0 and self.grid[i][j-1] == '1' and (i, j-1) not in queue:
                queue.append((i, j-1))  # left
            if j+1 < self.n_col and self.grid[i][j+1] == '1' and (i, j+1) not in queue:
                queue.append((i, j+1))  # right

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n_row, self.n_col = len(grid), len(grid[0])
        n_island = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.grid[i][j] == '1':
                    n_island += 1
                    self.BFS(i, j)
        return n_island
