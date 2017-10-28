doxml
=====

The [doxml][doxml] utility drives [Doxygen][doxygen], causing it to
produce its XML output. The resulting XML is minimized and cleaned of
empty nodes, ready for further processing.

Requirements
------------

- [Python 3.6][py36] or greater
- [LXML 4.0][lxml4] or greater

Installation
------------

To install [doxml][doxml], use [pip][pip] passing the [doxml][doxml]
source directory.

For exmaple:

```
$ pip install /path/to/doxml
```

Command-Line Arguments
----------------------

### `-o`, `--output-file`

This option forces the generated output to be written to the specified
file. If the specified file is empty or `-` then the output is written
to [standard output][stdout].

### `-i`, `--include`

Zero or more patterns matching files to process with [Doxygen][doxygen].

### `-e`, `--exclude`

Zero or more patterns to exclude from [Doxygen][doxygen] processing.

### `-c`, `--config`

A file containg [Doxyfile][doxyfile]-like entries to be passed to
[Doxygen][doxygen]. The options specified in this file may be
overwritten by more specific options.

### `-d`, `--dump-config`

Rather than running [Doxygen][doxygen], just print on
[standard output][stdout] the options that would be passed to it.

Environment
-----------

The following environment variables affect the operation of
[doxml][doxml].

### `DOXYGEN`

The `DOXYGEN` environment variable specifies the path to the
[Doxygen][doxygen] utility. If omitted, the default `doxygen` name is
used. If you have not specified the `DOXYGEN` environment variable, you
should ensure that the `doxygen` program is available in one of the
directories specified in the `PATH` environment variable, or on
Windows, within the current directory.

[doxml]: https://github.com/codebrainz/doxml
[doxyfile]: https://www.stack.nl/~dimitri/doxygen/manual/config.html
[doxygen]: http://www.stack.nl/~dimitri/doxygen/
[lxml4]: http://lxml.de/
[pip]: https://pypi.python.org/pypi/pip
[py36]: https://www.python.org/downloads/release/python-360/
[stdout]: https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
