from PIL import Image
import numpy as np

width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        image_data[y, x] = [x, y, 128]

image = Image.fromarray(image_data)

image.save('output_image.tga')
