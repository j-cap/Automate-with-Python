# englisch to pig latin translator

print("Enter the English message to translate to PigLatin")
message = input()

VOWELS = ("a", "e", "i", "o", "u")

words = message.split(" ")

for idx, word in enumerate(words):
    if word[0] in VOWELS:
        words[idx] = word + "yay"
    else:
        letters = word.split()