with open('hello.py', mode='r', encoding='utf-8') as f:
    content = f.read()

# print(content)
exec(content)

greet(name='David')
