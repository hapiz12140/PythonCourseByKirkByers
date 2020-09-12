#2. Create a list of five IP addresses.

#Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

#Use list concatenation to add two more IP addresses to the end of the list.

#Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

#Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

#Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

from __future__ import print_function, unicode_literals

ipaddrs = ["192.168.0.1","192.168.0.2","192.168.0.3","192.168.0.4","192.168.0.5"]

ipaddrs.append("192.168.0.6")
ipaddrs.extend(["192.168.0.7","192.168.0.8"])
ipaddrs = ipaddrs + ["192.168.0.9","192.168.0.10"]

print(ipaddrs)
print("First address is: ",ipaddrs[0])
print("Last address is: ",ipaddrs[-1])

ipaddrs.pop(0)
ipaddrs.pop()
print("Popping first and last...")
print("Now, first address is: ",ipaddrs[0])
print("Now, last address is: ",ipaddrs[-1])

print("Updating first ip address..")
ipaddrs[0] = "2.2.2.2"
print("First address is : ", ipaddrs[0])