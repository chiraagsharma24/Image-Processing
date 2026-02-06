from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(script_dir, "Fig0304(a)(breast_digital_Xray).tif")

img = Image.open(img_path).convert("L")
img = np.array(img)

# Negative transformation: s = (L - 1) - r
negative_img = 255 - img

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Negative Image")
plt.imshow(negative_img, cmap='gray')
plt.axis('off')

plt.show()
