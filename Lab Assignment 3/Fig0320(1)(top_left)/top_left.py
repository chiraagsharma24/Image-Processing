from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0320(1)(top_left).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.uint8)

M, N = img.shape
L = 256

hist = np.zeros(L)
for r in range(L):
    hist[r] = np.sum(img == r)

p_rk = hist / (M * N)

cdf = np.cumsum(p_rk)

s = np.round((L - 1) * cdf).astype(np.uint8)

img_eq = s[img]

hist_eq = np.zeros(L)
for r in range(L):
    hist_eq[r] = np.sum(img_eq == r)

p_eq = hist_eq / (M * N)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Histogram Equalized Image")
plt.imshow(img_eq, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Histogram of Equalized Image")
plt.plot(range(L), p_eq, linewidth=1)
plt.xlabel("Gray level")
plt.ylabel("p(rk)")
plt.xlim([0,255])

plt.tight_layout()
plt.show()
