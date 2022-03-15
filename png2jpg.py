import cv2 as cv
import os
b = 'Black'
w = 'White'
i = 0
dir = os.fsencode(f'/home/kimetsu/new/{w}')

for file in os.listdir(dir):
    print(i)
    filename = os.fsdecode(file)
    img = cv.imread(f'{w}/{filename}', cv.IMREAD_UNCHANGED)
    alpha = img[:,:,3] == 0
    img[alpha] = [255,255,255,255]
    newimg = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
    i = i + 1
    cv.imwrite(f'{w}Jpg/{filename}.jpg', newimg)