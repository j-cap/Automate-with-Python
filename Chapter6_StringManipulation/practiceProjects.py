
# Table printer

def printTable(table):
    
    length = []
    for row in table:
        l = 0
        for element in row:
            if len(element) > l:
                l = len(element)
        length.append(l)

    for i in range(len(table[0])):
        for idx, row in enumerate(table):
            print(row[i].rjust(length[idx]), end=" ")
        print()
    

testTable = [
    ["apples", "oranges", "cherries"],
    ["Alice", "Bob", "Carolaaa"],
    ["Cats", "Dogs", "Ponies"]
]

if __name__ == "__main__":

    printTable(testTable)