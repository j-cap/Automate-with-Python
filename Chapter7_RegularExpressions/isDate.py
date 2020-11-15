
import re, pyperclip, sys



def main():

    dateRegex = re.compile(r"([0-3]*\d{1})\/([0|1]*\d{1})\/([1|2]\d{3})")

    text = pyperclip.paste()
    if len(text) == 0:
        print("Please select some text")

    dates = dateRegex.findall(text)
    if len(dates) == 0:
        print("No dates found")
        sys.exit()
    for date in dates:
        print("Is", '/'.join(date), "a correct date? \t ", check_date(date))
    

def check_date(date):

    """
    31 :Jan March Mai July
        August Octo Dec 

    30: April June
        Sep Nov 
    
    28: Feb
    """
    day, month, year = list(map(int, date))
    
    if is_leap(year):
        if month == 2:
            correct = day <= 29
        else:
            if month in [4, 6, 9, 11]:
                correct = int(day) <= 30
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                correct = day <= 31
            else:
                correct = False
    else: 
        if month == 2:
            correct = day <= 28
        else: 
            if month in [4, 6, 9, 11]:
                correct = day <= 30
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                correct = day <= 31
            else:
                correct = False
    return correct

def is_leap(y):
    y = int(y)
    if y % 4:
        l = False
    else:
        if y % 100:
            l = True
        else:
            if y % 400:
                l = False
            else:
                l = True
    return l 



if __name__ == "__main__":
    main()