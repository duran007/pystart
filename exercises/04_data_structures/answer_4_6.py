ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
list1 = ospf_route.split()
list1[0] = 'OSPF'
list1[2] = list1[2].strip('[]')
list1[4] = list1[4].strip(',')
list1[5] = list1[5].strip(',')
dict1 = {'Protocol': list1[0], 'Prefix': list1[1], 'AD/Metric': list1[2], 'Next-Hop': list1[4], 'Last update': list1[5], 'Outbound Interface': list1[6]}
