CppGen.py
=========

CppGen.py generates a custom .cpp and .h file pair from a template.

Using it is easy:

    $ python CppGen.py <destination> <name>...

CppGen.py will make a copy of both your .cpp and .h templates and place
them in the `<destination>` directory. Both the file names and every
instance of `TEMPLATE` within the files will be replaced with `<name>`.
Every instance of `DATE` will be replaced by the time and date. CppGen.py
will do this for every name following the directory (each separated by a
single whitespace).

You can also do this:

    $ python CppGen.py -d <name>...

where CppGen.py will just use it's own directory as the destination.

Or you can just do this:

    $ python CppGen.py

and follow the CLI prompts.

NOTE: I've included my own templates as an example - make sure you modify
them to your own liking! Just remember that they must have the names
"template.cpp" and "template.h".


Dependency
----------

(Docopt)[http://docopt.org/] because it's so damn easy to make CLIs with it.

Just do this:

    $ pip install docopt

and you're ready to go.


ToDo
----

- Make a Vim plug-in i.e. `:CppGen 'name1' 'name2' 'name3' etc`

