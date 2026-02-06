from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0314(a)(100-dollars).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.uint8)

plt.figure(figsize=(12,8))

plt.subplot(3,3,1)
plt.title("(a) Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

for i in range(8):
    bit_plane = (img >> (7 - i)) & 1
    bit_plane = bit_plane * 255 

    plt.subplot(3,3,i+2)
    plt.title(f"Bit Plane {8 - i}")
    plt.imshow(bit_plane, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()
