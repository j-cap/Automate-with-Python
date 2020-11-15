
test = open("test.txt", "r")

text = test.read().split()

for idx, word in enumerate(text):
    dot = False
    if word[-1] == ".":
        word = word[:-1]
        dot = True
    if word.lower() in ["adjective", "noun", "verb"]:
        newword = input(f"Please enter a {word.lower()}: \n")
        if dot: newword = newword + "."
        text[idx] = newword

print(f"Write the following text to file: \n {' '.join(text)}")
newfile = open("test_new.txt", "w")
newfile.write(" ".join(text))
newfile.close()
