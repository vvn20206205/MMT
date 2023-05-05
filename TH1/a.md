### Bài thực hành số 1
1.	Xác định địa chỉ IP của máy đang sử dụng, mặt nạ mạng, địa chỉ Gateway, địa chỉ máy chủ DNS.
2.	Tìm hiểu cách sử dụng phần mềm Cisco Packet Tracer, mô phỏng mạng LAN của phòng máy sử dụng Switch SW1, mạng LAN của Văn phòng sử dụng Switch SW2, Bộ môn Toán Tin sử dụng Switch SW3.
3.	Giả sử mạng LAN của Phòng máy, Văn phòng và Bộ môn Toán Tin kết nối với nhau thông qua 3 Router R1, R2, R3. 
Cấu hình thử nghiệm định tuyến, giả sử dải địa chỉ IP của các mạng LAN như sau
Phòng máy	10.0.1.0/24
Văn phòng 	10.0.2.0/24
Bộ môn Toán Tin	10.0.3.0/24
Mạng kết nối Router	10.0.4.0/24

Cấu hình định tuyến và kiểm tra kết nối giữa các mạng bằng lệnh ping.
MMT-TH1-20206205.docx
MMT-TH1-20206205.docx
MMT-TH1-20206205.docx
MMT-TH1-20206205.docx
'''
1.	Xác định địa chỉ IP của máy đang sử dụng, mặt nạ mạng, địa chỉ Gateway, địa chỉ máy chủ DNS. 
Dùng lệnh ipconfig để xác định:
Hoặc
Dùng lệnh ipconfig /allcompartments /all để xác định:
- Địa chỉ IP (IPv4 Address): xxxxxxxxxxxxxxxxxxxx
- Mặt nạ mạng (Subnet Mask): xxxxxxxxxxxxxxxxxxxx
- Địa chỉ Gateway (Default Gateway): xxxxxxxxxxxxxxxxxxxx
- Địa chỉ máy chủ DNS (DNS Servers): xxxxxxxxxxxxxxxxxxxx
'''

Trên Windows:
Địa chỉ IP của máy đang sử dụng được liệt kê dưới mục "IPv4 Address".
Mặt nạ mạng được liệt kê dưới mục "Subnet Mask".
Địa chỉ Gateway được liệt kê dưới mục "Default Gateway".
Địa chỉ máy chủ DNS được liệt kê dưới mục "DNS Servers".
Trên Mac OS X:
Địa chỉ IP của máy đang sử dụng được liệt kê dưới mục "inet".
Mặt nạ mạng được liệt kê dưới mục "netmask".
Địa chỉ Gateway được liệt kê dưới mục "gateway".
Địa chỉ máy chủ DNS được liệt kê dưới mục "nameserver".