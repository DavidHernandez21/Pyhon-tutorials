code = """
z = x + y
"""

compiled_code = compile(code, '<string>', 'exec', optimize=2)

x = 42
y = 21

# exec(compiled_code, {"x": x})


exec(compiled_code, {'x': x, 'y': y})

# print(z) # NameError: name 'z' is not defined

exec(compiled_code)
print(z)


# using locals (mapping)
exec(compiled_code, {'x': x}, {'y': y})
print(z)
