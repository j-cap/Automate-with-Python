
import pyinputplus as pyip 

while True:
    prompt = "Want to know how to keep an idiot buys for an hour?\n"
    response = pyip.inputYesNo(prompt)

    if response == "no":
        print("Thank you. Have a nice day.")
        break