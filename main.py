import cv2

image = cv2.imread("images/test.jpg")

print("Gambar berhasil dibaca!")
print("Ukuran gambar:", image.shape)

cv2.imshow("Gambar Saya", image)

cv2.waitKey(0)
cv2.destroyAllWindows()