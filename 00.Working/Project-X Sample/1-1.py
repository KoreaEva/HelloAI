# Print Hello Mars
print('Hello Mars')

# mission_computer_main.log의 내용 출력

# 파일 경로
file_path = "00.Working/Project-X Sample/data/mission_computer_main.log"

try:
    # 파일 열기
    with open(file_path, "r") as file:
        # 파일 내용 읽기
        file_content = file.read()
        # 화면에 출력
        print(file_content)
except FileNotFoundError:
    print(f"파일 '{file_path}'를 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")


# 보너스 과제 
try:
    # 파일 열기
    with open(file_path, "r") as file:
        # 파일 내용 읽기
        file_content = file.read()
        # 화면에 출력
        print(file_content)
except FileNotFoundError:
    print(f"파일 '{file_path}'를 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
