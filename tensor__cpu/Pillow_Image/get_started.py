from PIL import Image


im = Image.open('6164.png')

'''
The mode attribute defines the number and names of the bands in the image, 
and also the pixel type and depth. Common modes are “L” (luminance) for greyscale images, 
“RGB” for true color images, and “CMYK” for pre-press images.
'''
print(im.size, im.format, im.mode)
im.show()

# im.thumbnail((42, 42))
# im.save('./1.jpeg', "JPEG")
