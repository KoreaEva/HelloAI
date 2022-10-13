import qrcode
import os

current_path = os.path.dirname(os.path.realpath(__file__))

current_file_path = current_path + "/" + 'qr코드모음.txt'

with open(current_file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
        
        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = current_path + '/' + qr_data + '.png'
        print(save_path)
        qr_img.save(save_path)