import streamlit as st

st.set_page_config(
    page_title="Dự đoán thời gian giao hàng",
    page_icon="🚚"
)

st.title("🚚 Hệ thống dự đoán thời gian giao hàng")

# ===== Nhập dữ liệu =====

distance = st.number_input(
    "Khoảng cách (km)",
    min_value=1,
    value=5
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
    min_value=0.1,
    value=1.0
)

# ===== Dự đoán =====

if st.button("Dự đoán"):

    result = distance * 3 + weight * 2

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

# ===== Chatbot =====

st.subheader("🤖 Chatbot Logistics")

question = st.text_input(
    "Đặt câu hỏi về giao hàng"
)

if st.button("Gửi câu hỏi"):

    q = question.lower()

    if (
        "thời tiết" in q
        or "mưa" in q
        or "nắng" in q
    ):
        st.write(
            "🌦️ Thời tiết ảnh hưởng trực tiếp đến thời gian giao hàng. Mưa lớn thường làm tăng thời gian giao hàng do tốc độ di chuyển giảm."
        )

    elif (
        "giao thông" in q
        or "kẹt xe" in q
        or "tắc đường" in q
        or "tắc" in q
    ):
        st.write(
            "🚦 Giao thông tắc nghẽn là một trong những nguyên nhân chính làm thời gian giao hàng tăng lên."
        )

    elif (
        "dịch vụ" in q
        or "nhanh" in q
        or "hỏa tốc" in q
    ):
        st.write(
            "⚡ Dịch vụ hỏa tốc có thời gian giao hàng ngắn hơn nhưng chi phí vận chuyển cao hơn."
        )

    elif (
        "dự đoán" in q
        or "ai" in q
        or "mô hình" in q
    ):
        st.write(
            "🤖 Hệ thống sử dụng mô hình AI Random Forest để hỗ trợ dự đoán thời gian giao hàng dựa trên dữ liệu lịch sử."
        )

    elif (
        "xin chào" in q
        or "hello" in q
        or "hi" in q
        or "chào" in q
    ):
        st.write(
            "👋 Xin chào! Tôi là Chatbot Logistics. Tôi có thể hỗ trợ các câu hỏi về giao hàng, thời tiết, giao thông và dự đoán thời gian giao hàng."
        )

    elif question.strip() == "":
        st.warning("Vui lòng nhập câu hỏi.")
    
    else:
        st.write(
            "💬 Tôi có thể hỗ trợ các câu hỏi liên quan đến thời tiết, giao thông, dịch vụ giao hàng và thời gian giao hàng dự kiến."
        )



