import torch
from glob import glob

img_path = r'40. 사진에서 사람을 인식하여 분류하기\원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    results.save(r"40. 사진에서 사람을 인식하여 분류하기\이미지확인용")
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])] 
        print(tag)