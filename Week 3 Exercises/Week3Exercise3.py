"""
3.  Read the 'show_lldp_neighbors_detail.txt' file.
Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id".
Save these two items into variables and print them to the screen.
You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15').
Break out of your loop once you have retrieved these two items.

"""

from __future__ import print_function, unicode_literals
from pprint import pprint

with open("D:\College\Degree\Python course by Kirk Byers\Week 3\Week 3 Exercises\show_lldp_neighbors_detail.txt") as f:
    output = f.read()

flag1, flag2 = (False,False)
for item in output.splitlines():
    if "System Name" in item:
        name = item.split(":")
        name = name[1]
        print("Name found: ", name)
        flag1 = True
    elif "Port id" in item:
        portid = item.split(":")
        portid = portid[1]
        print("Port ID found: ", portid)
        flag2 = True
    if flag1 and flag2:
        print("Exiting...")
        break