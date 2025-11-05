import timestamp
from netmiko import ConnectHandler
from datetime import datetime
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}


# Connect to device
print(f"Connecting to {device['ip']}...")
connect = ConnectHandler(**device)

# Command to copy running-config to startup-config
command = f"copy running-config startup-config"
print("copy running-config startup-config in progress...")



connect.save_config()
connect.disconnect()
