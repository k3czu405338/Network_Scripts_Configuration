from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

conn = ConnectHandler(**device)
conn.send_config_set([
    'interface range fa0/7-8',
    'switchport mode access',
    'switchport access vlan 6'
])
conn.save_config()
conn.disconnect()
