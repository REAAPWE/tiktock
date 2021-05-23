import requests


print("     /\            | |            ")            
print("    /  \__   ____ _| |_ __ _ _ __ ")
print("   / /\ \ \ / / _` | __/ _` | '__|")
print("  / ____ \ V / (_| | || (_| | |   ")
print(" /_/    \_\_/ \__,_|\__\__,_|_|   ")

print("[Main] Tiktok Password Changer")

sessionid = input("\n[?] Enter Sessionid :")
old_password = input("[?] Enter Old Password :")
new_password = input("[?] Enter New Password :")

url = 'https://api2.musical.ly/passport/password/update/?version_code=9.0.0&language=ar&pass-region=1&app_name=musical_ly&vid=2473DC0F-0B47-459B-ABED-514C60E781AC&app_version=9.0.0&carrier_region=AE&is_my_cn=0&channel=App%20Store&mcc_mnc=42402&device_id=6923575826752275974&tz_offset=14400&account_region=&sys_region=US&aid=1233&screen_width=1242&openudid=a861b4160267eee9fb66e847074a28f711bb7de1&os_api=18&ac=WIFI&os_version=14.3&app_language=ar&tz_name=Asia/Dubai&device_platform=iphone&build_number=90006&device_type=iPhone9,4&iid=6962661388847630085&idfa=00000000-0000-0000-0000-000000000000&mas=01b44cf53cf545849449b462a4b1ce605203491547858df05f8cf7&as=a176062ac123a087502242&ts=1621124913'
headers = {
    'Connection': 'close',
    'Content-Length': '57',
    'sdk-version': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-SS-TC': '0',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': f'sessionid={sessionid}'
    }
data = {
    'current_password': old_password,
    'mix_mode': '1',
    'password': new_password}
    

r1 = requests.post(url, headers=headers, data=data).text

if '"message":"success"' in r1:
    print("\n[+] Password Has Been Updated")
    exit()
elif '"description":"گفتوگۆکە تەواو بوو، تکایە دووبارە بچۆ ژوورەوە."' in r1:
    print("\n[-] Failed Login")
    exit()
elif '"message":"error"' in r1:
    print("\n[-] Failed Change Password")
    exit()
else:
    print(r1)
    exit()

