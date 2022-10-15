[video](https://www.youtube.com/watch?v=uwtupH7LJco)

directory tree
![alt_text](https://github.com/DavidHernandez21/Pyhon-tutorials/files/9791999/img.txt)

using python3 a/b/c/bar.py

```
['/home/david/antony_explains/**explicit_imports/a/b/c**', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
Traceback (most recent call last):
  File "a/b/c/bar.py", line 3, in <module>
    from .foo import x
ImportError: attempted relative import with no known parent package
```

using "modules" or "mod" option
python3 -m a.b.c.bar

```
['/home/david/antony_explains/**explicit_imports**', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
got x=1 from foo
imported a=<module 'a.a' from '/home/david/antony_explains/explicit_imports/a/a.py'> from a
imported b=<module 'a.b.b' from '/home/david/antony_explains/explicit_imports/a/b/b.py'> from b
```
