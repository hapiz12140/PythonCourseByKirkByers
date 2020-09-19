#1. Read the "show_vlan.txt" file into your program.
# Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations.
# From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME).
# Print this data structure to the screen. Your output should look as follows:
#  [('1', 'default'),
# ('400', 'blue400'),
# ('401', 'blue401'),
# ('402', 'blue402'),
# ('403', 'blue403')]

from __future__ import print_function, unicode_literals
from pprint import pprint

f = open("D:\College\Degree\Python course by Kirk Byers\Week 3\Week 3 Exercises\show_vlan.txt")
output = f.readlines()
f.close()

output = output[2:10]

pprint(output)
print('\n')

new_list = []
for line in output:
    new_line = line.split()
    VLAN_ID = new_line[0]
    VLAN_name =new_line[1]
    new_list.append((new_line[0],new_line[1]))

print("The list containing tuples of (VLANID, VLANNAME):", new_list)



