import gradio as gr
from audio_processing import transcribe_and_process_audio

# Xây dựng giao diện Gradio
interface = gr.Interface(
    fn=transcribe_and_process_audio,  # Hàm xử lý âm thanh
    inputs=gr.Textbox(label="YouTube URL"),  # Đầu vào là link YouTube
    outputs=[
        gr.Textbox(label="Văn bản đã xử lý"),      # Đầu ra 1: Văn bản đã thêm dấu câu
        gr.Textbox(label="Văn bản tóm tắt"),       # Đầu ra 2: Văn bản đã được tóm tắt
        gr.File(label="Tải xuống file transcript") # Đầu ra 3: File transcript để tải xuống
    ],
    title="Chuyển đổi và tóm tắt nội dung từ file âm thanh",
    description="Nhập link YouTube và nhận văn bản đã xử lý và tóm tắt từ hệ thống",  # Mô tả giao diện
)

# Chạy giao diện
if __name__ == "__main__":
    interface.launch(share=True)
