from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.ndimage import gaussian_filter

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0334(a)(hubble-original).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.float32)

sigma = 4.0   
filtered = gaussian_filter(img, sigma=sigma)

filtered_norm = (filtered - filtered.min()) / (filtered.max() - filtered.min())

T = 0.6   
binary = np.zeros_like(filtered_norm)
binary[filtered_norm >= T] = 1.0

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("(a) Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("(b) Gaussian Low-pass Filtered")
plt.imshow(filtered, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("(c) Thresholded Image")
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
