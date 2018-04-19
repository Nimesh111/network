import getpass
import telnetlib
import sys

def telentcheck():
	try:
		# Host IP address will be IP address of device to which you want to connect. 
		Host="127.0.0.1"
		username=raw_input("Enter Your Username:")
		password= getpass.getpass()
		
		tn=telnetlib.Telnet(Host)
		
		tn.read_until("Username: ")
		tn.write(username + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")
		
		tn.write("show ip int br\n")
		tn.write("exit\n")
		
		print tn.read_all()
	except:
		print "Connection cannot be established."

if __name__=="__main__":
	telentcheck()
