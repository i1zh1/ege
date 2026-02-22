from ipaddress import *
ip = ip_network('106.184.0.0/255.248.0.0')
count = 0
for i in ip:
    if bin(int(i))[2:].count('1') % 2 !=0:
        count+=1
print(count)