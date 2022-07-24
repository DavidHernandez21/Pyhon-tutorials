import re

# possessive quantifiers: .++, .*+, .?+, .{n,}+, .{n,m}+

reg = re.compile(r'".++"')

print(
    reg.match('"abc"'),
)  # do not match, .++ match until the end of the string i.e. " and does not backtrack

reg1 = re.compile(r'"[^"]++"')

print(reg1.match('"abc"'))
