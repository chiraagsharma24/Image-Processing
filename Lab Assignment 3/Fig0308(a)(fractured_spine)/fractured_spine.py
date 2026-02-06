from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

gammas = [0.6, 0.4, 0.3]

script_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(script_dir, "Fig0308(a)(fractured_spine).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.float32)

img_norm = img / 255.0

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.title("(a) Original MRI")
plt.imshow(img, cmap='gray')
plt.axis('off')

# (b)–(d) Power-law transformed images
for i, g in enumerate(gammas):
    # s = c * r^gamma, c = 1
    transformed = img_norm ** g

    # Scale to [0, 255]
    transformed = (transformed * 255).astype(np.uint8)

    plt.subplot(2,2,i+2)
    plt.title(f"(b–d) γ = {g}")
    plt.imshow(transformed, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()
