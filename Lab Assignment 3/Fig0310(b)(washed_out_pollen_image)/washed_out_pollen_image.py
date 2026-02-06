from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0310(b)(washed_out_pollen_image).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.uint8)

r1 = np.percentile(img, 10)
r2 = np.percentile(img, 90)

stretched = (img - r1) * (255 / (r2 - r1))
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

T = 140  

binary = np.zeros_like(stretched)
binary[stretched >= T] = 255

# Display
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.title("Input Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Contrast Stretched + Thresholded")
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
