import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np


fig, ax = plt.subplots(nrows=2, ncols=3)
img = plt.imread('PyPict.jpg')

img_1 = img.copy()
img_1[:, :, 0] = 0
ax[0, 0].imshow(img_1)

img_2 = img.copy()
img_2[:, :, 2] = 0
ax[0, 1].imshow(img_2)

img_3 = Image.open('PyPict.jpg').convert('L')
ax[0, 2].imshow(np.array(img_3))

im = img.copy()
img_4 = (Image.fromarray(np.array(im))).filter(ImageFilter.CONTOUR)
ax[1, 0].imshow(img_4)

red = [1, 0, 0]
img_5 = img.copy()
ax[1, 1].imshow(img_5 * red)


# взято с сайта https://ru.haru-atari.com
def bright(source_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))

            red_color = int(r * brightness)
            red_color = min(255, max(0, red_color))

            green = int(g * brightness)
            green = min(255, max(0, green))

            blue = int(b * brightness)
            blue = min(255, max(0, blue))

            result.putpixel((x, y), (red_color, green, blue))
    return result


img_6 = bright('PyPict.jpg', 2)
ax[1, 2].imshow(img_6)
plt.savefig('My_pic.png')
plt.show()
