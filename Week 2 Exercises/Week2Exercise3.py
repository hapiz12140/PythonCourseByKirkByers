# 3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

# Use pretty print to print out the resulting list to the screen, syntax is:
# from pprint import pprint
# pprint(some_var)

# Use the list .sort() method to sort the list based on IP addresses.

# Create a new list slice that is only the first three ARP entries.

# Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

# Write this string containing the three ARP entries out to a file named "arp_entries.txt".

from __future__ import print_function, unicode_literals
from pprint import pprint

f = open("D:\College\Degree\Python course by Kirk Byers\Week 2\Week 2 Exercises\show_arp.txt")
output = f.readlines()
pprint(output)
f.close()

output = output[1:15]
print("\n","After slicing header:", "\n")
pprint(output)

output.sort()
print("\n","After sorting by IP: ")
pprint(output)

new_list = output[0:3]
print("\n","New list with only 3 ARP entries: ")
pprint(new_list)

newstring = "\n".join(new_list)
print("\n","New strings after joining new_list: \n",newstring)

f = open(r"D:\College\Degree\Python course by Kirk Byers\Week 2\Week 2 Exercises\arp_entries.txt",mode="a")
f.write(newstring)
f.close()
print(r"Write to D:\College\Degree\Python course by Kirk Byers\Week 2\Week 2 Exercises\arp_entries.txt success!")



