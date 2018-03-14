import netmiko
from netmiko import ConnectHandler
import os
import sys
import getpass
import telnetlib

# Opening file that contains IP address and read Each Ip address line by line. 
# Example of input.txt file:
# 1.1.1.1
# 2.2.2.2

with open('input.txt') as fname:
	switches=fname.read().splitlines()
	
# Username and Password to login to switch. 
username="singhr"
password="*******"

# Opening file and saving device details collected to file DeviceDetails.txt
with open('DeviceDetails.txt','w+') as file:
	print("Trying SSH and Telnet Test for User ID: ", username, "Password: ", password)
	file.write("Trying SSH and Telnet Test for User ID: " + username + "Password: " + password + "\n")
	print(":" * 90 + "\n")
	file.write("#" * 90 + "\n")
	for device in switches:
		try:
				ios_device= {
					'device_type' : 'cisco_ios',
					'ip' : device,
					'username' : username,
					'password' : password,
				}
				# We are attempting to connect.
				net_connect = ConnectHandler(**ios_device)
				print(device, " : SSH login Successful")
				print("*" * 35 + "\n")
				file.write(str(device) + " : SSH login Successful" + "\n" + "*" * 35)
				output = net_connect.send_command('show version | inc System serial|uptime|image|Model number|MAC|Cisco\n')
				print(output)
				file.write(output)
				file.write("\n" + "==" * 30 + "\n")
		except:
				# If ssh failed, TRY telnet
				print(device, " : SSH Failed. Trying to Telnet")
				file.write(str(device) + " : SSH Failed. Trying to Telnet" + "\n")
				try:
					tn = telnetlib.Telnet(device,23,5)
					tn.read_until(b"UserName: ")
					tn.write(username.encode('ascii') + b"\n")
					if password:
						tn.read_until(b"Password: ")
						tn.write(password.encode('ascii') + b"\n")
						print(device," : Telnet login Successful")
						file.write(str(device) + " : Telnet login Successful" + "\n"  + "*" * 35)
						
					tn.write("terminal length 0\n".encode('utf-8'))
					tn.write(b"show version | inc System serial|uptime|image|Model number|MAC|Cisco\n".encode('utf-8'))
					tn.write(b"exit\n".encode('utf-8'))
					output= tn.read_all()
					print tn.read_all()
					file.write(output)
					file.write("==" * 40 + "\n")
					#tn.close()
					#break
					continue	
					#print("====" * 12)
					#file.write("====" * 12 + "\n")
				except Exception,EOFError:
					print(device, "Unable to SSH and Telnet")
					file.write(str(device) + " :Unable to SSH and Telnet" + "\n")
					print("====" * 12)
					file.write("====" * 12 + "\n")
