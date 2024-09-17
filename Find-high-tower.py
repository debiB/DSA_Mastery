from collections import deque
def solution(matrix, tower1, tower2):
    def inbound(x,y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
    visited_1 = set()
    visited_2 = set()
    tower_1 = deque([tower1])
    tower_2 = deque([tower2])
    highest_elevation = 0
    best_elevation = [0,0]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    while tower_1 and tower_2:
        r1x,  r1y = tower_1.popleft()
        for dx, dy in directions:
            nr1, nc1 = r1x+ dx, r1y +dy
            if inbound(nr1,nc1) and (nr1,nc1) not in visited_1 and matrix[nr1][nc1] >= matrix[r1x][r1y]:
                tower_1.append((nr1, nc1))
                visited_1.add((nr1, nc1))
            if (nr1,nc1) in visited_2:
                if highest_elevation < matrix[nr1][nc1]:
                    highest_elevation = matrix[nr1][nc1]
                    best_elevation = [nr1, nc1]
        
        r2x,  r2y = tower_2.popleft()
        for dx, dy in directions:
            nr2, nc2 = r2x+ dx, r2y +dy
            if inbound(nr2,nc2) and (nr2,nc2) not in visited_2 and matrix[nr2][nc2] >= matrix[r2x][r2y]:
                tower_2.append((nr2, nc2))
                visited_2.add((nr2, nc2))
            if (nr1,nc1) in visited_2:
                if highest_elevation < matrix[nr2][nc2]:
                    highest_elevation = matrix[nr2][nc2]
                    best_elevation = [nr2, nc2]
    

    return best_elevation
        
matrix = [
    [10, 8, 7, 3],
    [6, 5, 4, 3],
    [9, 6, 3, 2],
    [8, 7, 6, 1]
]

tower1 = (0,0)
tower2 = (3,3)
print(solution(matrix, tower1, tower2))



 