import streamlit as st

st.title("🚚 Hệ thống dự đoán thời gian giao hàng")

distance = st.number_input(
    "Khoảng cách (km)",
    min_value=1
)

weather = st.selectbox(
    "Thời tiết",
    ["Nắng", "Mưa nhẹ", "Mưa lớn"]
)

traffic = st.selectbox(
    "Tình trạng giao thông",
    ["Thông thoáng", "Trung bình", "Tắc nghẽn"]
)

service = st.selectbox(
    "Loại dịch vụ",
    ["Tiêu chuẩn", "Nhanh", "Hỏa tốc"]
)

weight = st.number_input(
    "Khối lượng hàng (kg)",
    min_value=0.1
)

if st.button("Dự đoán"):

    result = (
        distance * 3
        + weight * 2
    )

    if weather == "Mưa nhẹ":
        result += 5

    if weather == "Mưa lớn":
        result += 10

    if traffic == "Trung bình":
        result += 5

    if traffic == "Tắc nghẽn":
        result += 10

    if service == "Hỏa tốc":
        result -= 5

    st.success(
        f"⏱️ Thời gian giao hàng dự kiến: {result:.1f} phút"
    )

st.subheader("🤖 Chatbot Logistics")

question = st.text_input("Đặt câu hỏi")

if st.button("Gửi câu hỏi"):

    q = question.lower()

    if (
        "thời tiết" in q
        or "mưa" in q
        or "nắng" in q
    ):
        st.write(
            "Thời tiết là một trong những yếu tố ảnh hưởng đến thời gian giao hàng. Mưa lớn thường làm tăng thời gian giao hàng do tốc độ di chuyển bị hạn chế."
        )

    elif (
        "giao thông" in q
        or "kẹt xe" in q
        or "tắc đường" in q
        or "tắc" in q
    ):
        st.write(
            "Tình trạng giao thông ảnh hưởng trực tiếp đến thời gian giao hàng. Khi giao thông tắc nghẽn, thời gian giao hàng thường tăng đáng kể."
        )

    elif (
        "hỏa tốc" in q
        or "nhanh" in q
        or "dịch vụ" in q
    ):
        st.write(
            "Dịch vụ hỏa tốc có thời gian giao hàng nhanh nhất nhưng chi phí cao hơn dịch vụ tiêu chuẩn."
        )

    elif (
        "giao hàng" in q
        or "dự đoán" in q
        or "thời gian" in q
    ):
        st.write(
            "Hệ thống sử dụng các yếu tố như khoảng cách, thời tiết, giao thông và khối lượng hàng để dự đoán thời gian giao hàng."
        )

    else:
        st.write(
            "Tôi có thể trả lời các câu hỏi về thời tiết, giao thông, dịch vụ giao hàng và dự đoán thời gian giao hàng."
        )
        
    else:
        st.write("Hãy hỏi về thời tiết, giao thông hoặc dịch vụ giao hàng.")

