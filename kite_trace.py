import cv2
import numpy as np

# Load image
img = cv2.imread("Test.jpeg")

if img is None:
    print("Image not found!")
    exit()

# Show image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



edges = cv2.Canny(gray, 50, 150)

cv2.imshow("Edges (Strings)", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


