from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

conn = ConnectHandler(**device)
conn.send_config_set([
    'interface g0/2',
    'switchport mode trunk',
    'switchport trunk allowed vlan 1,2,3,4,6,7',
    'switchport trunk native vlan 99'
])
conn.save_config()
conn.disconnect()
