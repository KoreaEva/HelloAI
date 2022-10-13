import qrcode
import os

current_path = os.path.dirname(os.path.realpath(__file__))

current_file_path = current_path + "/" + 'qr코드모음.txt'
print(current_file_path)

with open(current_file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)