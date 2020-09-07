#3. Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator.
# The second variable should use all upper case characters with underscore as the word separator.
# The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.
#
#Make all three variables be strings that refer to IPv6 addresses.
#
#Use the from future technique so that any string literals in Python2 are unicode.
#
#compare if variable1 equals variable2
#compare if variable1 is not equal to variable3

from __future__ import print_function, unicode_literals

var_one = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
VAR_TWO = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
var_3 = "fe80::1ff:fe23:4567:890a"

print(f"""Variable one is {var_one} 
Variable two is {VAR_TWO} 
Variable three is {var_3} """)

print("Is variable one equal to variable two ?" , var_one == VAR_TWO)
print("Is variable 1 not equal to variable three? ", var_one!= var_3)