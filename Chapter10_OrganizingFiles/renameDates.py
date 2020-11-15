
# renameDates.py - Rename filenames with American MM-DD-YYYY data format
#                  to European DD-MM-YYYY

import re,shutil, os

datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-     # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|29)\d\d)   # four digits for the year
    (.*?)$          # all text after the date
""", re.VERBOSE)
# Loop over the files in the working directory.
for amerFilenname in os.listdir():
    mo = datePattern.search(amerFilenname)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + "-" + monthPart + "+-" + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath()
    amerFilenname = os.path.join(absWorkingDir, amerFilenname)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print(f"Renaming '{amerFilenname}' to '{euroFilename}'...")
    #shutil.move(amerFilenname, euroFilename) # uncomment after testing
    