import itertools
import zipfile

passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'6. 압축파일 암호푸는 프로그램\암호1234.zip')

for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd = passwd.encode())
            print (f"비밀번호는 {passwd} 입니다")
            break
        except:
            pass