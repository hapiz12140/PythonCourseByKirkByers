#4. Create a show_version variable that contains the following

# show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
#Remove all leading and trailing whitespace from the string.
#Split the string and extract the model and serial_number from it.
#Check if 'Cisco' is contained in the model string (ignore capitalization).
#Check if '881' is in the model string.
#Print out both the serial number and the model.

from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.rstrip()

details = show_version.split()

model = details[1]
serial_number = details [2]

print(r"Is there 'Cisco' in ",model, " ?", "Cisco".lower() in model.lower())
print(r"Is there '881' in ",model, " ?", "881" in model)
print(r"The model is ",model, " and the serial number is ", serial_number)