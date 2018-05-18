import Bruteforce,time
trials = 100000
times = []

for trial in range(trials):
    start = time.time()
    Bruteforce.Bruteforce()
    end = time.time()
    times.append(end-start)

print("Completed " + str(trials) + " trials with a mean of " + str((sum(times)/trials) * 1000) + " milliseconds!")