from PIL import Image
from os import listdir

files = [f for f in listdir("./hires/noncriminal/")]

for file in files:
    img = Image.open("./hires/noncriminal/"+file)
    newIMG = img.resize((300,300))
    newIMG.save(file[0:-4]+"-300.png", "PNG")