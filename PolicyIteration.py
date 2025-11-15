# Policy Iteration greedy
#Adin Hultin
import random

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
    (1,2):10,
    (2,3):20
}

# all others have 0 reward
for s in states:
    if s not in rewards:
        rewards[s] = 0

Max_Iterations = 20

def apply(s, a):
    x, y = s
    if s in terminal_states:
        return s
    if a == 'U': y += 1
    elif a == 'D': y -= 1
    elif a == 'L': x -= 1
    elif a == 'R': x += 1
    if (x,y) not in states:
        return s
    return (x,y)

gammas = [0.9, 0.5, 0.1]

for gamma in gammas:

    # generate policy
    policy = {}
    for s in states:
        if s not in terminal_states:
            policy[s] = random.choice(actions)

    iterations = 0

    # policy
    for k in range(Max_Iterations):

        iterations += 1

        # policy eval
        V = {s: 0 for s in states}

        for _ in range(Max_Iterations):
            change = False
            for s in states:
                if s in terminal_states:
                    continue
                s1 = apply(s, policy[s])
                old_v = V[s]

                # EXACT professor update rule:
                V[s] = max(V[s], rewards[s1] + gamma * V[s1])

                if V[s] != old_v:
                    change = True

            if not change:
                break

        #policy
        stable = True
        for s in states:
            if s in terminal_states:
                continue

            old_action = policy[s]
            best_v = float('-inf')
            best_a = None

            for a in actions:
                s1 = apply(s, a)
                v = rewards[s1] + gamma * V[s1]
                if v > best_v:
                    best_v = v
                    best_a = a

            policy[s] = best_a
            if best_a != old_action:
                stable = False

        if stable:
            break

    #output
    print(f"\ngamma = {gamma}")
    print(f"iterations = {iterations}")
    print(f"policy = {policy}")
    print(f"V((0,0)) = {round(V[(0,0)],3)}")
    print(f"V((2,2)) = {round(V[(2,2)],3)}")
