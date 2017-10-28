from setuptools import setup

setup(
    name = 'doxml',
    version = '1.0',
    description = 'Extract XML from C/C++ documentation comments using Doxygen.',
    author = 'Matthew Brush',
    author_email = 'mbrush@codebrainz.ca',
    url = 'https://github.com/codebrainz/doxml',
    scripts = [ 'doxml' ],
    install_requires = [ 'lxml' ]
)
