import streamlit as st
import pandas as pd
import pdfplumber
import plotly.express as px 
st.set_page_config(layout="centered")


""" # Đọc dữ liệu từ file Excel
data = pd.read_excel("bkme.xlsx", sheet_name = 'recapmentee')

while True:
    # Nhập email và tên từ người dùng
    user_email = input("Nhập email của bạn: ")

    user_name = input("Nhập tên của bạn: ")

    # Kiểm tra xem email và tên có trong dữ liệu hay không
    match = data[(data["Mail"] == user_email) & (data["Tên Mentee"] == user_name)]

    if not match.empty:
        # Nếu có, lấy tổng recap từ bản ghi đầu tiên (nếu có nhiều hơn một bản ghi)
        a = match["Tổng số recap"].values[0]
        print(f"Tổng số recap của bạn là: {a}")
        break

    else:
        print("Email hoặc tên không tồn tại trong dữ liệu.")
        break


if a >= 10:
    print("Chúc mừng bạn nhận chứng chỉ")
else:
    print("Hiện bạn chưa đủ chứng chỉ. Cảm ơn bạn đã cố gắng") """ 

# ------------- 


st.title("BKM Info")
st.header("Giới thiệu")
st.markdown("Nhằm giúp Mentor - Mentee xem được thông tin hành trình hoạt động của mình dễ hơn Website của BK Mentoring.")
st.subheader("Liên hệ")
st.markdown("[Fanpage](https://www.facebook.com/bk.mentoring) ")
st.markdown("---------")

#st.header("Truy cập")
# click = st.button("Truy cập")

""" if Name or Email is None:
    again = st.write("Vui lòng nhập đầy đủ thông tin")
    a = st.text_input("Name") """  

#  st.header("Sử dụng")

st.subheader("Recap Mentee")
data = pd.read_excel("bkme.xlsx", sheet_name = 'recapmentee') 
st.dataframe(data)


formtee = st.form("Thông tin Mentee")
Email = formtee.text_input("Email: ")
Name = formtee.text_input("Name: ")
Submit = formtee.form_submit_button("Tìm dữ liệu")
#Sv = formtee.radio("Bạn là sinh viên năm ",['Năm 1','Năm 2','Năm 3'])
# submit_button = formtee.form_submit_button("Submit") 

    # Nhập email và tên từ người dùng
    #user_email = input("Nhập email của bạn: ")

    #user_name = input("Nhập tên của bạn: ")

    # Kiểm tra xem email và tên có trong dữ liệu hay không
match = data[(data["Mail"] == Email) & (data["Tên Mentee"] == Name)]
a = None  # Khởi tạo biến a với giá trị None

while True:
    if Submit:
        if not match.empty:
            # Nếu có, lấy tổng recap từ bản ghi đầu tiên (nếu có nhiều hơn một bản ghi)
            a = match["Tổng số recap"].values[0]
            b = st.write(f"Tổng số recap của bạn là: {a}")
            break
        else:
            st.write("Email hoặc tên không tồn tại trong dữ liệu.")
        break
    break

if a is not None:  # Kiểm tra nếu a không phải là None
    if a >= 10:
        st.write("Chúc mừng bạn nhận chứng chỉ")
    else:
        st.write("Hiện bạn chưa đủ chứng chỉ. Cảm ơn bạn đã cố gắng")
else:
    st.write("Không thể kiểm tra chứng chỉ do không có dữ liệu hợp lệ.")

range = (0,3,9, 12, 15)

st.subheader("Phân tích data")
view_scatter = px.scatter(data, x = "Tổng số recap mentoring" , y =  "Tổng số recap" , color = "Tổng số recap")

# display figure
st.subheader("Display")
st.plotly_chart(view_scatter)











st.subheader("Upload your here")
upload = st.file_uploader("Upload a PDF file")

if upload is not None:
    imported_df = pd.read_excel(upload)
    st.dataframe(imported_df)