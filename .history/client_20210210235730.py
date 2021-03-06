# echo_client.py
import socket

host = socket.gethostname()
port = 60301                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
command=['1','2','3','4','5','6','exit']
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
            print('(3) ผลการพยากรณ์อากาศสำหรับประเทศไทยล่วงหน้า(ราย 7 วัน)')
            print('(4) กลับไปเปลี่ยนชื่อจังหวัด')
            print('(exit) ออกโปรแกรม')
            
            number = input("กรุณาใส่เลขที่ต้องการ: ")
            if number not in command:
                print("ไม่มีชุดคำสั่งนี้")
                s.send(number.encode())
                continue
            s.send(number.encode())
            if number == "4" :
                break
            elif number == 'exit':
                province = 'exit'
                break
           
            data = s.recv(4096).decode()
            print(data)
    else:
        print('กรุณาพิมพ์ชื่อจังหวัดให้ถูกต้อง')
    if province == 'exit':
        break
    

s.close()
# print('Received', repr(data))
