import os
import sys
import socket
from Tkinter import *
from netmiko import ConnectHandler

# Functions Defined #

def clicked():
	ipaddress = el.get()
	portlist=[]
	#username = e2.get()
	#password= e3.get()
	response = os.system("ping -n 4 " + ipaddress)
	
	if response==0:
		a= socket.gethostbyaddr(ipaddress)
		outputlbl.configure(text="Device is UP")
		print ipaddress, 'is up!'
		outputlbl1.configure(text=a[0])
	else:
		outputlbl.configure(text="Device is DOWN")
		outputlbl1.configure(text="---")
		outputlbl2.configure(text= "---")
		print ipaddress, 'is down!'
		return
	
	for port in range(22,24):
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			connection=s.connect_ex((ipaddress,port))
			if(connection == 0):
				#outputlbl2.configure(text=str(port) + " ")
				portlist.append(port)
			joinlist=",".join([str(x) for x in portlist])
			print(joinlist)
			#portlist.split(",")
			outputlbl2.configure(text=joinlist)
			if not joinlist:
				outputlbl2.configure(text= "No Open Ports")
			s.close()
		except:
			outputlbl2.configure(text="Socket Error")
				
def closeWindow():
        master.destroy()

master = Tk()
master.title("Device Details (version 1)")
master.geometry('500x350')

############# Initialization #############
# Label 1 #
label_1= Label(master, text="Device IP address    :",anchor="e",width=20, font=("Arial Bold",10))
label_1.grid(column=0, row=0)
el= Entry(master,width=40)
el.grid(row=0,column=1)
el.focus_set()
'''
# Lable 2 #
label_2= Label(master, text="Username    :",anchor="e",width=20, font=("Arial Bold",10))
label_2.grid(column=0, row=1)
e2= Entry(master,width=40)
e2.grid(row=1,column=1)


# Lable 3 #
label_3= Label(master, text="Password    :",anchor="e",width=20, font=("Arial Bold",10))
label_3.grid(column=0, row=2)
e3= Entry(master,width=40,show="#")
e3.grid(row=2,column=1)
'''

# Buttons- Submit and Quit #
btn1= Button(master, text="Submit",command=clicked,width=20,cursor="arrow").grid(column=0,row=3,sticky=W, pady=4)
btn2=Button(master,text="Quit",command=closeWindow, width=20).grid(column=1,row=3,sticky=W,pady=4)

# Outputs #
Reachability=Label(master, text="Reachability of device    :",anchor="e",width=20, font=("Arial Bold",10)).grid(column=0,row=4)
outputlbl=Label(master,text="---",anchor="w",width=40)
outputlbl.grid(column=1,row=4)

copy1=Button(master,text="Copy",command="",).grid(column=2,row=4,sticky=W, pady=4)

Reachability=Label(master, text="NsLookup    :",anchor="e",width=20,font=("Arial Bold",10)).grid(column=0,row=5)
outputlbl1=Label(master,text="---",anchor="w",width=40)
outputlbl1.grid(column=1,row=5)

OpenPorts= Label(master, text="Open Ports (22,23)    :",anchor="e",width=20,font=("Arial Bold",10)).grid(column=0,row=6)
outputlbl2=Label(master,text="---",anchor="w",width=40)
outputlbl2.grid(column=1,row=6)
'''
sshpossible=Label(master, text="Is SSH Possible?    :",anchor="e",width=20, font=("Arial Bold",10)).grid(column=0,row=7)
outputlbl3=Label(master,text="---",anchor="w",width=40)
outputlbl3.grid(column=1,row=7)


Reachability=Label(master, text="Is Telnet Possible?    :",anchor="e",width=20, font=("Arial Bold",10)).grid(column=0,row=8)
outputlbl4=Label(master,text="---",anchor="w",width=40)
outputlbl4.grid(column=1,row=8)
'''
develpedby=Label(master, text="- NJ",font=("Arial Bold",9))
develpedby.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

master.mainloop()

