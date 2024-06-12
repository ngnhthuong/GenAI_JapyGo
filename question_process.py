import os
from groq import Groq

# Đặt API key của bạn từ GroqCloud ở đây
api_key = "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"

# Khởi tạo client của Groq
client = Groq(api_key=api_key)

# Bối cảnh của khách sạn Japy Go Hotel
context = """
Giám đốc của khách sạn JAPY Go Hotel là Huỳnh Thị Bích Tuyền. Cô ấy tuy có chiều cao hơi khiêm tốn nhưng là một người con gái rất xinh đẹp, luôn chu toàn trong mọi thứ. Hôm nay là ngày 13/6/2024. Khách sạn của tôi là Japy Go Hotel. Password wifi của khách sạn chúng tôi là “hoilamgi.” Địa chỉ của khách sạn chúng tôi ở 159 Thùy Vân, Phường Thắng Tam, Thành phố Vũng Tàu, Bà Rịa - Vũng Tàu. Nếu gặp một số trục trặc như: hỏng máy lạnh, máy nóng lạnh hỏng hoặc tivi hỏng, bạn có thể liên hệ lễ tân qua số điện thoại: 0123456789. Địa chỉ email của khách sạn chúng tôi là japygohotel@gmail.com. Người dùng có thể liên hệ số điện thoại 0123456789 để được hướng dẫn đặt phòng hoặc bạn có thể đặt trên trang web chính của chúng tôi. Khách sạn của bạn có những dịch vụ gì? Wifi, Netflix Premium, Bữa sáng, Đồ uống mini bar, Dịch vụ xe, Chỗ đỗ xe, Giặt ủi, Spa. Khi cần, Bạn có thể liên hệ khách sạn chúng tôi qua số điện thoại 0123456789. Khách sạn của chúng tôi phục vụ từ 8h đến 23h. Bạn có thể xem gợi ý hoạt động dựa theo thời tiết xung quanh khách sạn chúng tôi qua link sau: http://localhost:5173/weather-activity-suggestions. Gần khách sạn chúng tôi có những địa điểm bao gồm: Tượng Chúa Kitô Vua, Hải đăng Vũng Tàu, Chợ Xóm Lưới, Soho Coffee, Bạch Dinh, Khu du lịch Hồ Mây, Gành Hào, Ốc thiên nhiên, Lotte Mart, bãi biển (bãi trước)
Xung quanh khách sạn chúng tôi, bạn có thể thực hiện những hoạt động sau:
        - Đi dạo và tắm ở bãi trước, tham quan các địa điểm như Tượng Chúa Kitô Vua, Hải đăng Vũng Tàu.
        - Khám phá chợ Xóm Lưới để thưởng thức hải sản tươi sống
        - Ghé thăm các quán cà phê nổi tiếng như Soho Coffee để thư giãn và ngắm cảnh
        - Tham quan các khu du lịch, ghé thăm Bạch Dinh hoặc Khu du lịch Hồ Mây
        - Tắm biển hoặc lặn ngắm san hô dưới nước
        - Thưởng thức ẩm thực biển tại các nhà hàng hải sản nổi tiếng như Gành Hào hoặc Ốc thiên nhiên
        - Tham gia các hoạt động trong nhà như khám phá các bảo tàng hoặc các trung tâm mua sắm như Lotte Mart
        - Thư giãn tại spa, thưởng thức các dịch vụ spa tại các khách sạn chúng tôi
"""

# Biến để theo dõi việc chào hỏi ban đầu
greeting_done = False

def generate_response(user_question):
    # Tạo prompt để gửi đến Groq dựa trên câu hỏi của khách hàng
    prompt = f"""
    You are a customer service representative at Japy Go Hotel in Vũng Tàu, Vietnam. Here is the context of your hotel:

    {context}

    Respond to the customer's question professionally and politely, providing a concise and accurate response in Vietnamese. Greet only the first time, then provide direct and polite answers without greetings. Do not include any notes or unnecessary English phrases.

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
    Làm sạch phần ghi chú hoặc các câu tiếng Anh không mong muốn trong phản hồi.
    """
    # Xóa các phần ghi chú không mong muốn và các câu tiếng Anh không cần thiết
    lines = response.split("\n")
    cleaned_lines = [line for line in lines if not line.startswith("Note:") and "apologized" not in line]
    # Loại bỏ các câu tiếng Anh không cần thiết
    cleaned_lines = [line for line in cleaned_lines if not (line.startswith("(Tiếng Anh") or "We are" in line or "Note:" in line)]
    return "<br/>".join(cleaned_lines).strip()
