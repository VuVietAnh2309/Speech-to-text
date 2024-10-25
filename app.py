import gradio as gr
from audio_processing import transcribe_and_process_audio

# Xây dựng giao diện Gradio
interface = gr.Interface(
    fn=transcribe_and_process_audio,  # Hàm xử lý âm thanh
    inputs=gr.Textbox(label="Youtube URL"),  # Đầu vào là link YouTube
    outputs=[
        gr.Textbox(label="Văn bản đã xử lý"),  # Đổi tên output 1 thành "Văn bản đã xử lý"
        gr.File(label="Tải xuống file transcript")  # Thêm phần tải xuống file transcript
    ],
    title="Automatically translate audio files into text",  # Tiêu đề giao diện
    description="Nhập link YouTube và nhận transcript từ hệ thống",  # Mô tả giao diện
)

# Chạy giao diện
if __name__ == "__main__":
    interface.launch(share=True)
