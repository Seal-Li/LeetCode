# 接雨水
def waterTrap(heights):
    if len(heights) < 2:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = heights[0]
    right_max[n-1] = heights[n-1]

    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])
    
    for j in range(n-2, -1, -1):
        right_max[j] = max(right_max[j+1], heights[j])
    
    trap = 0
    for k in range(n):
        trap += min(left_max[k], right_max[k]) - heights[k]
    
    return trap

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(waterTrap(heights))