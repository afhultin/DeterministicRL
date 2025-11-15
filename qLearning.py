# Q-Learning 
#Adin hultin

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
    #q table
    Q = {}
    for s in states:
        Q[s] = [0] * len(actions)

    iterations = 0


    for k in range(Max_Iterations):

        iterations += 1
        change = False

        for s in states:
            if s in terminal_states:
                continue

            for i, a in enumerate(actions):

                s1 = apply(s, a)
                max_q_s1 = max(Q[s1])

                q_new = rewards[s1] + gamma * max_q_s1

                if q_new != Q[s][i]:
                    Q[s][i] = q_new
                    change = True

        if not change:
            break

    #policy
    policy = {}
    for s in states:
        if s in terminal_states:
            continue

        best_q = float("-inf")
        best_a = None

        for i, a in enumerate(actions):
            if Q[s][i] > best_q:
                best_q = Q[s][i]
                best_a = a

        policy[s] = best_a

    #output
    print(f"\ngamma = {gamma}")
    print(f"iterations = {iterations}")
    print(f"policy = {policy}")
    print(f"Q((0,0)) = {[round(x,3) for x in Q[(0,0)]]}")
    print(f"Q((2,2)) = {[round(x,3) for x in Q[(2,2)]]}")
