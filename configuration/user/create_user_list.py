from netmiko import ConnectHandler
import random
import string
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

privilege_level = 15
#Combination for one letter password
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+[]{}<>?/"

conn = ConnectHandler(**device)
for user_id in range(1,11):
    # Generate a 12-character random password
    password = ''.join(random.choice(chars) for _ in range(12))
    print(password)

    conn.send_config_set([
        f'username admin_{user_id} privilege {privilege_level} secret {password}'
    ], read_timeout=60)

    # Write generated password to text file
    with open("passwords.txt", 'a') as file:
        file.write(f"admin_{user_id} {password}\n")

conn.save_config()
conn.disconnect()
