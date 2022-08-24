import jmespath

data = {
    'Contents': [
        {'Date': '2014-12-21T05:18:08.000Z', 'Key': 'logs/bb', 'Size': 303},
        {'Date': '2014-12-20T05:19:10.000Z', 'Key': 'logs/aa', 'Size': 308},
        {'Date': '2014-12-20T05:19:12.000Z', 'Key': 'logs/qux', 'Size': 297},
        {'Date': '2014-11-20T05:22:23.000Z', 'Key': 'logs/baz', 'Size': 329},
        {'Date': '2014-12-20T05:25:24.000Z', 'Key': 'logs/bar', 'Size': 604},
        {'Date': '2014-12-20T05:27:12.000Z', 'Key': 'logs/foo', 'Size': 647},
    ],
}


print(jmespath.search('sort_by(Contents, &Date)[1:3].{Key: Key, Size: Size}', data))
print(jmespath.search('sort_by(Contents, &Date)[*].{Key: Key, Size: Size}', data))
print(jmespath.search('sort_by(Contents, &Size)[::-1].{Key: Key, Size: Size}', data))
