import sys
import os
from PIL import Image

# # grab the first and second argument
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

# # check is new/ exist, if not create
path = os.getcwd()
new_path = path+f'\{png_folder}'
jpg_path = path+f'\{jpg_folder}'
isdir = os.path.isdir(new_path)

if not isdir:
    os.makedirs(new_path)

# # loop through Pokedex
for filename in os.listdir(jpg_path):
    if filename.endswith(".jpg"):
        name = os.path.splitext(filename)[0]
        img_path = jpg_path+f'\{filename}'
        img = Image.open(img_path)
        img.save(new_path+f"\{name}.png", 'png')
# # convert images to png
# # save to the new folder
