import cv2 as cv
import numpy as np

imm = "test.jpg"

img = cv.imread(imm, cv.IMREAD_COLOR)

x = img.shape[1]
y = img.shape[0]

a = 525
b = 25
c = 1000

pts1 = np.float32([[1159, 194], [1632, 332], [1265, 658], [791, 525]])
pts2 = np.float32([[a+1500, b + 1250], [c+1500, a + 1250], [a+1500, c + 1250], [b+1500, a + 1250]])

matrix = cv.getPerspectiveTransform(pts1, pts2)
result = cv.warpPerspective(img, matrix, (x + 1050, y + 2500))

gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray, 5)

'''circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 2, 10)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    x, y, r = circles[0][0], circles[0][1], circles[0][2]
    cv.circle(result, (x, y), r, (0, 255, 0), 10)
    cv.circle(result, (x, y), 5, (0, 255, 0), -1)'''

matrix = cv.getPerspectiveTransform(pts2, pts1)
result = cv.warpPerspective(img, matrix, (x, y))

cv.imshow('warp', result)

cv.waitKey(0)

cv.destroyAllWindows()
