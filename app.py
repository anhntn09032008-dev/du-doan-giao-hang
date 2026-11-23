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
    new_data = pd.DataFrame([{
        "weather": weather,
        "traffic": traffic,
        "service": service,
        "weight": weight
    }])
if st.button("Dự đoán"):
    new_data = pd.DataFrame([{
        "weather": weather,
        "traffic": traffic,
        "service": service,
        "weight": weight
    }])

    new_data = pd.get_dummies(new_data)
    new_data = new_data.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(new_data)[0]

    st.success(
        f"Thời gian giao hàng dự kiến: {prediction:.0f} phút"
    )
