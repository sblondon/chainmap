chainmap
========

An attempt to implement ChainMap in python 2.7 like python 3.3

The main purpose was for experimenting only.
Reusing the cPython implementation (with only few change) could be a better
solution if someone plans to use ChainMap in production. See:
https://github.com/python/cpython/blob/master/Lib/collections/__init__.py


Use
---

The goal is to mimick the behaviour of collections.ChainMap.

```
$ python2 
Python 2.7.8 (default, Jul  4 2014, 13:08:34) 
[GCC 4.9.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import chainmap
>>> c = chainmap.ChainMap({"a": 1, "b": 2}, {"c": 3, "b": "ignored"})
>>> d = c.new_child()
>>> e = c.new_child()
>>> e.maps[0]
{}
>>> e.maps[-1]
{'c': 3, 'b': 'ignored'}
>>> d['b']
2
>>> d['b'] = 100
>>> d['b']
100
>>> del d['b']
>>> d['b']
2
>>> list(d)
['a', 'c', 'b']
>>> 'c' in d
True
>>> 'x' in d
False
>>> len(d)
3
>>> d.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> dict(d)
{'a': 1, 'c': 3, 'b': 2}
```


Target interface:
https://docs.python.org/3/library/collections.html#chainmap-objects


Execute tests
----------------
in root dir:
```
$ make check
```

Licence
-------

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation; either version 3 of the License, or (at your option) any
later version. The text of the license can be found in LICENCE file. 

