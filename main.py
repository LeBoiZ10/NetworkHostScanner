import os
import socket
##############################################
#THIS PROGRAM TAKES 9 HOURS TO FULLY EXCECUTE#
##############################################

#getting local ip to use prefix
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
s.close()

#getting ip prefix
ipArr = ip.split(".")
ipStr = str(ipArr[0]) + "." + str(ipArr[1])

count = 0

#opening file to store online hosts
db = open("Hosts.txt", "w")
#for loop to iterate through all possible IPs in the network
for x in range(0, 255):
    for y in range(0, 255):
        #concatenating ip address
        ip = ipStr + "." + str(x) + "." + str(y)
        #if the ping is successful then write it to the file
        if os.system("ping " + ip + " -n 1 -w 500") == 0:
            db.write(ip + "\n")
            count += 1
        print(count)

#close file
db.close()