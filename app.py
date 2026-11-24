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

    if "mưa" in question.lower():
        st.write("Mưa làm tăng thời gian giao hàng.")

    elif "tắc" in question.lower():
        st.write("Tắc nghẽn giao thông làm đơn hàng giao chậm hơn.")

    elif "hỏa tốc" in question.lower():
        st.write("Hỏa tốc giúp giảm thời gian giao hàng nhưng chi phí cao hơn.")

    else:
        st.write("Hãy hỏi về thời tiết, giao thông hoặc dịch vụ giao hàng.")

