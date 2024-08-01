import os
from pydub import AudioSegment
import whisper

model = whisper.load_model("medium", device='cuda')

def convert_m4a_to_wav(m4a_file_path, wav_file_path):
    audio = AudioSegment.from_file(m4a_file_path, format="m4a")
    audio.export(wav_file_path, format="wav")

def format_timestamp(seconds):
    milliseconds = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def transcribe_audio_to_srt(wav_file_path, srt_file_path):
    result = model.transcribe(wav_file_path, fp16=False)
    
    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(result["segments"]):
            start = format_timestamp(segment["start"])
            end = format_timestamp(segment["end"])
            text = segment["text"]
            srt_file.write(f"{i + 1}\n")
            srt_file.write(f"{start} --> {end}\n")
            srt_file.write(f"{text}\n\n")
 

def process_m4a_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    files = os.listdir(folder_path)
    total_files = len(files)

    i = 0
    for file_name in files:
        if file_name.endswith(".m4a"):
            m4a_file_path = os.path.join(folder_path, file_name)
            wav_file_path = os.path.join(folder_path, file_name.replace(".m4a", ".wav"))
            srt_file_path = os.path.join(folder_path + '\\text_files', file_name.replace(".m4a", ".txt"))
            
            if not os.path.exists(m4a_file_path):
                print(f"File not found: {m4a_file_path}")
                continue
            
            i = i + 1
            print(f"Processing file: {total_files}/{i} -------{m4a_file_path}")
            
            convert_m4a_to_wav(m4a_file_path, wav_file_path)
            transcribe_audio_to_srt(wav_file_path, srt_file_path)
            
            os.remove(wav_file_path)
            #print(f"Removed temporary WAV file----------- : {wav_file_path}")
            #print(f"Finished processing file----------- : {m4a_file_path}")
            print('----------------------------------------------------------------------------')

folder_path = r"C:\Users\young\Documents\GITHUB\HelloAI\00.Working\Y\call_records"
process_m4a_files(folder_path)
