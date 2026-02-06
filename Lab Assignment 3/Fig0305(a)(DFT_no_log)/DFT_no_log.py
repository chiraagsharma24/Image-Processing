from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(script_dir, "Fig0305(a)(DFT_no_log).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.float32)

# Log transformation: s = c * log(1 + r), c = 1
log_img = np.log(1 + img)

log_img = (log_img / log_img.max()) * 255
log_img = log_img.astype(np.uint8)

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Log Transformed Image")
plt.imshow(log_img, cmap='gray')
plt.axis('off')

plt.show()
