
# readCensusTable.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint
print("Opening workbook".center(35, "-"))
wb = openpyxl.load_workbook("../materials/censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]

countyData = {}
# TODO: Fill in county data with each county's population and tracts
print("Reading rows".center(35, "-"))
for row in range(2, sheet.max_row +1):
    # Each row in the spreadsheed has data for one census tract
    state = sheet["B"+str(row)].value
    county = sheet["C"+ str(row)].value
    pop = sheet["D" + str(row)].value

    # MAke sure the key for this state exists
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {"tracts":0, "pop":0})
    countyData[state][county]["tracts"] += 1
    countyData[state][county]["pop"] += int(pop)

# TODO: Open a new text file and write the contets oc countyData to it. 
print("Writing resutls".center(35, "-"))
resultFile = open("census2010.py", "w")
resultFile.write("allData = "+ pprint.pformat(countyData))
resultFile.close()
print("Done".center(35, "-"))