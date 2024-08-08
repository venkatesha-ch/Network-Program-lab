from socket import *
import time

grp = '224.0.0.1'
port = 4321
sockfd = socket(AF_INET, SOCK_DGRAM, 0)
sockfd.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 16)
while True:
    val = str(input("Enter msg for multicast : "))
    print("Sending msg")
    sockfd.sendto(val.encode(), (grp, port))
    time.sleep(1)
