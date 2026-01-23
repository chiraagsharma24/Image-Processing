import math
from PIL import Image

# Load image
img = Image.open("input.png").convert("RGB")
width, height = img.size
pixels = img.load()

# User Inputs
sx = float(input("Enter horizontal scaling factor: "))
sy = float(input("Enter vertical scaling factor: "))

angle = float(input("Enter rotation angle (degrees): "))
theta = math.radians(angle)

tx = int(input("Enter horizontal translation: "))
ty = int(input("Enter vertical translation: "))

shx = float(input("Enter horizontal shear factor: "))
shy = float(input("Enter vertical shear factor: "))

# Create output image
out_img = Image.new("RGB", (width, height), (0, 0, 0))
out_pixels = out_img.load()

# Affine Transformation Matrix
# Scaling
S = [
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1]
]

# Rotation
R = [
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta),  math.cos(theta), 0],
    [0, 0, 1]
]

# Shearing
Sh = [
    [1, shx, 0],
    [shy, 1, 0],
    [0, 0, 1]
]

# Translation
T = [
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
]

# Matrix Multiplication
def mat_mul(A, B):
    result = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Combined transformation matrix
M = mat_mul(T, mat_mul(Sh, mat_mul(R, S)))

# Apply Transformation 
for x in range(width):
    for y in range(height):
        X = x
        Y = y

        new_x = int(M[0][0]*X + M[0][1]*Y + M[0][2])
        new_y = int(M[1][0]*X + M[1][1]*Y + M[1][2])

        # Check bounds
        if 0 <= new_x < width and 0 <= new_y < height:
            out_pixels[new_x, new_y] = pixels[x, y]

# Save Output
out_img.save("output.jpg")
print("Affine transformation completed. Output saved as output.jpg")