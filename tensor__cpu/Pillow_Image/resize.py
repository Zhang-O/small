from PIL import Image
import os
'''
The mode attribute defines the number and names of the bands in the image, 
and also the pixel type and depth. Common modes are “L” (luminance) for greyscale images, 
“RGB” for true color images, and “CMYK” for pre-press images.
'''
read_dir = "C:/zhang/项目/身份证识别/img_data/zhangkaiguo2/"
write_dir = "C:/zhang/项目/身份证识别/img_data/zhangkaiguo3/"

p = "C:/zhang/项目/身份证识别/img_data/zhangkaiguo1/140122199708130026_康乐_照片反面.jpg"



def resize_img(rpath, wpath, filename):
    im = Image.open(rpath + filename)

    width, height = im.size
    print(im.size, im.format, im.mode)
    # im.show()

    ratio = width/1300

    re_im = im.resize((1300, int(height/ratio)))
    # re_im.show()

    # im.thumbnail((42, 42))
    re_im.save(wpath + filename)


for file in os.listdir(read_dir):


    resize_img(read_dir, write_dir, file)