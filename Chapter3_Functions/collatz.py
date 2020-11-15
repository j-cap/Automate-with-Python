
import sys, time

def collatz(number):
    if number % 2:
        number = 3 * number + 1
    else:
        number = number // 2
    print(number)
    return number

print("Please input an integer:")
try:
    num = int(input())
except ValueError:
    print("Please enter an integer!")
    sys.exit()

while True:
    num = collatz(number=num)
    time.sleep(0.1)
    if num == 1:
        sys.exit()