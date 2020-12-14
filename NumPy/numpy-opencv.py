import cv2
import numpy

img = cv2.imread("smallgray.png",0)

print(img)

# slicing and indexing

print(img[0:2, 2:4])  # rows , columns
print(img[:, 1:3])
print(img[2, 4])

# iterating
# rows
for i in img:
    print(i)
# columns
for i in img.T:
    print(i)
# item by item
for i in img.flat:
    print(i)


# stacking numpy arrays
# stacks horizontally, takes a tuple as argument
img_Hstacked = numpy.hstack((img, img))
print(img_Hstacked)
# stacks vertically, takes a tuple as argument
img_Vstacked = numpy.vstack((img, img))
print(img_Vstacked)

# splitting
img_Hsplitted = numpy.hsplit(img_Hstacked, 2)
print(img_Hsplitted)
