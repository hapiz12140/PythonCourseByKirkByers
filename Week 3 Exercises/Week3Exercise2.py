#2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file.
# Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

# Add a conditional statement that searches for '10.220.88.1'.
# If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

# Using a conditional statement, also search for '10.220.88.30'.
# If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

# Keep track of whether you have found both the Default Gateway and the Arista3 switch.
# Once you have found both of these devices, 'break' out of the for loop.

from __future__ import print_function, unicode_literals
from pprint import pprint

f = open("D:\College\Degree\Python course by Kirk Byers\Week 3\Week 3 Exercises\show_arp.txt")
output = f.readlines()
f.close()

pprint(output)
print("\n")

flag1,flag2 = (False,False)
for line in output:
    if 'protocol' in line.lower():
        continue
    line = line.split()
    ip_addr = line[1]
    mac_addr = line[3]
    if ip_addr == '10.220.88.1':
        print("Default gateway IP/Mac: ",ip_addr, "/", mac_addr)
        flag1 = True
    elif ip_addr == '10.220.88.30':
        print("Arista3 IP/Mac is",ip_addr, "/", mac_addr)
        flag2 = True
    if flag1 and flag2:
        break



