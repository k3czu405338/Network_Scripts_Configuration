from netmiko import ConnectHandler
import random
import string
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

conn = ConnectHandler(**device)
for user_id in range(0,10):
    conn.send_config_set([
        f'no username admin_{user_id}'
    ], read_timeout=10)

    # # Write generated password to text file
    # with open("passwords.txt", 'a') as file:
    #     file.write(f"admin_{user_id} {password}\n")

conn.save_config()
conn.disconnect()
