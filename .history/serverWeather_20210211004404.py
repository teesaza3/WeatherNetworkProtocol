import socket
import json
import requests


host = ''        # Symbolic name meaning all available interfaces
port = 60301     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
querystring = {'uid': 'u64teelak1113','ukey': 'f97efea71db0ec46c6b9750375720891', 'format': 'json'}


def findProvince(input):
    print("ตรวจสอบจังหวัดว่ามีอยู่ในประเทศไทย")
    with open('./data.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    for province in data['provinces']:
        if input == province['PROVINCE_NAME']:
            print("พบจังหวัดที่ต้องการค้นหา")
            return 'correct'
    print("ไม่พบจังหวัดที่กำลังค้นหา")
    return 'wrong'

    # print(provinces['provinces'])


def spiltDataWeatherToday(json_data):
    temp = ""
    for key in json_data:
        if key == "Time" or key == "TotolCloud":
            temp += key + " : " + str(json_data[key]) +"\n"
        else:
            temp += key + " : " + str(json_data[key]['Value'])+ " " +str(json_data[key]['Unit']) +"\n"
        
    # print(temp)
    conn.send(temp.encode())

def spiltDataForeCast7Days(json_data):
    temp = ""
    print('ชื่อจังหวัด : ' + json_data['ProvinceNameTh'])
    for eachDay in json_data['SevenDaysForecast']:
        for data in eachDay:
            if data == "TempartureLevel" or data == "WeatherDescription" or data == "Date":
                temp += data + " : " + str(eachDay[data]) +"\n"
            elif data == "WeatherDescriptionEn" or data == "TempartureLevelEn" or data == "WaveHeight" or data == "WaveHeightEn":
                temp += ""
            else:
                temp += data + " : " + str(eachDay[data]['Value'])+ " " +str(eachDay[data]['Unit']) +"\n"
        temp += '-----------------------------------------------------------' + "\n"
    # print(temp)
    conn.send(temp.encode())
    
def weatherToday(province):
    print("แสดงข้อมูล สภาพอากาศวันนี้")
    url = 'https://data.tmd.go.th/api/WeatherToday/V1/'
    response = requests.request('GET', url, params=querystring)
    response = json.loads(response.text)
    string = ""
    for i in response['Stations']:
        if i['Province'] == province:
            spiltDataWeatherToday(i['Observe'])
            break
    return string

def news():
    print("ข่าวเตือนภัยสภาพอากาศ ข่าวสารภูมิอากาศ")
    url = 'https://data.tmd.go.th/api/WeatherWarningNews/v1/?uid=demo&ukey=demokey'
    response = requests.request('GET', url, params=querystring)
    response = json.loads(response.text)
    print(response)
    return 






def foreCast7Days(province):
    # print(province)
    print("แสดงข้อมูล ผลการพยากรณ์อากาศสำหรับประเทศไทยล่วงหน้า 7 วัน ของจังหวัด" + province)
    url = 'https://data.tmd.go.th/api/WeatherForecast7Days/V1/'
    response = requests.request('GET', url, params=querystring)
    response = json.loads(response.text)
    string = ""
    for nameProvince in response['Provinces']:
        # print(nameProvince['ProvinceNameTh'])
        if nameProvince['ProvinceNameTh'] == province:
            spiltDataForeCast7Days(nameProvince)
            break
        #     print('11111')
        #     break
            # break
    return string


print('Connected by', addr)
while True:
    while True:
        # print("loop 1")
        province = conn.recv(1024)
        province = str(province, 'utf-8')
        if province == "exit":
            print('ออกจากระบบ')
            conn, addr = s.accept()
            continue
        check = findProvince(province)
        # correct = 'correct' if check == 1 else 'wrong'
        if check == 'correct':
            conn.send(check.encode())
            break 
        else:
            conn.send(check.encode())
    while True:
        # print("loop 2")
        number = conn.recv(1024)
        number = str(number, 'utf-8')
        if number == "1":
            print("ผู้ใช้ต้องการข้อมูล สภาพอากาศวันนี้")
            weatherToday(province)  
        elif number == "2":
            print("ผู้ใช้ต้องการข้อมูล ข่าวเตือนภัยสภาพอากาศ")
            news()
        elif number == "3":
            print("ผู้ใช้ต้องการข้อมูล ผลการพยากรณ์อากาศสำหรับประเทศไทยล่วงหน้า(ราย 7 วัน)")
            foreCast7Days(province)
        elif number == "4":
            print("ผู้ใช้ต้องการเปลี่ยนจังหวัดในการค้นหา")
            break
        elif number == "exit":
            print('ออกจากระบบ')
            conn, addr = s.accept()
            break
        else:
            print("ไม่มีชุดคำสั่งนี้")
            continue
conn.close()