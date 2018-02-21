import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def get_file_data(file_name):
    landmarks = open(file_name, 'r')
    landmarks = landmarks.readlines()
    landmarks = [item.rstrip() for item in landmarks]
    return landmarks


def save_images_without_name(file_name, plot_file_type):
    path = os.getcwd() + "/images/"
    img = Image.open(path + file_name + '.' + plot_file_type)
    return img


def save_images_with_name(name, img, fill, plot_file_type):
    width, height = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/System/Library/Fonts/SFCompactDisplay-Regular.otf", 512)
    if name == 'SanLuisObispo':
        draw.text((18 * width / 32, 100), name, fill=fill, font=font)
    else:
        draw.text((width / 32, 100), name, fill=fill, font=font)
    file_name = os.path.abspath(os.path.join('./images', name + '_text.' + plot_file_type))

    img.save(file_name)

    print('File saved to {}'.format(file_name))
