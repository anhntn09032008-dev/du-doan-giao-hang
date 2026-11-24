import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("delivery_model.pkl")

st.title("🚚 Hệ thống dự đoán thời gian giao hàng")

distance = st.number_input("Khoảng cách (km)", min_value=1)

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

# Mã hóa giống lúc train
weather_map = {
    "Nắng": 0,
    "Mưa nhẹ": 1,
    "Mưa lớn": 2
}

traffic_map = {
    "Thông thoáng": 0,
    "Trung bình": 1,
    "Tắc nghẽn": 2
}

service_map = {
    "Tiêu chuẩn": 0,
    "Nhanh": 1,
    "Hỏa tốc": 2
}

if st.button("Dự đoán"):

    input_data = pd.DataFrame(
        [[
            distance,
            weather_map[weather],
            traffic_map[traffic],
            service_map[service],
            weight
        ]],
        columns=[
            "Khoang_Cach_Km",
            "Thoi_Tiet",
            "Tinh_Trang_Giao_Thong",
            "Loai_Dich_Vu",
            "Khoi_Luong_Hang_kg"
        ]
    )

    prediction = model.predict(input_data)

    st.success(
        f"⏱️ Thời gian giao hàng dự kiến: {prediction.1f} phút"
    )

st.subheader("🤖 Chatbot Logistics")

question = st.text_input("Đặt câu hỏi")

if st.button("Gửi câu hỏi"):

    if "mưa" in question.lower():
        st.write(
            "Mưa thường làm tăng thời gian giao hàng do ảnh hưởng đến tốc độ di chuyển."
        )

    elif "tắc" in question.lower():
        st.write(
            "Tắc nghẽn giao thông là một trong những nguyên nhân gây giao hàng chậm."
        )

    elif "hỏa tốc" in question.lower():
        st.write(
            "Dịch vụ hỏa tốc giúp rút ngắn thời gian giao hàng nhưng chi phí cao hơn."
        )

    else:
        st.write(
            "Hãy hỏi về thời tiết, giao thông hoặc dịch vụ giao hàng."
        )
