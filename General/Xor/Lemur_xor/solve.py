import cv2

img1 = cv2.imread("flag.png")
img2 = cv2.imread("lemur.png")

dst = cv2.bitwise_xor(img1, img2)

cv2.imwrite('out.png', dst)
