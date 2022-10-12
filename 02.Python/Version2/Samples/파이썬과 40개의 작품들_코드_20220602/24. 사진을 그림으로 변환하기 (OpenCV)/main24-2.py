import numpy as np
import cv2

ff = np.fromfile(r'24. 사진을 그림으로 변환하기 (OpenCV)\여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows")

cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange)
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)

cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

while True:
    
    if cv2.waitKey(100) == ord('q'):
        break
    
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    print("sigma_s_value:",sigma_s_value)
    print("sigma_r_value:",sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)  

    cv2.imshow("Trackbar Windows", cartoon_img)

cv2.destroyAllWindows() 
