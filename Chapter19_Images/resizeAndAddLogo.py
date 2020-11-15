
# resizeAndAddLogo.py - Resizes all images in the current working directory
#                       to fit in a 300x300 square, and adds catlogo.png
#                       to the lower right corner

import os 
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
# Loop over all files in the working director
for fname in os.listdir("."):
    if not (fname.endswith(".png") or fname.endswith(".jpg")) or fname == LOGO_FILENAME:
        continue
    im = Image.open(fname)
    width, height = im.size
    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            widht = SQUARE_FIT_SIZE
        else:
            widht = int((SQUARE_FIT_SIZE/width)*height)
            height = SQUARE_FIT_SIZE
        # Resize the image
        print(f"Resizing {fname}")
        im = im.resize((width, height))
    # Add the logo
    print(f"Adding logo to {fname}")
    im.paste(logoIm, (width-logoWidth, height - logoHeight), logoIm)
    # Save changes
    im.save("withLogo_"+fname)





