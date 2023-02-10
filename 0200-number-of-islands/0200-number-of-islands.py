class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        
        m, n = len(grid), len(grid[0])
        
        check = [[False] * n for _ in range(m)]
        dq = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if check[i][j] or grid[i][j] == '0':
                    continue
                    
                cnt += 1  # 미개척지를 발견하면 cnt를 1 증가하고 연결된 땅을 모두 개척
                check[i][j] = True
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    
                    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nx = x + dx
                        ny = y + dy
                        
                        if 0 <= nx < m and 0 <= ny < n:
                            if not check[nx][ny] and grid[nx][ny] == '1':
                                check[nx][ny] = True
                                dq.append((nx, ny))
        for line in check:
            print(line)
        return cnt