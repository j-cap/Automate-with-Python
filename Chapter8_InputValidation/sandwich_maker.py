
import pyinputplus as pyip

prompt_welcome = "Welcome to the Sandwich Maker :) \n"

print(prompt_welcome)
bread = pyip.inputChoice(["wheat", "white", "sourdough"])
protein = pyip.inputChoice(["chicken", "turkey", "ham", "tofu"])

want_cheese = pyip.inputYesNo(prompt="Do you want cheese?\n")
if want_cheese == "yes":
    cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"])

want_mayo = pyip.inputYesNo(prompt="Do you want mayo?\n")
want_mustard = pyip.inputYesNo(prompt="Do you want mustard?\n")
want_lettuce = pyip.inputYesNo(prompt="Do you want lettuce?\n")
want_tomato = pyip.inputYesNo(prompt="Do you want tomato?\n")

mayo = "mayo" if want_mayo else "empty"
mustard = "mustard" if want_mustard else "empty"
lettuce = "lettuce" if want_lettuce else "empty"
tomato = "tomato" if want_tomato else "empty"

nr_sandwiches = pyip.inputInt(prompt="How many ssandwhiches do you want?\n")

sandwich = [bread, protein, cheese, mayo, mustard, lettuce, tomato]
prices = {
    "wheat": 0.75,
    "white": 0.69,
    "sourdough": 0.82,
    "chicken": 1.4,
    "turkey": 1.5,
    "ham": 1.45,
    "tofu": 1.3,
    "cheddard": 0.4,
    "Swiss": 0.42,
    "mozzarella": 0.44,
    "mayo": 0.05,
    "mustard": 0.05,
    "lettuce": 0.1,
    "tomato": 0.1,
    "empty": 0
}

price = 0
for ingredient in sandwich:
    price += prices[ingredient]

print(f"\n One sandwich costs {round(price, 2)} $")
print(f"Your total order  {round(price * nr_sandwiches, 2)} $")