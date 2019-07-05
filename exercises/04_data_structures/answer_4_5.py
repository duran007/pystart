command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
vlan1 = (command1.split()[-1]).split(',') 
vlan2 = (command2.split()[-1]).split(',')
list1 = list(set(vlan1).intersection(vlan2))
list1.sort()
list1
