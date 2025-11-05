from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

conn = ConnectHandler(**device)
conn.send_config_set([
    'interface fa0/1',
    'switchport mode access',
    'switchport access vlan 3'
])
conn.save_config()
conn.disconnect()
