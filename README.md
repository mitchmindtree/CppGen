CppGen.py
=========

CppGen.py generates a custom .cpp and .h file pair from a template.

Usage
-----

Using it is easy:

    $ python CppGen.py <destination> <name>...

CppGen.py will make a copy of both your .cpp and .h templates and place
them in the `<destination>` directory. Both the file names and every
instance of `TEMPLATE` within the files will be replaced with `<name>`.
Every instance of `DATE` will be replaced by the time and date.

CppGen.py will do this for every name following the directory (separate
each by a single whitespace).

You can also do this:

    $ python CppGen.py -d <name>...

where CppGen.py will just use it's own directory as the destination.

Or you can just do this:

    $ python CppGen.py

and follow the CLI prompts.

NOTE: I've included my own templates as an example - make sure you modify
them to your own liking! Just remember that they must have the names
"template.cpp" and "template.h".


Vim - Ready!
------------

CppGen.py is also ready as a vim plugin! Just do this:

    git clone https://github.com/mitchmindtree/CppGen.py.git ~/.vim/plugin

Or drag the CppGen folder into `~/.vim/plugin` (you might need to make the
`~/.vim/plugin` directory first). Ready to go!

Using CppGen.py as a vim plugin is even easier:

    :CppGen name1 name2 name3

This will generate your .cpp and .h files with name1, name2 and name3 in the
current working directory. You can generate as many files as will fit on the
line this way.


Dependency
----------

[Docopt] (http://docopt.org/) because it's so damn easy to make CLIs with it.

Just do this:

    $ pip install docopt

and you're ready to go.


Enjoy
-----

by Mitchell Nordine
