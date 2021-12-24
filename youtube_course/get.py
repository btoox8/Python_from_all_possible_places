import socket

####################
ip = socket.gethostbyname("www.google.com")
print(ip)
####################
ip2 = socket.gethostbyname("localhost")
print(ip2)
####################
host = socket.gethostbyaddr(str(ip))
print(host)
####################
host2 = socket.gethostbyaddr(str(ip2))
print(host2)
####################
port = socket.getservbyname("telnet")
#http, https ,ftp,...
print(port)
####################
service_name = socket.getservbyport(21)
print(service_name)