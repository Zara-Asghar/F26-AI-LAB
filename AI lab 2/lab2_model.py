
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None
    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"
        send_command = target != self.previous_mode
        self.previous_mode = target
        return target, send_command
agent = ClassroomAgent()
percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]
for step, percept in enumerate(percepts, 1):
    previous = agent.previous_mode
    target, send = agent.act(*percept)
    result = "SEND COMMAND" if send else "NO COMMAND"
    print(
        step,
        "Previous:", previous,
        "Percept:", percept,
        "Target:", target,
        "Result:", result
    )
