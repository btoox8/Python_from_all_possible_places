import socket
####################
                                #IPv4                     #UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

####################
              #set ip         #set port
s.bind(("127.0.0.1",5555))

####################
Rdata , address = s.recvfrom(1024)
    #buffer size

####################
Rdata = Rdata.decode("UTF-8")
    #decode for data
####################
Sdata = "Hello Client"

####################
Sdata = Sdata.encode("UTF-8")
     #encoding

####################
s.sendto(Sdata,address)