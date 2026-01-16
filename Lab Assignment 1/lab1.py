import cv2
import numpy as np
import matplotlib.pyplot as plt

img_name = input("Image Link: ")
img = cv2.imread(img_name, 0)

if img is None:
    print("Image not found")
    exit()

h = img.shape[0]
w = img.shape[1]

if h > w:
    size = w
else:
    size = h

sh = (h - size) // 2
sw = (w - size) // 2

square_img = img[sh:sh+size, sw:sw+size]

print("pick spatial resolution:")
print("0 = 100x100")
print("1 = 200x200")
print("2 = 400x400")
print("3 = 800x800")
space_choice = int(input("enter 0-3: "))

if space_choice == 0:
    new_size = 100
elif space_choice == 1:
    new_size = 200
elif space_choice == 2:
    new_size = 400
else:
    new_size = 800

resized = cv2.resize(square_img, (new_size, new_size))

print("pick intensity:")
print("0 = 1 bit (2 levels)")
print("1 = 2 bit (4 levels)")
print("2 = 4 bit (16 levels)")
print("3 = 8 bit (256 levels)")
intensity_choice = int(input("enter 0-3: "))

if intensity_choice == 0:
    bits = 1
elif intensity_choice == 1:
    bits = 2
elif intensity_choice == 2:
    bits = 4
else:
    bits = 8

levels = 2 ** bits

quantized = resized / 255.0
quantized = quantized * (levels - 1)
quantized = quantized.astype(int)

f = open("encoded.bin", "wb")

header = (space_choice << 2) | intensity_choice
f.write(bytes([header]))

buffer = 0
count = 0

for i in range(new_size):
    for j in range(new_size):
        val = int(quantized[i][j])

        buffer = (buffer << bits) | val
        count += bits

        if count >= 8:
            out = buffer & 255
            f.write(bytes([out]))
            buffer = 0
            count = 0

if count > 0:
    buffer = buffer << (8 - count)
    f.write(bytes([buffer]))

f.close()
print("saved to encoded.bin")

print("decoding...")
f = open("encoded.bin", "rb")

header_data = f.read(1)
header_val = header_data[0]

space_idx = (header_val >> 2) & 3
intens_idx = header_val & 3

if space_idx == 0:
    img_size = 100
elif space_idx == 1:
    img_size = 200
elif space_idx == 2:
    img_size = 400
else:
    img_size = 800

if intens_idx == 0:
    bits = 1
elif intens_idx == 1:
    bits = 2
elif intens_idx == 2:
    bits = 4
else:
    bits = 8

decoded_img = np.zeros((img_size, img_size))
buffer = 0
count = 0

for i in range(img_size):
    for j in range(img_size):

        while count < bits:
            byte = f.read(1)
            if not byte:
                break
            buffer = (buffer << 8) | byte[0]
            count += 8

        shift = count - bits
        mask = (1 << bits) - 1
        val = (buffer >> shift) & mask

        decoded_img[i][j] = val

        buffer = buffer & ((1 << shift) - 1)
        count -= bits

f.close()

max_val = (2 ** bits) - 1
decoded_img = decoded_img / max_val * 255
decoded_img = decoded_img.astype(np.uint8)

plt.subplot(1, 2, 1)
plt.imshow(square_img, cmap='gray')
plt.title("original")

plt.subplot(1, 2, 2)
plt.imshow(decoded_img, cmap='gray')
plt.title("decoded")

plt.show()
