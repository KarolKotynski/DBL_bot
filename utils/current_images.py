from PIL import Image
import cv2
from mss import mss
import numpy as np


def current_image(area):
    left = area['left']
    top = area['top']
    width = area['width']
    height = area['height']
    mon = {'left': left, 'top': top, 'width': width, 'height': height}
    sct = mss()
    sct.get_pixels(mon)
    screen = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    img = np.array(screen)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
