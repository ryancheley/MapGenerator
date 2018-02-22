import os
import csv
from data_types import City
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        city = []
        for row in reader:
            c = City.create_from_dict(row)
            city.append(c)

        return city


def get_image_file_name(file_name, plot_file_type):
    path = os.getcwd() + "/images/"
    img = Image.open(path + file_name + '.' + plot_file_type)
    return img


def save_images_with_name(name, img, fill, plot_file_type):
    width, height = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/System/Library/Fonts/SFCompactDisplay-Regular.otf", 512)
    draw.text((width / 32, 100), name, fill=fill, font=font)

    file_name = os.path.abspath(os.path.join('./images', name + '_text.' + plot_file_type))

    img.save(file_name)

    print('File saved to {}'.format(file_name))
