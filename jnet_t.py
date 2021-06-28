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
    print(read_value)
    print("\n")  
    print("**********************************************************************" )
    value = read_value.split()
    idle_value = value[1]
    print("Current Value = " + idle_value)
    if int(idle_value) < int(value_idle):
   	   cmds =  net_connect.send_command_timing('show system process extensive')
   	   report = open(report_file, "a")
   	   report.write(cmds)
    print("Sleeping for " + str(c_delay))
    time.sleep(c_delay)