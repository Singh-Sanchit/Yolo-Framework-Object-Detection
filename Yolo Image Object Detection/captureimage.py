import cv2
import datetime

name = str(datetime.datetime.now().strftime('%d-%b-%Y %H-%M'))
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
img_name = "{}.jpg".format(name)
cv2.imwrite(img_name, frame)
print("{} writ!".format(img_name))
cam.release()
cv2.destroyAllWindows()