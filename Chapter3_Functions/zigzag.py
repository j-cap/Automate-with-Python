
import time, sys
indent = 0
indentIncreasing = True
try:
    while True:
        print(" "*indent, end="")
        print("*******", end="")
        print(" "*indent, end="")
        print("*******")
        time.sleep(0.05)
        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()