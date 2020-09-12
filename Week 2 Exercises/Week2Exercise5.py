# 5. Read the 'show_ip_bgp_summ.txt' file into your program.
# From this BGP output obtain the first and last lines of the output.

# From the first line use the string .split() method to obtain the local AS number.

# From the last line use the string .split() method to obtain the BGP peer IP address.

# Print both local AS number and the BGP peer IP address to the screen.

from __future__ import print_function, unicode_literals

f = open("D:\College\Degree\Python course by Kirk Byers\Week 2\Week 2 Exercises\show_ip_bgp_summ.txt")
output = f.readlines()
f.close()

print("First line is :", output[0])
print("Last line is :", output[-1])

asnumber = output[0].split()
asnumber = asnumber[-1]

bgppeeraddr = output[-1].split()
bgppeeraddr = bgppeeraddr[0]

print("The local AS number is : ",asnumber)
print("The BGP peer IP address is : ",bgppeeraddr)