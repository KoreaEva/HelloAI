import qrcode
import os

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

current_file_path = os.getcwd() + "/" + qr_data + '.png'
print(current_file_path)

qr_img.save(current_file_path)
