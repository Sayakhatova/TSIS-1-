import re
file=open('./raw.txt', 'r', encoding='utf-8')
text=file.read()
cname=re.search(r'\nФилиал ТОО.*(?P<name>\b[A-Z]+)', text)
#print(cname.group('name'))
BIN=re.search(r'\nБИН.*(?P<bin>\b[0-9]+)', text)
#print(BIN.group('bin'))