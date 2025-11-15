# Adin Hultin

states = [
    (0,0),(1,0),(2,0),
    (0,1),(1,1),(2,1),
    (0,2),(1,2),(2,2),
    (0,3),(1,3),(2,3)
]

terminal_states = {(1,1), (2,1), (1,2), (2,3)}

actions = ['U','D','L','R']

rewards = {
    (1,1):-10,
    (2,1):-20,
    (1,2): 10,
    (2,3): 20
}

# all others = 0 reward
for s in states:
    if s not in rewards:
        rewards[s] = 0

Max_Iterations = 30


def apply(s, a):
    x, y = s

    if s in terminal_states:
        return s

    if a == 'U': y += 1
    if a == 'D': y -= 1
    if a == 'L': x -= 1
    if a == 'R': x += 1

    if (x,y) not in states:
        return s

    return (x,y)

def follow_optimal_path(policy, start=(0,0)):
    path = []
    s = start
    visited = set()
    while s not in terminal_states:
        if s in visited: break
        visited.add(s)
        a = policy[s]
        if a is None: break
        path.append(a)
        s = apply(s, a)
    return path


gammas = [0.9, 0.5, 0.1]

for gamma in gammas:

    # initialize V
    V = {}
    for s in states:
        if s in terminal_states:
            V[s] = rewards[s]
        else:
            V[s] = 0

    # value iter.
    iterations = 0
    for _ in range(Max_Iterations):
        iterations += 1
        changed = False

        for s in states:
            if s in terminal_states:
                continue

            for a in actions:
                s1 = apply(s, a)

                if s1 in terminal_states:
                    new_val = rewards[s1]
                else:
                    new_val = rewards[s1] + gamma * V[s1]

                if new_val > V[s]:
                    V[s] = new_val
                    changed = True

        if not changed:
            break

    # policy
    policy = {}
    for s in states:
        if s in terminal_states:
            policy[s] = None
            continue

        best_a = None
        best_v = None

        for a in actions:
            s1 = apply(s, a)
            if s1 in terminal_states:
                v = rewards[s1]
            else:
                v = rewards[s1] + gamma * V[s1]

            if (best_v is None) or (v > best_v):
                best_v = v
                best_a = a

        policy[s] = best_a

    clean_policy = follow_optimal_path(policy)

    # output
    print(f"\ngamma = {gamma}")
    print(f"iterations = {iterations}")
    print(f"policy = {clean_policy}")
    print(f"V((0,0)) = {round(V[(0,0)], 3)}")
    print(f"V((2,2)) = {round(V[(2,2)], 3)}")
