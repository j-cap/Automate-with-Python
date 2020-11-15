# bulletPointAdder.py - Adds Wikipedia bullet points to start of each line 
#                       of the text on the clipboard

import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars
newtext = []
for line in text.splitlines():
    newtext.append("* " + line)

text = "\n".join(newtext)
pyperclip.copy(text)