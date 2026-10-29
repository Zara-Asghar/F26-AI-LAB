import heapq
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            continue
        print(
            "Selected:", node,
            "g =", g,
            "h =", h[node],
            "f =", f
        )
        if node == goal:
            return g, path
        for nxt, cost in graph.get(node, []):
            new_g = g + cost
            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                new_f = new_g + h[nxt]
                heapq.heappush(
                    pq,
                    (new_f, new_g, nxt, path + [nxt])
                )
    return None, []
cost, path = astar(graph, h, "S", "G")
print("Final Path:", path)
print("Total Cost:", cost)