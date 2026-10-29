import heapq
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = []
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            continue
        processed.append(node)
        if node == goal:
            return g, path, processed, expanded
        expanded.append(node)
        for nxt, cost in graph.get(node, []):
            new_g = g + cost
            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(
                    pq,
                    (new_g + h[nxt], new_g, nxt, path + [nxt])
                )
    return None, [], processed, expanded
h_astar = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
h_ucs = {node: 0 for node in graph}
for name, h in [("A*", h_astar), ("UCS", h_ucs)]:
    cost, path, processed, expanded = search(
        graph, h, "S", "G"
    )
    print("\nAlgorithm:", name)
    print("Path:", path)
    print("Total Cost:", cost)
    print("Processed Nodes:", processed)
    print("Expanded Nodes:", expanded)
    print("Expansion Count:", len(expanded))