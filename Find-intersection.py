from collections import deque
def solution(arr, posA, posB):
    if posA == posB:
        return 0 
    visited = set([posA, posB, 0])
    q= deque([(posA, posB, 0)])
    while q:
        a , b, steps = q.popleft()
        if a == b:
            return steps
        curr_a = arr[a]
        curr_b = arr[b]
        if (curr_a, curr_b) not in visited:
            q.append((curr_a, curr_b, steps+1))
            visited.add((curr_a, curr_b))
    return -1

arr =  [1, 1]
startA = 0
startB = 1
print(solution(arr, startA, startB)) 


        
    


