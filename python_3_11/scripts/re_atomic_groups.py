import re

#  atomic groups: (?>...)

reg = re.compile(r'a(?>bc|b)c')

print(reg.match('abc'))  # Do not match due to the aotmic group, it does not backtrack
print(reg.match('abcc'))
