import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("car.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert BGR image to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the image to 300 x 300 pixels
resized_image = cv2.resize(rgb_image, (300, 300))

# Display the images
plt.figure(figsize=(10, 4))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(rgb_image)
plt.title("Original Image")
plt.axis("off")

# Grayscale image
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

# Resized image
plt.subplot(1, 3, 3)
plt.imshow(resized_image)
plt.title("Resized Image")
plt.axis("off")

plt.show()

# Save the grayscale image
cv2.imwrite("gray_output.jpg", gray_image)

print("Image processing completed successfully!")