Web Install and Configuration
=============================
.. _web-install:

Installation
------------
To install the required dependencies for the web plugin, run the following
command::

    $ pip install spreads[web]

Alternatively, make sure you have the following modules installed in their
most recent versions:

* Flask
* Flask-Compress
* jpegtran-cffi
* requests
* waitress
* zipstream

To use the JavaScript web interface, make sure you use a recent version of
Firefox or Chrome.

Startup and Configuration
-------------------------
You can launch the web interface with its subcommand::

    $ spread web [OPTIONS]

This will serve the spreads web interface and its RESTish-API on port 5000
for the whole network. There are a number of options with which you can


.. option:: --database <path>

   Location of workflow database, by default `~/.config/spreads/workflows.db`

.. option:: --standalone-device

   Enable standalone mode. This option can be used for devices that are
   dedicated to scanning (e.g. a RaspberryPi that runs spreads and nothing
   else). At the moment the only additional feature it enables is the ability
   to shutdown the device from the web interface and REST API.

.. option:: --debug

   Run the application in debugging mode. This activates source maps in the
   client-side code, which will increase the initial loading time significantly.

.. option:: --project-dir <path>

   Location where workflow files are stored. By default this is `~/scans`.

