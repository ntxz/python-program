import cv2 as cv
src = cv.imread("E:/1.jpg")
cv.namedWindow("input image",cv.WINDOW_NORMAL)#可以改尺寸
cv.imshow("input image",src)
cv.waitKey(0) #等待键入，防止闪退
cv.destroyAllWindows()
