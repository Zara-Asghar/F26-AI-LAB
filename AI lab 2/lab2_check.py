
from lab2_model import ClassroomAgent
agent = ClassroomAgent()
tests = [
    ("Repeated COOL", 29, True),
    ("Repeated COOL", 29, True),
    ("Boundary 20", 20, True),
    ("Boundary 26", 26, True),
    ("Change to WARM", 19, True),
    ("Repeated WARM", 19, True),
    ("Empty room", 29, False),
    ("Repeated ECO", 29, False),
    ("Change to IDLE", 24, True)
]
for name, temp, occupied in tests:
    previous = agent.previous_mode
    target, send = agent.act(temp, occupied)
    result = "SEND COMMAND" if send else "NO COMMAND"
    print(
        name,
        "| Previous:", previous,
        "| Percept:", (temp, occupied),
        "| Target:", target,
        "| Result:", result
    )
