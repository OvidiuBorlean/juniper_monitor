from netmiko import ConnectHandler
from jnetconfig import *
import time

jnet = {
	'device_type': 'juniper',
	'host':   hostname,
	'username': c_username,
	'password': c_password,
	'port' : 22,
}

net_connect = ConnectHandler(**jnet)

while True:
	read_value = net_connect.send_command(jcommand)
	value = read_value.split()
	idle_value = value[1]
	print(idle_value)
	if idle_value >= 50:
   		cmds =  net_connect.send_command('show system process extensive')
   		report = open(report_file, "a")
   		report.write(cmds)
   	report.close()
	time.sleep(delay)