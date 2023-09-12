# shoal

Experimental tasks that extends `calcipy`'s functionality

Documentation can be found on [GitHub (./docs)](./docs), [PyPi](https://pypi.org/project/shoal/), or [Hosted](https://shoal.kyleking.me/)!

---

Go file by file

Table: files

- Pk: file path
- str hash of file content for cache invalidation

Table: Call Stack

- PK: str, absolute import path (possible joint PK of name and path)
- str: list of raised exceptions (maybe column for caught?)
- row for each important line and column. Could be internal call, raises, or catches(but need to track as new context)

Display as tab indented list where same tab indent is parallel call path

Show relationship between functions, modules, and error handling?

Needs to handle reduce and more complicated ways code is called
