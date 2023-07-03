from PIL import Image
import os

# im = Image.open(r'C:\Users\hp\Downloads\New folder\New folder\Images\book1act1cover.png')
# print(im)
# print(im.format, im.mode, im.size)
# im.show()


image_path = input(r'Paste image path:')
image = Image.open(image_path)
def image_resize():
    x = int(input('Length: '))
    y = int(input('Breadth: '))
    
    out = image.resize(( x , y ))
    out.show()

def rotate_image():
    
    
    pass

image_resize()    
    
    
    