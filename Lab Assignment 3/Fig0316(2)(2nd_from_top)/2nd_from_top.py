from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0316(2)(2nd_from_top).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.uint8)

M, N = img.shape
L = 256

hist = np.zeros(L)
for r in range(L):
    hist[r] = np.sum(img == r)

p_rk = hist / (M * N)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Input Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Normalized Histogram p(rk)")
plt.plot(range(L), p_rk, linewidth=1)
plt.xlabel("Gray level (rk)")
plt.ylabel("p(rk)")
plt.xlim([0, 255])

plt.tight_layout()
plt.show()
