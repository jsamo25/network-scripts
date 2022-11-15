import getpass
import telnetlib


HOST = "192.168.0.1"
user = "cisco"
password = "cisco"

#Login
tn = telnetlib.Telnet(HOST)  # to open telnet connection
tn.read_until(b"Username: ")
tn.write(user.encode('utf8') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('utf8') + b"\n")

#Enable
tn.write(b"enable\n")  # \n represents end of line
tn.write(b"cisco\n")
tn.write(b"term len 0\n")
tn.write(b"show ver | i IOS \n")
tn.write(b"conf t\n")
tn.write(b"interface loopback 100\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")

tn.write(b"end\n")
tn.write(b"exit\n")  # to close the connection

print(tn.read_all().decode('utf8'))