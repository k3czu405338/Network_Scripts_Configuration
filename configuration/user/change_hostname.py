from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

conn = ConnectHandler(**device)
conn.send_config_set([
    'hostname S33'
],read_timeout=10)
conn.save_config()
conn.disconnect()
