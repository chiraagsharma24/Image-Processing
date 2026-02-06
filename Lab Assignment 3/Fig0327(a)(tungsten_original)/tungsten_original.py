from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Fig0327(a)(tungsten_original).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.float32)

M, N = img.shape
L = 256

m_G = np.mean(img)
sigma_G = np.std(img)

k0 = 0.4
k1 = 0.02
k2 = 0.4
E  = 4.0       

window_size = 15
pad = window_size // 2

padded = np.pad(img, pad, mode='reflect')
out = img.copy()

for i in range(M):
    for j in range(N):
        window = padded[i:i+window_size, j:j+window_size]

        m_S = np.mean(window)
        sigma_S = np.std(window)

        if (m_S <= k0 * m_G and
            k1 * sigma_G <= sigma_S <= k2 * sigma_G):
            out[i, j] = E * img[i, j]

out = np.clip(out, 0, 255).astype(np.uint8)

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.title("(a) Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("(b) Local Enhancement (Histogram Statistics)")
plt.imshow(out, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
