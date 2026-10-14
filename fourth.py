import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)
cv2.circle(img2, (150, 150), 120, 255, -1)

# 4a. AND
img_and = cv2.bitwise_and(img1, img2)

# 4b. OR
img_or = cv2.bitwise_or(img1, img2)

# 4c. Intersection (= AND)
intersection = cv2.bitwise_and(img1, img2)

# NOT (negative)
img_not = cv2.bitwise_not(img1)

# XOR bonus
img_xor = cv2.bitwise_xor(img1, img2)

titles = ['Rectangle', 'Circle', 'AND', 'OR', 'XOR', 'NOT']
images = [img1, img2, img_and, img_or, img_xor, img_not]
plt.figure(figsize=(10, 6))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
