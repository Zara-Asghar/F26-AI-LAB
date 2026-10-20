
def check_application(score, documents_complete, attendance, similarity):
    problems = []

    if score < 70:
        problems.append("Score is below 70")

    if not documents_complete:
        problems.append("Documents are incomplete")

    if attendance < 80:
        problems.append("Attendance is below 80%")

    if similarity > 20:
        problems.append("Similarity is above 20%")

    if problems:
        decision = "Hold"
        reason = "; ".join(problems)
    else:
        decision = "Review"
        reason = "All four conditions are satisfied"

    return decision, reason


test_cases = [
    {
        "name": "Successful case",
        "score": 82,
        "documents_complete": True,
        "attendance": 90,
        "similarity": 10,
        "expected": "Review"
    },
    {
        "name": "Low attendance",
        "score": 82,
        "documents_complete": True,
        "attendance": 79,
        "similarity": 10,
        "expected": "Hold"
    },
    {
        "name": "High similarity",
        "score": 82,
        "documents_complete": True,
        "attendance": 90,
        "similarity": 21,
        "expected": "Hold"
    },
    {
        "name": "Threshold boundary",
        "score": 70,
        "documents_complete": True,
        "attendance": 80,
        "similarity": 20,
        "expected": "Review"
    }
]


for case in test_cases:
    actual, reason = check_application(
        case["score"],
        case["documents_complete"],
        case["attendance"],
        case["similarity"]
    )

    print("\nTest:", case["name"])
    print("Input:", {
        "score": case["score"],
        "documents_complete": case["documents_complete"],
        "attendance": case["attendance"],
        "similarity": case["similarity"]
    })
    print("Expected result:", case["expected"])
    print("Actual result:", actual)
    print("Reason:", reason)

    assert actual == case["expected"]

print("\nAll four tests passed successfully!")
