# create low light image dataset

from PIL import ImageEnhance
import cv2
import matplotlib.pyplot as plt

from PIL import Image
from skimage import data, exposure, img_as_float
import os

root = "path_for_all_images"

root_zero = "root_zero_shot_data/"
img_list = os.listdir(root)


def adjust_brightness(img, brightness_factor):
    """Adjust brightness of an Image.

    Args:
        img (PIL Image): PIL Image to be adjusted.
        brightness_factor (float):  How much to adjust the brightness. Can be
            any non negative number. 0 gives a black image, 1 gives the
            original image while 2 increases the brightness by a factor of 2.

    Returns:
        PIL Image: Brightness adjusted image.
    """
    #if not _is_pil_image(img):
    #    raise TypeError('img should be PIL Image. Got {}'.format(type(img)))

    enhancer = ImageEnhance.Brightness(img)
    img1 = enhancer.enhance(brightness_factor)



    return img1
brithness = [0.2,0.3,0.4, 0.5, 0.6, 0.7,0.8, 0.9 ,1]
cnt = 1
for im in img_list:

    for b in brithness:
        img = Image.open(root + "/" + im)
        img_adj = adjust_brightness(img, b)

        img_adj.save(root_zero + "our_" + str(cnt) + '_' + str(b) +".png")
    cnt +=1
