from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

gamma_monitor = 2.5
gamma_correct = 1 / gamma_monitor   

script_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(script_dir, "Fig0307(a)(intensity_ramp).tif")

img = Image.open(img_path).convert("L")
img = np.array(img, dtype=np.float32)

img_norm = img / 255.0

# (b) Image as viewed on monitor with gamma = 2.5
monitor_img = img_norm ** gamma_monitor

# (c) Gamma-corrected image
gamma_corrected = img_norm ** gamma_correct

# (d) Corrected image viewed on same monitor
final_view = gamma_corrected ** gamma_monitor

monitor_img = (monitor_img * 255).astype(np.uint8)
gamma_corrected = (gamma_corrected * 255).astype(np.uint8)
final_view = (final_view * 255).astype(np.uint8)

# Display results
plt.figure(figsize=(10,8))


plt.subplot(2,2,1)
plt.title("(a) Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2,2,2)
plt.title("(b) Viewed on γ = 2.5 Monitor")
plt.imshow(monitor_img, cmap='gray')
plt.axis('off')

plt.subplot(2,2,3)
plt.title("(c) Gamma-corrected Image")
plt.imshow(gamma_corrected, cmap='gray')
plt.axis('off')

plt.subplot(2,2,4)
plt.title("(d) Corrected Image on Same Monitor")
plt.imshow(final_view, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
