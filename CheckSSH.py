from netmiko import ConnectHandler

def CheckSSH():
	try:
		device={
			'device_type':'cisco_ios',
			'ip':'IPADDRESS',
			'username':'USERNAME',
			'password':'PASSWORD',
			}
			
		net_connect=ConnectHandler(**device)
		print "SSH connection Successful"
	except:
		print "SSH connection not possible."
		
if __name__=="__main__":
	CheckSSH()