import os
import yt_dlp
import whisper
from gemini_api import call_gemini_api
import torch

# Kiểm tra xem có GPU hay không
device = "cuda" if torch.cuda.is_available() else "cpu"

# Tải mô hình Whisper lớn để chuyển âm thanh tiếng Việt sang văn bản
model = whisper.load_model("large", device=device)

# Hàm tải âm thanh từ link YouTube
def download_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "audio.wav"

# Hàm chuyển đổi âm thanh sang văn bản tiếng Việt và xử lý với Google Gemini
def transcribe_and_process_audio(youtube_url):
    # Tải audio từ link YouTube
    audio_file = download_audio_from_youtube(youtube_url)

    # Chuyển đổi âm thanh sang văn bản
    result = model.transcribe(audio_file, language="vi")
    transcript = result['text']

    # Gọi API Gemini để hoàn thiện văn bản
    processed_text = call_gemini_api(transcript, task="add_punctuation")

    # Gọi API Gemini để tóm tắt văn bản đã hoàn thiện
    summarized_text = call_gemini_api(processed_text, task="summarize")

    # Lưu processed_text vào file
    transcript_file = "transcript.txt"
    with open(transcript_file, "w", encoding='utf-8') as f:
        f.write(summarized_text)

    # Xóa file âm thanh sau khi xử lý
    os.remove(audio_file)

    return processed_text, summarized_text, transcript_file  # Trả về văn bản đã hoàn thiện, tóm tắt và file text
