chainmap
========

An attempt to implement ChainMap in python 2.7 like python 3.3

Use
---
instead of:
import collections
collections.ChainMap()

use:
import chainmap
chainmap.ChainMap()

The goal is to mimick the behaviour of collections.ChainMap.

Target interface:
https://docs.python.org/3/library/collections.html#chainmap-objects


Execute tests
----------------
in root dir:

$ make check


Licence
-------

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation; either version 3 of the License, or (at your option) any
later version. The text of the license can be found in LICENCE file. 

