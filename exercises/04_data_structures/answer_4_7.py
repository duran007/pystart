mac = 'AAAA:BBBB:CCCC'
list1=mac.split(':')
str1 = ''.join([str(i) for i in list1])
bin(int(str1,16))[2::]
