from collections import deque
def simulate_connection(nodes, edges):
    adj_list  = defaultdict(list)
    for u,v in edges:
        adj_list[u].append(v)
    for i in nodes:
        if i == 16:
            q.append((i,16))
    while q:
        for _ in range(len(q)):
            root, amount = q.popleft()
            for node, val in adj_list[root]:
                if amount - 1 > nodes[val]:
                    q.append((node,amount - 1))
    return node
