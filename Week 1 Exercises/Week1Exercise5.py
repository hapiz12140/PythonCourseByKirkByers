#5. You have the following three variables from the arp table of a router:
#
#mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
#mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
#mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
#
#Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:
#
#             IP ADDR          MAC ADDRESS
#-------------------- --------------------
#        10.220.88.29       5254.abbe.5b7b
#        10.220.88.30       5254.ab71.e119
#        10.220.88.32       5254.abc7.26aa
#
#Two columns, 20 characters wide, data right aligned, a header column.

from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

info1 = mac1.split()
info2 = mac2.split()
info3 = mac3.split()

ipaddr1 = info1[1]
ipaddr2 = info2[1]
ipaddr3 = info3[1]

macadd1 = info1[3]
macadd2 = info2[3]
macadd3 = info3[3]

print(f"{'IP ADDR':>20}{'MAC ADDRESS' :>20}")
print(f"{'-'*19:>20}{'-'*19:>20}")
print(f"{ipaddr1:>20}{macadd1:>20}")
print(f"{ipaddr2:>20}{macadd2:>20}")
print(f"{ipaddr3:>20}{macadd3:>20}")