# 4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

# Obtain the list entry associated with the FastEthernet4 interface.
# You can just hard-code the index at this point since we haven't covered for-loops or regular expressions.
# Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.

# Create a two element tuple from the result (intf_name, ip_address).

# Print that tuple to the screen.

# Use pycodestyle on this script. Get the warnings/errors to zero.
# You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt).
# Alternatively, you can type 'python -m pip install pycodestyle'.

from __future__ import print_function, unicode_literals
from pprint import pprint

f = open("D:\College\Degree\Python course by Kirk Byers\Week 2\Week 2 Exercises\show_ip_interfaces_brief.txt")
output = f.readlines()
pprint(output)
f.close()

for x in range(len(output)):
    if "FastEthernet" in output[x]:
        fastethernet = output[x]

print("\nEntry with only FastEthernet4 interfaces: ")
print(fastethernet)

print("\nSplitting into list...")
info = fastethernet.split()
print(info)

print("\nTaking only intfname and ip , converting to tuple ....")
new_info = tuple(info[0:2])
print("The variable new_info is type: ", type(new_info), "\nThe contents are:")
print(new_info)

