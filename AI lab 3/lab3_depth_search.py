graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        return "CUTOFF", None
    cutoff = False
    for n in graph[node]:
        if n not in path:
            status, result = dls(n, goal, limit - 1, path + [n])
            if status == "FOUND":
                return status, result
            if status == "CUTOFF":
                cutoff = True
    return ("CUTOFF", None) if cutoff else ("FAILURE", None)
def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit, [start])
        print("Limit:", limit, "Status:", status, "Path:", path)
        if status == "FOUND":
            return path
    return None
print("DLS Tests:")
for limit in range(1, 5):
    print("Limit:", limit, dls("A", "G", limit, ["A"]))
print("\nIDDFS Test:")
iddfs("A", "G", 4)