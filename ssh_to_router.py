from netmiko import ConnectHandler

#Device object where you want to connect

device_id ={
    'device_type': 'cisco_ios', #check CLASS_MAPPER in https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
    'host': '192.168.0.1',
    'username': 'cisco',
    'password': 'cisco',
    'port': 22,  # optional, defaults to 22
}

#Start connection to device
net_connect = ConnectHandler(**device_id)

#Commands can be executed
output = net_connect.send_command('show ver | inc IOS')
print("the current IOS version is {}".format(output))

#Close connection
net_connect.disconnect()
