from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0323(a)(mars_moon_phobos).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.uint8)

L = 256
hist = np.zeros(L)

for r in range(L):
    hist[r] = np.sum(img == r)

hist_scaled = hist / 1e4

plt.figure(figsize=(6,4))

plt.bar(
    range(L),
    hist_scaled,
    width=1,
    color="#8fb3d9",
    edgecolor="#8fb3d9",
    alpha=0.8
)

plt.xlim(0, 255)
plt.ylim(0, 7.0)

plt.xticks([0, 64, 128, 192, 255])
plt.yticks([0, 1.75, 3.50, 5.25, 7.00])

plt.xlabel("Gray level")
plt.ylabel("Number of pixels (×10⁴)")

plt.grid(False)

plt.tight_layout()
plt.show()
