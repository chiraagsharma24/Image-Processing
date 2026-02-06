from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

gammas = [3.0, 4.0, 5.0]

script_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(script_dir, "Fig0309(a)(washed_out_aerial_image).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.float32)

img_norm = img / 255.0

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.title("(a) Original Aerial Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

for i, g in enumerate(gammas):
    transformed = img_norm ** g

    transformed = (transformed * 255).astype(np.uint8)

    plt.subplot(2,2,i+2)
    plt.title(f"(b–d) γ = {g}")
    plt.imshow(transformed, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()
