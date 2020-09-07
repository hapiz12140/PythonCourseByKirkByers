#2. Prompt a user to enter in an IP address from standard input.
# Read the IP address in and break it up into its octets.
# Print out the octets in decimal, binary, and hex.
#
#Your program output should look like the following:
#
#​ $ python exercise2.py
#Please enter an IP address: 80.98.100.240
#
#    Octet1         Octet2         Octet3         Octet4
#------------------------------------------------------------
#      80             98             100            240
#   0b1010000      0b1100010      0b1100100     0b11110000
#     0x50           0x62           0x64           0xf0
#------------------------------------------------------------
#
#Four columns, fifteen characters wide, a header column, data centered in the column.

from __future__ import print_function

ipaddr = input("Please enter input address: ")

octets = ipaddr.split(".")

print("{:^15}{:^15}{:^15}{:^15}".format("Octet1","Octet2","Octet3","Octet4"))
print("-"*70)
print(f"{octets[0]:^15}{octets[1]:^15}{octets[2]:^15}{octets[3]:^15}")
print(f"{bin(int(octets[0])):^15}{bin(int(octets[1])):^15}{bin(int(octets[2])):^15}{bin(int(octets[3])):^15}")
print(f"{hex(int(octets[0])):^15}{hex(int(octets[1])):^15}{hex(int(octets[2])):^15}{hex(int(octets[3])):^15}")
print("-"*70)




