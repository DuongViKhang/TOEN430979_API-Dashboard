import imapclient
import email
import re
def NhanOTP_Email():
    # Kết nối tới máy chủ IMAP
    imap_server = 'imap.gmail.com'
    username = "testipa33zz@gmail.com"
    password = "bejfbzbdwfewnldh"

    # Khởi tạo client IMAP
    client = imapclient.IMAPClient(imap_server, ssl=True)

    # Đăng nhập vào tài khoản
    client.login(username, password)

    # Chọn hộp thư
    client.select_folder('INBOX')

    # Tìm tin nhắn đầu tiên
    messages = client.search('ALL', )
    first_message_id = messages[-1]

    # Lấy tin nhắn đầu tiên và chuyển thành chuỗi
    response = client.fetch([first_message_id], ['BODY[]'])
    message_data = response[first_message_id]
    raw_message = message_data[b'BODY[]']
    message = email.message_from_bytes(raw_message)

    # Kiểm tra nếu tin nhắn có phần BODY
    if message.is_multipart():
        for part in message.get_payload():
            if part.get_content_type() == 'text/plain':
                message_text = part.get_payload(decode=True).decode('utf-8')
                break
    else:
        message_text = message.get_payload(decode=True).decode('utf-8')

    # Đóng kết nối
    client.logout()
    match = re.search(r'\b\d{6}\b', message_text)
    if match:
        code = match.group()
        return code

