import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)