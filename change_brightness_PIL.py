from PIL import ImageEnhance
import cv2
import matplotlib.pyplot as plt


import numpy as np
from PIL import Image
from skimage import data, exposure, img_as_float

img = Image.open('./data/img.BMP')


def adjust_brightness(img, brightness_factor, contrsat_factor):
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

    e = ImageEnhance.Contrast(img)
    img2 = e.enhance( contrsat_factor)

    return img1, img2 








img1, img2 = adjust_brightness(img, 1,5)


plt.imshow(img1)
plt.show()

plt.imshow(img2)
plt.show()


