
def minimax(depth, index, is_max, scores, target):
    if depth == target:
        return scores[index]

    left = minimax(depth + 1, index * 2, not is_max,
                   scores, target)
    right = minimax(depth + 1, index * 2 + 1, not is_max,
                    scores, target)

    return max(left, right) if is_max else min(left, right)


def alphabeta(depth, index, is_max, scores, target,
              alpha, beta, counter):
    if depth == target:
        counter[0] += 1
        return scores[index]

    if is_max:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(
                depth + 1, index * 2 + i, False, scores,
                target, alpha, beta, counter))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(
                depth + 1, index * 2 + i, True, scores,
                target, alpha, beta, counter))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


scores = [3, 5, 2, 9, 3, 5, 2, 9]
target = 3

reordered = scores[4:8] + scores[0:4]

for name, leaves in [
    ("Original Order", scores),
    ("Reversed Order", reordered)
]:
    counter = [0]

    result1 = minimax(0, 0, True, leaves, target)
    result2 = alphabeta(
        0, 0, True, leaves, target,
        float('-inf'), float('inf'), counter
    )

    print("\n", name)
    print("Minimax Value:", result1)
    print("Alpha-Beta Value:", result2)
    print("Leaves Evaluated:", counter[0])
    print("Results Match:", result1 == result2)
