import re
lin = 'my name is pranjal@33321.ert.75.f is the best'
y = re.findall('.*', lin)
print(y)
y = re.findall('@([^ ]*)', lin)
print(y)
# starting with my having  @ extract sigle non blank character zero or more times
y = re.findall('^my @(\S+)', lin)
print(y)
y = re.findall('\S+?@\S+?', lin)
print(y)
