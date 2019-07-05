ip = '192.168.3.1'
list1 = ip.split('.')
ip_template = ''' 
     ...: {0:<10} {1:<10} {2:<10} {3:<10} 
     ...: {0:010b} {1:010b} {2:010b} {3:010b} 
     ...: '''  
print(ip_template.format(int(list1[0]), int(list1[1]), int(list1[2]), int(list1[3])))
