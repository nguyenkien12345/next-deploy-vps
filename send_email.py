import smtplib # Thư viện để gửi email qua SMTP
import ssl # Thư viện để tạo kết nối bảo mật SSL
import os # Thư viện để làm việc với biến môi trường
from email.mime.text import MIMEText # Để tạo nội dung email dạng text
from email.mime.multipart import MIMEMultipart # Để tạo email có nhiều phần

port = 465 # Port SSL của Gmail
smtp_server = "smtp.gmail.com" # Server SMTP của Gmail
USERNAME = os.environ.get('USER_EMAIL') # Lấy email từ biến môi trường
PASSWORD = os.environ.get('USER_PASSWORD') # Lấy password từ biến môi trường (Password ở đây chính là lấy từ password application từ tài khoản email của chúng ta)
Subject = "GitHub Email Report"  # Tiêu đề emai
Body = "This is your daily email report." # Nội dung email
To_Emails=["phongmy1120@gmail.com"] # Danh sách người nhận

if not USERNAME or not PASSWORD:
    raise ValueError("USER_EMAIL và USER_PASSWORD phải được cung cấp.")

try:
    # Tạo 1 đối tượng email
    msg = MIMEMultipart()
    msg["From"] = USERNAME
    msg["To"] = ', '.join(To_Emails)
    msg["Subject"] = Subject

    # Thêm nội dung email vào message
    msg.attach(MIMEText(Body, 'plain'))

    # Tạo context SSL để bảo mật
    context = ssl.create_default_context()

    # Kết nối và gửi email
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, To_Emails, msg.as_string())
        
except smtplib.SMTPAuthenticationError:
    raise ValueError("Lỗi xác thực: Tên người dùng hoặc mật khẩu không đúng.")
except smtplib.SMTPException as e:
    raise ValueError(f"Lỗi SMTP: {e}")
except Exception as e:
    raise ValueError(f"Lỗi không xác định: {e}")