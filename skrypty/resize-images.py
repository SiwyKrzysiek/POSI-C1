import cv2
from glob import glob

dim = (300, 300)

images = glob("*.png")
print(images)

for image in images:
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
    cv2.imwrite(f'Resized_{image}', resized)