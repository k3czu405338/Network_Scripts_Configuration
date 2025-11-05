from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

connect = ConnectHandler(**device)
for vlan_id in range(100,200):
    connect.send_config_set([
    f'no vlan {vlan_id}'
])
connect.save_config()
connect.disconnect()
