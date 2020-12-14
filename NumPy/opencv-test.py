import cv2

# 0 -> gray scale
# 1 -> bgr
img_gray = cv2.imread("smallgray.png", 1)

print(img_gray)

cv2.imwrite("new-image-sameSmallGray.png", img_gray)
