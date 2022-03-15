import cv2 as cv
import numpy as np
from colorutils import Color

hexs = ['#000000']
i = 0
# with open('Black.txt') as codes:
#     for code in codes:
#         hexs.append(f'{code}\b')

img = cv.imread('shit2.png', cv.IMREAD_UNCHANGED)

alpha = img[:,:,3]

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)

for hex in hexs:

    print(f'{hex}====> {i}' )
    color = Color(hex = f'{hex}')
    hue, sat, val = color.hsv

    rhue = int(hue)/2 - h
    rsat = (sat*255) - s

    hnew = np.mod( h + rhue, 180).astype(np.uint8)
    snew = np.mod(  s + rsat , 256).astype(np.uint8)

    hsv_new = cv.merge([hnew, snew, v])
    bgr_new = cv.cvtColor(hsv_new, cv.COLOR_HSV2BGR)
    bgra = cv.cvtColor(bgr_new, cv.COLOR_BGR2BGRA)

    bgra[:,:,3] = alpha

    i = i + 1
    cv.imwrite(f'{hex}.jpg', bgra)
