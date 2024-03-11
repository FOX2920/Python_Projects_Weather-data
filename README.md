# Ứng dụng Dữ liệu Thời tiết

Đây là một ứng dụng Python lấy dữ liệu thời tiết cho một thành phố ngẫu nhiên bằng cách sử dụng API OpenWeatherMap và lưu trữ dữ liệu vào cơ sở dữ liệu MySQL.

## Yêu cầu

Trước khi chạy ứng dụng, hãy đảm bảo rằng bạn đã cài đặt:

- Python 3.x
- Cơ sở dữ liệu MySQL

## Cài đặt

1. Clone kho lưu trữ:
```
git clone https://github.com/FOX2920/Python_Projects_Weather-data-test-.git
```

2. Chuyển đến thư mục dự án:
```
cd Python_Projects_Weather-data-test-
```
3. Cài đặt các gói Python cần thiết:
```
pip install -r requirements.txt
```
4. Thiết lập cơ sở dữ liệu MySQL:
Tạo một cơ sở dữ liệu mới có tên weather.
Mở tệp main.py và cập nhật thông tin kết nối cơ sở dữ liệu với thông tin đăng nhập MySQL của bạn:
```
db = DatabaseConnection(
    host="your_host",
    username="your_username",
    password="your_password",
    database="weather"
```
5. Thiết lập khóa API OpenWeatherMap:
Mở tệp main.py và thay thế "YOUR_API_KEY" bằng khóa API OpenWeatherMap thực tế của bạn.

## Cách Sử dụng

Để chạy ứng dụng, hãy thực hiện lệnh sau:
```
python main.py
```
Ứng dụng sẽ thực hiện các bước sau:

1. Kết nối đến cơ sở dữ liệu MySQL và tạo các bảng cần thiết nếu chúng chưa tồn tại.
2. Lấy một quốc gia ngẫu nhiên và thủ đô của nó từ API countriesnow.space.
3. Lấy dữ liệu thời tiết cho thành phố ngẫu nhiên từ API OpenWeatherMap.
4. Chèn dữ liệu vị trí và thời tiết vào các bảng tương ứng trong cơ sở dữ liệu MySQL.
5. Đầu ra sẽ hiển thị một thông báo cho biết liệu dữ liệu thời tiết đã được chèn thành công vào cơ sở dữ liệu hay chưa.

## Cấu trúc Dự án
`connection.py`: Chứa lớp DatabaseConnection để quản lý kết nối cơ sở dữ liệu MySQL.
`weather.py`: Chứa các lớp Location và Weather để tạo và tương tác với các bảng cơ sở dữ liệu tương ứng.
`main.py`: Tập lệnh chính điều khiển quá trình lấy và lưu trữ dữ liệu thời tiết.
`requirements.txt`: Liệt kê các gói Python cần thiết cho dự án.
