import requests

# Đặt API key của Google Gemini
api_key = 'AIzaSyD3Hu747dbztC-jogggDfZudh_zYg40PJg'  # Thay bằng API key thực của bạn

# URL API của Google Gemini (Gemini 1.5)
api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

# Hàm gọi API Google Gemini
def call_gemini_api(text):
    headers = {
        'Content-Type': 'application/json'
    }

    prompt = f"Hãy thêm dấu câu cho đoạn văn sau đây: {text}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        try:
            return result['candidates'][0]['content']['parts'][0]['text']
        except KeyError:
            return "Không tìm thấy câu trả lời hợp lệ."
    else:
        return f"Lỗi {response.status_code}: {response.text}"
