config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config[30:].split(',')


config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
list1 = config.split()
list1[-1].split(',')
