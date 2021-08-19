ProtoTurk
=========

A simple server and script for rapidly prototyping Mechanical Turk
interfaces.

prototurk server
----------------

The ProtoTurk package provides ``prototurk``, a Bottle_-based
webserver for rapidly prototyping Mechanical Turk interfaces.
``prototurk`` takes Mechanical-Turk compatible HTML templates and CSV
files as arguments::

    prototurk [--host hostname] [--port port_number] html_file csv_file

and starts a webserver that, by default, listens on localhost
port 8080.  ``prototurk`` re-reads the HTML template and CSV file from
disk with every page refresh.  When a user submits the HTML template's
form, the form parameters are logged to stdout.

``prototurk`` does not save any data to database or disk.  If you need
to run a Mechanical Turk-style server in your Local Environment,
please take a look at Turkle_.

prototurk-populate script
-------------------------

The ProtoTurk package also includes ``prototurk-populate``, a simple
script that takes as arguments the path to a Mechanical-Turk
compatible HTML template, the path to a CSV file, and the (1-indexed)
row number for the data to use from the CSV file::

    prototurk-populate [--output-file OUTPUT_FILE] html_file csv_file csv_row_number

The script outputs a populated HTML template, where the template
variables have been replaced with values from the row of the CSV file.
By default, ``prototurk-populate`` writes the populated HTML template
to stdout, but the ``--output-file`` flag can alternately be used to
write the populated output directly to a (UTF-8 encoded) file.

``prototurk-populate`` makes it easier to validate Mechanical Turk
template files using HTML and JavaScript validation tools.  Most
popular HTML/JavaScript will generate errors about Mechanical
Turk-style template variables.  ``prototurk-populate`` makes it easier
to validate populated templates with real data, particularly as part
of Continuous Integration workflows.


Installation
------------

ProtoTurk can be installed using::

    python setup.py install

Or from PyPI::

    pip install prototurk

.. _Bottle: https://www.bottlepy.org
.. _Turkle: https://github.com/hltcoe/turkle
