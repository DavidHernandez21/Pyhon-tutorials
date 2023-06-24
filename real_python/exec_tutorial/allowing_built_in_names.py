# disallowing built-in names
# exec("print(min([2, 3, 7, 4, 8]))", {"__builtins__": {}}, {})

allowed_builtins = {'__builtins__': {'min': min, 'print': print}}
exec('print(min([2, 3, 7, 4, 8]))', allowed_builtins, {})
