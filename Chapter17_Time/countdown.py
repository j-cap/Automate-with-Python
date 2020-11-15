
# countdown.py - A simple countdown script.
import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# TODO: At the end of the countdown, play a sound file
subprocess.Popen(["start", "..//materials//alarm.wav"], shell=True)