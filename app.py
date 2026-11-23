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
    st.success("Thời gian giao hàng dự kiến: 42 phút")
