import re

show_output = """RTB# show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
 D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
 N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
 E1 - OSPF external type 1, E2 - OSPF external type 2
 i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
 * - candidate default, U - per-user static route, o - ODR
 P - periodic downloaded static route
Gateway of last resort is not set
 2.0.0.0/24 is subnetted, 1 subnets
C 2.2.2.0 is directly connected, Ethernet0/0
C 3.0.0.0/8 is directly connected, Serial1/0
O N2 200.1.1.0/24 [110/94] via 2.2.2.1, 00:11:12, Ethernet0/0
O N1 200.2.2.0/24 [110/20] via 2.2.2.2, 00:12:23, Ethernet0/0
 131.108.0.0/24 is subnetted, 2 subnets
O IA 141.108.1.0 [110/84] via 2.2.2.1, 00:12:11, Ethernet0/0
O IA 151.108.1.0 [110/84] via 2.2.2.1, 00:12:11, Ethernet0/0
O 131.108.2.0 [110/74] via 2.2.2.2, 00:12:23, Ethernet0/0
O IA 131.108.1.0 [110/84] via 2.2.2.2, 00:12:11, Ethernet0/0"""

user_input = input("Enter route code: ")

regEx = r"^%s\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)" \
        ".*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"%user_input

for lines in show_output.split('\n'):
    match = re.search(regEx, lines)
    if match:
        print(match.group(1))
        print(match.group(2))















