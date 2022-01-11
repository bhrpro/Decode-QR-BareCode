from pyzbar.pyzbar import decode
from PIL import Image
#Déclaration de l'image || Mettre le nom de l'image ex : image.png
img = Image.open('image.png')
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))
