import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Untitled.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Untitled2.jpg', cv2.IMREAD_GRAYSCALE)

h, w = img1.shape
img2 = cv2.resize(img2, (w, h))

# 3a. Addition
img_add = cv2.add(img1, img2)
blend = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# 3b. Subtraction
img_sub = cv2.subtract(img1, img2)
diff = cv2.absdiff(img1, img2)

# 3c. Mean
print('Mean (OpenCV):', cv2.mean(img1))
print('Mean (NumPy):', np.mean(img1))
print('Std Dev:', np.std(img1))
print('Min:', np.min(img1), 'Max:', np.max(img1))

titles = ['Image 1', 'Image 2', 'Addition', 'Blended', 'Subtraction', 'Abs Diff']
images = [img1, img2, img_add, blend, img_sub, diff]
plt.figure(figsize=(10, 6))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
