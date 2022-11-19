import sys
sys.path.insert(0,'..')
import cv2
from letterbox import letterbox


path = "car.jpeg"
frame = cv2.imread(path)
window_name = 'frame'

cv2.imshow(window_name, frame)
cv2.waitKey(0)

frame, _ratio, (_dw, _dh) = letterbox(frame, 640, stride=32) # recommended for yolov7 input
cv2.imshow(window_name, frame)
cv2.waitKey(0)
cv2.destroyAllWindows() 