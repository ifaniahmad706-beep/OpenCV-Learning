import cv2

image = cv2.imread("images/test.jpg")

print("Tipe data:", type(image))
print("Ukuran gambar:", image.shape)
print("Pixel [0,0]:", image[0, 0])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Ukuran grayscale:", gray.shape)
print("Pixel grayscale [0,0]:", gray[0, 0])

cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()