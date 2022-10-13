import numpy as np
import cv2

ff = np.fromfile(r'24. 사진을 그림으로 변환하기 (OpenCV)\여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) 
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)  

cv2.imshow('cartoon view', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()