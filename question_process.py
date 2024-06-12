import os
from groq import Groq
from fuzzywuzzy import fuzz, process

# Đặt API key của bạn từ GroqCloud ở đây
api_key = "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"

# Khởi tạo client của Groq
client = Groq(api_key=api_key)

# Bối cảnh của khách sạn Japy Go Hotel
context = """
Khách sạn của tôi là Japy Go Hotel. Địa chỉ của khách sạn chúng tôi ở 159 Thùy Vân, Phường Thắng Tam, Thành phố Vũng Tàu, Bà Rịa - Vũng Tàu. Người dùng có thể liên hệ số điện thoại 0123456789 để được hướng dẫn đặt phòng hoặc bạn có thể đặt trên trang web chính của chúng tôi. Khách sạn của bạn có những dịch vụ gì? Wifi, Netflix Premium, Bữa sáng, Đồ uống mini bar, Dịch vụ xe, Chỗ đỗ xe, Giặt ủi. Khi cần, Bạn có thể liên hệ khách sạn chúng tôi qua số điện thoại 0123456789. Khách sạn của chúng tôi phục vụ từ 8h đến 23h. Bạn có thể xem gợi ý hoạt động dựa theo thời tiết xung quanh khách sạn chúng tôi qua link sau: http://localhost:5173/weather-activity-suggestions.
"""

def generate_response(user_question):
    # Tạo prompt để gửi đến Groq dựa trên câu hỏi của khách hàng
    prompt = f"""
    You are a customer service representative at Japy Go Hotel in Vũng Tàu, Vietnam. Here is the context of your hotel:

    {context}   

    Respond to the customer's question professionally and politely, providing helpful and accurate information in Vietnamese.

    Customer's Question: {user_question}

    Response:
    """
    return ask_groq(prompt)

def ask_groq(prompt):
    try:
        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }

        chat_completion = client.chat.completions.create(**data)

        return clean_response(chat_completion.choices[0].message.content)

    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"

def clean_response(response):
    """
    Làm sạch phần ghi chú hoặc phần không mong muốn trong phản hồi.
    """
    # Xóa các phần ghi chú không mong muốn
    lines = response.split("\n")
    print(lines)
    cleaned_lines = [line for line in lines if not line.startswith("(Note:")]
    return "\n".join(cleaned_lines).strip()

