
# stopwatch.py - A simple stopwatch program
import time
# Display the program's instructions
print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit")
input()
print("Started.")
startTime = time.time()
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap {lapNum}: {totalTime}, {lapTime}", end="")
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("\nDone.")