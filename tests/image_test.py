import os
import random
from PIL import Image

# path = "/Users/amy/Documents/DailyDianxia/images"
# files = os.listdir(path)
# d = random.choice(files)
# print(d)

# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'images')
# print(dirname)
# print(filename)

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'images')
files = os.listdir(path)
fileName = random.choice(files)
filePathName = "images/" + fileName
print(filePathName)
im = Image.open(filePathName)
im.show()