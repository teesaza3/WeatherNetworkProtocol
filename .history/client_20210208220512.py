# echo_client.py
import socket

host = socket.gethostname()
port = 60301                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
command=['1','2','3','4','5','']
while True:
    province = input("ใส่ชื่อจังหวัด: ")
    if province == 'exit':
        s.send(province.encode())
        break
    s.send(province.encode())
    correct = s.recv(1024).decode()
    
    if correct == 'correct':
        while True:
            print('(1) สภาพอากาศวันนี้')
            print('(2) ข่าวเตือนภัยสภาพอากาศ')
            print('(3) กลับไปเปลี่ยนชื่อจังหวัด')
            print('(exit) ออกโปรแกรม')
            
            number = input("กรุณาใส่เลขที่ต้องการ: ")
            if number not in list
            s.send(number.encode())
            if number == "3" :
                break
            elif number == 'exit':
                province = 'exit'
                break
            else:
                print("ไม่มีชุดคำสั่งนี้")
                continue
            data = s.recv(1024).decode()
            print(data)
    else:
        print('กรุณาพิมพ์ชื่อจังหวัดให้ถูกต้อง')
    if province == 'exit':
        break
    

s.close()
# print('Received', repr(data))