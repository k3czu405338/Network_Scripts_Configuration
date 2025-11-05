import timestamp
from netmiko import ConnectHandler
from datetime import datetime
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.253',
    'username': 'cisco',
    'password': 'cisco',
}

tftp_server='192.168.1.47'
timestamp = datetime.now().strftime('%Y_%m_%d__%H-%M-%S')
backup_filename = f"backup_running_config_{timestamp}.cfg"

# Connect to device
print(f"Connecting to {device['ip']}...")
connect = ConnectHandler(**device)

# Command to copy running-config to TFTP
command = f"copy running-config tftp:"
print(f"Sending command: {command}")


output = connect.send_command_timing(command)
if "Address" in output:
    output += connect.send_command_timing(tftp_server + "\n")
if "Destination" in output:
    output += connect.send_command_timing(backup_filename + "\n")

print("Backup in progress...")
print(output)


connect.save_config()
connect.disconnect()
