# This code is used to ping multiple devices, Check the NSlookup of devices, Check open ports (Here we are checking only telnet and SSH, 
# however you can check any number of ports). 

# Importing Modules.

import socket
import sys
import subprocess
from datetime import datetime
import os

# Opening Input file which contains IP addresses. 
with open('subnetcheck.txt') as fname:
    switches = fname.read().splitlines()

# Checking out which version of python compiler is used. 
print(sys.version)

# Collect details of device up, device down and Open port for each device in differenct files.
with open('DeviceStatus-UP.txt','w+') as filename, open('DeviceStatus-DOWN.txt','w+') as downfile, open('OpenPorts-Device_UP.txt','w+') as openports:
	for ip in switches:
		
		# Checking the start time of scanning.
		t1=datetime.now()
		
		print("-" * 40)
		print("Please wait, We are checking Device reachability, NSlookup and Open Ports of: ", ip)
		print("-" * 40)
				
		# Checking Ping response. If ping is possible, we will check NSlookup of device with IP address.
		try:
			response =os.system("ping -n 1 " + ip)	#Returns Integer Value. 1 = Device Not reachable. 0= Device
			#print(str(result) + "\n")
			if response == 0: 
				print(ip, " is up!")
				try:
					print(socket.gethostbyaddr(ip))
					#nslook.write(socket.gethostbyaddr(ip))
				except:
					print(ip, ": Host cannot be resolved")
				filename.write(str(ip) + '\n')
			else: 
				print(ip, " is down!")
				#filename.write(str(ip) + ' is down!' + '\n')
				#downfile= open('devicesdownfile.txt','w+')
				downfile.write( str(ip) + '\n')
				#downfile.close()
				continue

				# Scanning ports from range 22 to 23 and checking out, if it is open or not.
			for port in range(22,24):
				# Socket instance is created and 2 parameters has been passed. 
				# The FIRST Parameter AF_INET refers to the address family of IPV4.
				# The SECOND Parameter SOCK_STREAM means connection oriented TCP Protocol.
				
				s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result=s.connect_ex((ip,port))
				
				if(result == 0):
					print("Port {}:  Open".format(port))
					openports.write(ip + " == Port {}:  Open\n".format(port))
				s.close()
			openports.write("==" * 20 + "\n")
			
		# Error if Ctrl+ c is pressed.         
		except KeyboardInterrupt:
			print("Keyboard interruption. You Pressed Ctrl+C.")
			sys.exit()
		
		# Error if device is not reachable. 
		except socket.gaierror:
			print("Could not connect to this device.")
			sys.exit()
		
		except socket.error:
			print("Could not connect to server")
			sys.exit()
			
		# Checking the End time of scanning. 
		t2= datetime.now()

		# Time difference.
		total=t2-t1
		
		print("Scanning completed in: ", total, "\n")
filename.close()
downfile.close()
openports.close()
