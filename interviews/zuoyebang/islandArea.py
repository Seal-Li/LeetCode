# 最大岛屿面积
def maxAreaOfIsland(grid):
    # 检查边界条件和非法输入
    if not grid or not grid[0]:
        return 0

    # 获取网格的行数和列数
    rows, cols = len(grid), len(grid[0])
    # 初始化最大岛屿面积为0
    max_area = 0

    # 定义DFS函数
    def dfs(r, c):
        # 如果坐标超出边界或者当前位置不是陆地，则返回0
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        # 将当前位置标记为已访问（水）
        grid[r][c] = 0
        # 初始化岛屿面积为1（当前位置）
        area = 1
        # 搜索上下左右四个方向
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    # 遍历网格中的每个点
    for i in range(rows):
        for j in range(cols):
            # 如果当前位置是陆地，则进行DFS搜索
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area

# 示例使用
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1]
]
print(maxAreaOfIsland(grid))