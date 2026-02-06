from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0312(a)(kidney).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.uint8)

L = 256  

A_high = 180
B_high = 255

slice_without_bg = np.zeros_like(img)
slice_without_bg[(img >= A_high) & (img <= B_high)] = L - 1

A_low = 40
B_low = 120

slice_with_bg = img.copy()
slice_with_bg[(img >= A_low) & (img <= B_low)] = L - 1

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("(a) Original Aortic Angiogram")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("(b) Slicing without Background")
plt.imshow(slice_without_bg, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("(c) Slicing with Background Preserved")
plt.imshow(slice_with_bg, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
