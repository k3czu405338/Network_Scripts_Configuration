from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

conn = ConnectHandler(**device)
conn.send_config_set([
    'interface range fa0/1-8',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
])
conn.save_config()
conn.disconnect()
