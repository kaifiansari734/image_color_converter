import cv2 as cv

import numpy as np

from colorutils import Color

hexs = ['#eb4034']
# hexs = ['#ff8500','#ff4500','#eb4034','#f20071']

img = cv.imread('new.png', cv.IMREAD_UNCHANGED)

alpha = img[:,:,3]

#bgr = img[:,:,0:3]

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

h, s, v = cv.split(hsv)

for hex in hexs:
    
    # print(f'h = {h} \n v={v} \n s={s}')
    # print(f'v={v} \n s={s}')

    # print(hex)

    color = Color(hex = f'{hex}')

    # print(color.hsv)

    hue, sat, val = color.hsv

    rhue = int(hue)/2 - h
    rsat = (sat*255) - s

    # rval = int(val)*255 - v
    # print( f"hue {rhue}\n", f"sat {rsat}\n",f"val {rval}\n")
    # print(f"sat {rsat}\n")

    hnew = np.mod( h + rhue, 180).astype(np.uint8)

    snew = np.mod(  s + rsat , 255).astype(np.uint8)

    # snew = 0 * s

    # vnew = np.mod( v + rval, 256).astype(np.uint8)
    # snew = rsat + s
    # print(f'hnew = {hnew}')
    # print(f'snew = {snew}')
    # print(f'vnew = {vnew}')

    hsv_new = cv.merge([hnew, snew, v])

    # print(hsv_new)

    bgr_new = cv.cvtColor(hsv_new, cv.COLOR_HSV2BGR)

    bgra = cv.cvtColor(bgr_new, cv.COLOR_BGR2BGRA)

    bgra[:,:,3] = alpha

    cv.imwrite(f'{hex}newimg.png', bgra)
    # cv.imwrite(f'{hex}newimg.png', bgr_new)
