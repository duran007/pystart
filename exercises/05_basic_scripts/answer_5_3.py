#!/usr/bin/env python3
mode = input('Input interface mode (access/trunk): ')
interface = input('Input interface type and number: ')
vlans = input('Input vlans: ')

template_list = [
[
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
],
[
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
]
template_indexes = ['access', 'trunk']
index1 = template_indexes.index(mode)
print('-'*30)
print('Interface {}'.format(interface))
print('\n'.join(template_list[index1]).format(vlans))

