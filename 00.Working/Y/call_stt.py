# 이 프로그램은 통화 녹음 파일은 *.m4a 파일을 읽어서 자막을 만드는 프로그램이다. 

import os
from pydub import AudioSegment
import whisper

def convert_m4a_to_wav(m4a_file_path, wav_file_path):
    # Load m4a file
    audio = AudioSegment.from_file(m4a_file_path, format="m4a")
    # Export as wav file
    audio.export(wav_file_path, format="wav")

def transcribe_audio(wav_file_path):
    model = whisper.load_model("large")
    result = model.transcribe(wav_file_path)
    return result["text"]

def process_m4a_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".m4a"):
            m4a_file_path = os.path.join(folder_path, file_name)
            wav_file_path = os.path.join(folder_path, file_name.replace(".m4a", ".wav"))
            txt_file_path = os.path.join(folder_path, file_name.replace(".m4a", ".txt"))
            
            # Convert m4a to wav
            print('Audio File converting.... ' + m4a_file_path)
            convert_m4a_to_wav(m4a_file_path, wav_file_path)
            
            # Transcribe audio to text
            print('Audio File transcribe.... ' + m4a_file_path)
            text = transcribe_audio(wav_file_path)
            
            # Save text to txt file
            print('Text File converting.... ' + m4a_file_path)
            with open(txt_file_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)
            
            # Optionally, remove the wav file after processing
            os.remove(wav_file_path)

# 사용 예시
AudioSegment.ffmpeg = r"C:\Users\young\Documents\GITHUB\HelloAI\ffmpeg.exe"
folder_path = r"C:\Users\young\Documents\GITHUB\HelloAI\00.Working\Y\call_records"
process_m4a_files(folder_path)
print('finish-------------------------------------------------------')