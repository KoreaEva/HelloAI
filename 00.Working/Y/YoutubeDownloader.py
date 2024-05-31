from pytube import YouTube
from moviepy.editor import VideoFileClip
import whisper
import os
import re

file_name = ''
current_path = os.getcwd() 

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

key = "4047eaf8a74541beadacbad7b070099d"
endpoint = "https://api.cognitive.microsofttranslator.com/"
region = "koreacentral"

credential = TranslatorCredential(key, region)
text_translator = TextTranslationClient(endpoint=endpoint, credential=credential)

# 파일 경로에서 파일명만 가져오는 함수
def get_filename_from_path(file_path):
    return os.path.basename(file_path)

def download_youtube_video(url, download_path='.'):
    global file_name

    try:
        # YouTube 객체 생성
        yt = YouTube(url)
        
        # 가장 높은 화질의 스트림 선택
        stream = yt.streams.get_highest_resolution()
        
        # 다운로드 경로 지정
        downloaded_file = stream.download(output_path=download_path)

        file_name = get_filename_from_path(downloaded_file)
        
        print(f"동영상 다운로드 완료: {yt.title}")
        return downloaded_file
    except Exception as e:
        print(f"동영상 다운로드 중 오류 발생: {e}")
        return None

def extract_audio(video_path, audio_path):
    try:
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path,codec='mp3')
        print(f"오디오 추출 완료: {audio_path}")
    except Exception as e:
        print(f"오디오 추출 중 오류 발생: {e}")

def generate_subtitles(audio_path, srt_path):
    try:
        model = whisper.load_model("base")
        audio_file_path = os.path.join(current_path,audio_path)
        result = model.transcribe(audio_file_path)
        
        with open(srt_path, 'w', encoding='utf-8') as srt_file:
            for i, segment in enumerate(result['segments']):
                start_time = segment['start']
                end_time = segment['end']
                text = segment['text']
                
                srt_file.write(f"{i+1}\n")
                srt_file.write(f"{format_timestamp(start_time)} --> {format_timestamp(end_time)}\n")
                srt_file.write(f"{text}\n\n")
        
        print(f"SRT 파일 생성 완료: {srt_path}")
    except Exception as e:
        print(f"SRT 파일 생성 중 오류 발생: {e}")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def translate_srt_to_korean(input_srt_path, output_srt_path,source_lang="en", target_lang=['ko']):
    source_language = source_lang
    target_languages = target_lang
    translated_text = ""

    try:
        with open(input_srt_path, 'r', encoding='utf-8') as file:
            
            i=0
            for line in file:
                if i == 0:                                      # 자막번호
                    print(line.strip())                             
                    translated_text = translated_text + line
                if i == 1:                                      # 타임라인
                    print(line.strip())  
                    translated_text = translated_text + line
                elif i == 2:                                    # 자막 내용
                     print(line.strip())
                     input_text_elements = [ InputTextItem(text = line.strip()) ]

                     response = text_translator.translate(content = input_text_elements, to = target_languages, from_parameter = source_language)
                     translation = response[0] if response else None
                     translated_text = translated_text + translation.translations[0].text
                     print(translation.translations[0].text)

                elif i == 3:                                    # 자막 사이 공란
                    translated_text = translated_text + '\n\n'

                    i=0
                    continue
                
                i=i+1
            
            write_srt(output_srt_path, translated_text)

    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {input_srt_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

   
    #print(translated_text)
    return #translated_text

def write_srt(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# def translate_srt(file_path, output_path, source_lang="auto", target_lang="en"):
#     srt_content = read_srt(file_path)
    
#     # SRT 파일 파싱
#     subtitles = re.split(r'(\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n)', srt_content)
    
#     translated_subtitles = []
    
#     for i in range(1, len(subtitles), 3):
#         subtitle_block = subtitles[i] + subtitles[i + 1]
#         text = subtitles[i + 2]
#         translated_text = translate_text(text, source_lang, target_lang)
#         translated_subtitles.append(subtitle_block + translated_text + '\n')
    
#     translated_srt_content = ''.join(translated_subtitles)
    
#     write_srt(output_path, translated_srt_content)

# 사용 예시
# translate_srt('input.srt', 'translated_output.srt', source_lang="auto", target_lang="en")



# 실행 코드
video_url = input('Input download youtube url: ')
download_path = 'downloads'

video_file = download_youtube_video(video_url, download_path)
#video_file = ''
#file_name = ''

audio_path = 'downloads\\{0}.mp3'.format(file_name[0:-4])
srt_path = 'downloads\\{0}_en.srt'.format(file_name[0:-4])
#srt_path = 'C:\\Users\\young\\Documents\\Github\\HelloAI\\downloads\\hhd800.com@STARS-999._en.srt'
translated_srt_path = 'downloads\\{0}.srt'.format(file_name[0:-4])

#srt_path = 'C:\\Users\\young\\Documents\\Github\\HelloAI\\downloads\\Full Keynote Satya Nadella at Microsoft Build 2024_en.srt'
#translate_srt_path = 'C:\\Users\\young\\Documents\\Github\\HelloAI\\downloads\\Full Keynote Satya Nadella at Microsoft Build 2024.srt'

if video_file:
    extract_audio(video_file, audio_path)
    generate_subtitles(audio_path, srt_path)
    translate_srt_to_korean(srt_path, translated_srt_path, source_lang='ja')
