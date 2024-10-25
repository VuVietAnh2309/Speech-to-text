# Chuyển Đổi Âm Thanh YouTube Thành Văn Bản và Xử Lý Văn Bản

Dự án này cung cấp một giao diện web đơn giản, cho phép người dùng nhập URL của YouTube, tải xuống âm thanh, chuyển đổi âm thanh thành văn bản bằng mô hình Whisper của OpenAI, và sau đó xử lý văn bản bằng cách thêm dấu câu với API Google Gemini. Văn bản đã được xử lý có thể được tải xuống dưới dạng file.

## Tính Năng

- Tải xuống âm thanh từ video YouTube.
- Chuyển đổi âm thanh thành văn bản tiếng Việt bằng mô hình Whisper.
- Cải thiện văn bản bằng cách thêm dấu câu thông qua API Google Gemini.
- Giao diện web Gradio dễ sử dụng.

## Yêu Cầu

Hãy đảm bảo rằng bạn đã cài đặt Python 3.7+ và các thư viện cần thiết được liệt kê trong file `requirements.txt`.

## Cài Đặt

1. Clone repository này:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Cài đặt các gói cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

3. Cài đặt FFmpeg (cần thiết cho xử lý âm thanh):
    - Trên Debian/Ubuntu:
      ```bash
      sudo apt-get install ffmpeg
      ```

    - Trên MacOS (dùng Homebrew):
      ```bash
      brew install ffmpeg
      ```

    - Trên Windows, tải về từ [trang web chính thức của FFmpeg](https://ffmpeg.org/download.html) và thêm vào hệ thống PATH.

4. Đăng nhập vào Hugging Face (nếu cần):
    ```bash
    huggingface-cli login
    ```

5. Thiết lập **API key của Google Gemini**. Thay thế placeholder trong file `gemini_api.py`:
    ```python
    api_key = 'your-api-key-here'
    ```

## Chạy Ứng Dụng

Để chạy ứng dụng, sử dụng lệnh sau:

```bash
python app.py
```

Lệnh này sẽ khởi chạy giao diện web Gradio, nơi bạn có thể nhập URL YouTube và ứng dụng sẽ trả về văn bản đã chuyển đổi và xử lý.

## Cách Sử Dụng

1. Mở giao diện Gradio trong trình duyệt web của bạn.
2. Nhập một URL YouTube hợp lệ chứa âm thanh mà bạn muốn chuyển đổi.
3. Ứng dụng sẽ tải xuống âm thanh, chuyển đổi nó thành văn bản, và thêm dấu câu vào văn bản.
4. Bạn có thể xem văn bản đã xử lý và tải xuống file văn bản.

## Cấu Trúc Thư Mục

- app.py: Script chính để khởi chạy giao diện Gradio.
- audio_processing.py: Chứa các hàm tải âm thanh từ YouTube và chuyển đổi nó thành văn bản bằng Whisper.
- gemini_api.py: Chứa hàm gọi API Google Gemini để xử lý văn bản.
- requirements.txt: Danh sách các gói Python cần thiết cho dự án.

## Lưu ý

- Dự án sử dụng mô hình Whisper của OpenAI để chuyển đổi giọng nói thành văn bản, hỗ trợ nhiều ngôn ngữ, bao gồm tiếng Việt.
- Đảm bảo rằng ffmpeg đã được cài đặt đúng cách và có thể truy cập từ hệ thống PATH.
- Dự án này sử dụng API Google Gemini để thêm dấu câu vào văn bản. Đảm bảo rằng API key của bạn hợp lệ và có đủ quyền truy cập.

## Đóng Góp
- Bạn có thể thoải mái fork repository này và thực hiện các thay đổi. Mọi đóng góp đều được hoan nghênh!