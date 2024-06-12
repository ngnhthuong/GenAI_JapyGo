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
        - Thư giãn tại spa, thưởng thức các dịch vụ spa tại các khách sạn chúng tôi.
Các loại phòng của JAYPY Go Hotel:
1. Phòng Tiêu Chuẩn (Standard Room)
•	Mô tả: Phòng cơ bản với giường đôi hoặc giường đơn, phòng tắm riêng, TV, và tiện nghi cơ bản như wifi, minibar.
•	Tiện nghi: Giường thoải mái, bàn làm việc, TV màn hình phẳng, điều hòa, ấm đun nước, két sắt.
2. Phòng Cao Cấp (Superior Room)
•	Mô tả: Phòng rộng hơn với giường đôi hoặc giường lớn, tầm nhìn tốt hơn, và tiện nghi bổ sung như khu vực ngồi, máy pha cà phê.
•	Tiện nghi: Giường lớn, khu vực tiếp khách, ban công (nếu có), máy pha cà phê, TV lớn hơn.
3. Phòng Hạng Sang (Deluxe Room)
•	Mô tả: Phòng lớn hơn với trang thiết bị sang trọng hơn, có thể có ban công hoặc tầm nhìn đẹp, phòng tắm rộng hơn với bồn tắm.
•	Tiện nghi: Giường cỡ lớn, phòng tắm có bồn tắm, ban công hoặc cửa sổ lớn, khu vực làm việc.
4. Phòng Gia Đình (Family Room)
•	Mô tả: Thiết kế để phục vụ gia đình với nhiều giường hoặc khu vực phòng khách riêng biệt, có thể có giường phụ hoặc sofa giường.
•	Tiện nghi: Giường đôi và giường đơn, phòng khách, bếp nhỏ (nếu có), đồ chơi trẻ em.
5. Phòng Suite (Junior Suite, Executive Suite, Presidential Suite)
•	Mô tả: Phòng rộng với không gian sống và ngủ riêng biệt, tiện nghi cao cấp và có thể có khu vực bếp nhỏ.
•	Tiện nghi: Phòng ngủ riêng biệt, phòng khách, phòng tắm lớn, khu vực bếp nhỏ, dịch vụ đặc biệt như quản gia hoặc xe đưa đón.
6. Phòng Studio (Studio Room)
•	Mô tả: Phòng kết hợp không gian ngủ và không gian sống, thường có thêm bếp nhỏ.
•	Tiện nghi: Giường đôi, khu vực bếp, bàn làm việc, TV, điều hòa.
7. Phòng Liền Kề (Connecting Room)
•	Mô tả: Hai phòng liền kề có cửa thông nhau, phù hợp cho nhóm hoặc gia đình muốn ở gần nhau nhưng vẫn có sự riêng tư.
•	Tiện nghi: Giường đơn hoặc đôi, phòng tắm riêng cho mỗi phòng, cửa thông nhau.
8. Phòng Tiện Nghi Đặc Biệt (Accessible Room)
•	Mô tả: Thiết kế để phục vụ người khuyết tật, với không gian rộng hơn và các tiện nghi hỗ trợ đặc biệt.
•	Tiện nghi: Cửa rộng, phòng tắm có tay vịn, ghế tắm, giường điều chỉnh.
9. Phòng Thương Gia (Business Room)
•	Mô tả: Được trang bị để phục vụ du khách công tác với bàn làm việc lớn, kết nối internet tốc độ cao, và dịch vụ văn phòng.
•	Tiện nghi: Bàn làm việc, ghế văn phòng, đèn bàn, dịch vụ in ấn, máy pha cà phê.
10. Phòng Căn Hộ (Apartment Room)
•	Mô tả: Cung cấp đầy đủ tiện nghi của một căn hộ với phòng ngủ, phòng khách, và bếp.
•	Tiện nghi: Phòng khách, phòng ngủ, nhà bếp đầy đủ thiết bị, máy giặt, bàn ăn.
11. Phòng Chủ Đề (Themed Room)
•	Mô tả: Phòng thiết kế theo một chủ đề đặc biệt để tạo ra trải nghiệm khác biệt (ví dụ: chủ đề biển, cổ điển).
•	Tiện nghi: Trang trí theo chủ đề, đồ nội thất đặc biệt, dịch vụ hoặc tiện nghi phù hợp với chủ đề.
12. Phòng Penthouse (Penthouse Suite)
•	Mô tả: Phòng ở tầng cao nhất với tầm nhìn toàn cảnh, không gian rộng rãi và tiện nghi cao cấp nhất.
•	Tiện nghi: Sân thượng riêng, nhiều phòng ngủ, phòng tắm xa hoa, dịch vụ quản gia.
Chi tiết về giá
Chi tiết về giá
1.	Phòng Tiêu Chuẩn (Standard Room)
•	Giá/Đêm: 1,000,000 VND
•	Giá tuần (7 đêm): 6,300,000 VND (giảm 10%)
2.	Phòng Cao Cấp (Superior Room)
•	Giá/Đêm: 1,500,000 VND
•	Giá tuần (7 đêm): 9,450,000 VND (giảm 10%)
3.	Phòng Hạng Sang (Deluxe Room)
•	Giá/Đêm: 2,000,000 VND
•	Giá tuần (7 đêm): 12,600,000 VND (giảm 10%)
4.	Phòng Gia Đình (Family Room)
•	Giá/Đêm: 2,500,000 VND
•	Giá tuần (7 đêm): 15,750,000 VND (giảm 10%)
5.	Phòng Junior Suite
•	Giá/Đêm: 3,000,000 VND
•	Giá tuần (7 đêm): 18,900,000 VND (giảm 10%)
6.	Phòng Executive Suite
•	Giá/Đêm: 4,500,000 VND
•	Giá tuần (7 đêm): 28,350,000 VND (giảm 10%)
7.	Phòng Presidential Suite
•	Giá/Đêm: 7,000,000 VND
•	Giá tuần (7 đêm): 44,100,000 VND (giảm 10%)
8.	Phòng Studio (Studio Room)
•	Giá/Đêm: 2,200,000 VND
•	Giá tuần (7 đêm): 13,860,000 VND (giảm 10%)
9.	Phòng Liền Kề (Connecting Room)
•	Giá/Đêm: 2,800,000 VND
•	Giá tuần (7 đêm): 17,640,000 VND (giảm 10%)
10.	Phòng Tiện Nghi Đặc Biệt (Accessible Room)
•	Giá/Đêm: 1,800,000 VND
•	Giá tuần (7 đêm): 11,340,000 VND (giảm 10%)
11.	Phòng Thương Gia (Business Room)
•	Giá/Đêm: 2,000,000 VND
•	Giá tuần (7 đêm): 12,600,000 VND (giảm 10%)
12.	Phòng Căn Hộ (Apartment Room)
•	Giá/Đêm: 4,000,000 VND
•	Giá tuần (7 đêm): 25,200,000 VND (giảm 10%)
13.	Phòng Chủ Đề (Themed Room)
•	Giá/Đêm: 3,500,000 VND
•	Giá tuần (7 đêm): 22,050,000 VND (giảm 10%)
14.	Phòng Penthouse (Penthouse Suite)
•	Giá/Đêm: 10,000,000 VND
•	Giá tuần (7 đêm): 63,000,000 VND (giảm 10%)


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
    return "\n".join(cleaned_lines).strip()