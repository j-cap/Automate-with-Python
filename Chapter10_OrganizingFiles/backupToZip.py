
# backupToZip.py - Copies an entire folder and its content into 
#                  ZIP  file whose filename increments

import zipfile, os

def backupToZip(folder):
    # Back up the entire 'folder' into a ZIP file.
    folder = os.path.abspath(folder)
    # Figure out the filename based on what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) +"_"+str(number)+".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1
    # Create the ZIP file
    print(f"Creating {zipFilename}...")
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # Walk the entire folder tree and compress the file in each folder.
    for foldername, subfolder, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        # Add the current folder to the ZIP file
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(filename) +"_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # Dont back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()   
    print("Done.")

backupToZip("testfolder")


