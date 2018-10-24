from time import sleep
from random import randint

N = 2               # Max 10 processes - you must change the size of niceness list
QUANTUM = 100

# Reportable statistics
alltime = 0
usedtime = [0 for i in range(N)]

# CPU vs I/O Bound ----------------------------------------------
""" CPU: run until whole process timeslice is used up  """
def run(pid, t):
    global alltime, usedtime
    alltime += t
    usedtime[pid] += t
    return 0


""" I/O: run until I/O event occurs randomly then switch tasks
def run(pid, t):
    global alltime, usedtime

    if t < 10:
        alltime += t
        usedtime[pid] += t
        return 0
    runtime = randint(QUANTUM // 10, t)
    if t - runtime <= 0:
        alltime += t
        usedtime[pid] += t
        return 0
    else:
        alltime += runtime
        usedtime[pid] += runtime
        return t - runtime
"""

# Equal vs Weighted priority of Round Robin ----------------------------

""" Equal 
def calculate_weights():
    return [QUANTUM for i in range(N)]
"""

""" Weights """
niceness = [0, 0]
print("NICE:: ", niceness, "\n")

def calculate_weights():
    w = [88761, 71755, 56483, 46273, 36291,
         29154, 23254, 18705, 14949, 11916,
         9548, 7620, 6100, 4904, 3906,
         3121, 2501, 1991, 1586, 1277,
         1024, 820, 655, 526, 423,
         335, 272, 215, 172, 137,
         110, 87, 70, 56, 45,
         36, 29, 23, 18, 15]
    timeslices = []

    w_nice = 0
    for i in range(N):
        w_nice += w[ niceness[i] + 20]

    for i in range(N):
        timeslices.append(int(QUANTUM * (w[ niceness[i] + 20 ] / w_nice)))

    return timeslices



if __name__ == '__main__':
    # Create processes - list with their weights (priorities)
    tasks = calculate_weights()
    print("TASKS: ", tasks, "\n")

    # Run process indefinitely
    while True:
        next = -1
        max_time = 0

        # Find process with largest available timeslice and choose it
        for pid in range(len(tasks)):
            if tasks[pid] > max_time:
                max_time = tasks[pid]
                next = pid

        if next != -1:
            t = tasks[next]

            # Run choosen process
            tasks[next] = run(next, tasks[next])
            sleep(1)

            # Print statistics
            print("\t\033[{};1m| {}  | {:20s} | CPU%: {:.2f} |\033[0m".format(
                  next + 91, chr(ord('A') + next),
                  '*' * ((t - tasks[next]) // 5),
                  usedtime[next] / alltime))
        else:
            # When all processes used up their timeslices recalculate!
            tasks = calculate_weights()
