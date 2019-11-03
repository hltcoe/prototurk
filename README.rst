ProtoTurk
=========

Simple server for rapidly prototyping Mechanical Turk interfaces.

ProtoTurk provides a Bottle_-based webserver for rapidly prototyping
Mechanical Turk interfaces.  ProtoTurk takes Mechanical-Turk
compatible HTML templates and CSV files as arguments::

    prototurk [--host hostname] [--port port_number] html_file csv_file

and starts a webserver that, by default, listens on localhost
port 8080.  ProtoTurk re-reads the HTML template and CSV file from
disk with every page refresh.  When a user submits the HTML template's
form, the form parameters are logged to stdout.

ProtoTurk does not save any data to database or disk.  If you need to
run a Mechanical Turk-style server in your Local Environment, please
take a look at Turkle_.

ProtoTurk can be installed using::

    python setup.py install

Or from PyPI::

    pip install prototurk

.. _Bottle: https://www.bottlepy.org
.. _Turkle: https://github.com/hltcoe/turkle
