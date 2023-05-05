import re
import subprocess
ipconfig_output = subprocess.check_output("ipconfig /all ")
ipconfig_output=ipconfig_output.decode()
pattern_IPv4_Address = r"IPv4 Address\. .+? : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
pattern_Subnet_Mask = r"Subnet Mask .+? : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
pattern_Default_Gateway = r"Default Gateway .+? : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
pattern_DHCP_Server = r"DHCP Server .+? : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
match = re.search(pattern_IPv4_Address,ipconfig_output)
IPv4_Address = match.group(1)
match = re.search(pattern_Subnet_Mask,ipconfig_output)
Subnet_Mask = match.group(1)
match = re.search(pattern_Default_Gateway,ipconfig_output)
Default_Gateway = match.group(1)
match = re.search(pattern_DHCP_Server,ipconfig_output)
DHCP_Server = match.group(1)
file=open("KQ_TH1_Bai1.txt",mode="w",encoding="utf-8")
file.write(f"""
Đại học Bách Khoa Hà Nội
Viện Toán ứng dụng và Tin học
Hệ thống và Mạng máy tính
Bài thực hành số 1

Thông tin sinh viên:
Họ và tên: Vũ Văn Nghĩa 
Mã số sinh viên: 20206205

Câu 1. Xác định địa chỉ IP của máy đang sử dụng, mặt nạ mạng, địa chỉ Gateway, địa chỉ máy chủ DNS. 
Bài làm:
Dùng lệnh ipconfig để xác định:
Hoặc
Dùng lệnh ipconfig /all để hiển thị đầy đủ:
=> Kết quả:
+ Địa chỉ IP (IPv4 Address): {IPv4_Address}
+ Mặt nạ mạng (Subnet Mask): {Subnet_Mask}
+ Địa chỉ Gateway (Default Gateway): {Default_Gateway}
+ Địa chỉ máy chủ DNS (DNS Servers): {DHCP_Server}
""")
file.close()
print("XONG!")