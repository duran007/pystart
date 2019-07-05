#!/usr/bin/env python3
var = input('Print subnet IP-address: ')
list1 = var.split('/')
network = list1[0].split('.')
mask_bin = '1'*int(list1[1])+'0'*(32-int(list1[1]))
mask_list = [int(mask_bin[0:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:32],2)]
network_template = ''' 
     ...: Network: 
     ...: {0:<8} {1:<8} {2:<8} {3:<8} 
     ...: {0:08b} {1:08b} {2:08b} {3:08b} 
     ...: ''' 
mask_template = ''' 
     ...: Mask: 
     ...: /{4:} 
     ...: {0:<8} {1:<8} {2:<8} {3:<8} 
     ...: {0:08b} {1:08b} {2:08b} {3:08b} 
     ...: ''' 
print(network_template.format(int(network[0]),int(network[1]),int(network[2]),int(network[3])))
print(mask_template.format(int(mask_list[0]),int(mask_list[1]),int(mask_list[2]),int(mask_list[3]),int(list1[1])))
