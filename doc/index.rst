.. toctree::
   :maxdepth: 2
   
   setup-other
   setup-spreadpi
   web_install
   web_interface
   gui
   cli
   tutorial
   faq
   drivers
   plugins
   contributing
   developers
   api
   chdk-tutorial
   changelog

About Spreads
=============

spreads is a software suite for the digitization of printed material. Its main
focus is to integrate existing solutions for individual parts of the scanning
workflow into a cohesive package that is intuitive to use and easy to extend.

At its core, it handles the communication with the imaging devices, the
post-processing of the captured material and its assembly into output formats
like PDF or ePub. On top of this base layer, we have built a variety of
interfaces that should fit into most use cases: A full-fledged and
mobile-friendly :doc:`web interface <web_interface>` that works on even the most
low-powered devices (like a Raspberry Pi, through the spreadpi distribution), a
:doc:`graphical wizard <gui>` for classical desktop users and a bare-bones
:doc:`command-line interface <cli>` for purists.

As for extensibility, we offer a plugin API that allows developers to hook into
almost every part of the architecture and extend the application according to
their needs. There are :ref:`interfaces for developing a device driver
<add_devices>` to communicate with new hardware, for writing new postprocessing
or output plugins to take advantage of a as of yet unsupported third-party
software. There is even the possibility to :ref:`create a completely new user
interface <add_commands>` that is better suited for specific environments.

The spreads core is completely written in the Python programming language,
which is widespread, easy to read and to learn (and beautiful on top of that).
Individual plugins also contain parts written in JavaScript and Lua. Through
the web-plugin it also offers a :doc:`REST(-ish) API <web_api>` that can be
accessed with any programming language that has a HTTP library.

**To get started we suggest you choose between one of two primary Spreads usage patterns to 
get up and running quickly:**

Spreads as an Appliance (SpreadPi)
----------------------------------
In this scenario Spreads is installed on a dedicated 
`Raspberry Pi <http://www.raspberrypi.org/>`_ computer which
controls the scanning process. The scanning cameras are attached to the Raspberry Pi. 
Once the page images are captured, they are transferred via a network connection 
to a general purpose computer for final processing. The Spreads software is controlled 
remotely via a network-based web interface running on the Raspberry Pi.

**Required:** Raspberry Pi B or B+, SD Card(8GB minimum), network connection (wired
connection recommended)

To get started:

   - :doc:`Installing SpreadPi<setup-spreadpi>`
   - :doc:`Using The Web Interface<web_interface>`

.. hint::
 
  SpreadPi is a special version of the Raspberry Pi operating system which has
  been optimized for running Spreads.  Although you can manually perform the Spreads 
  software install on a Raspberry Pi it is not recommended.
   
Spreads as a Software Utility
-----------------------------
In this scenario Spreads is installed on a general-purpose computer and the scanning
process is controlled from the command line, GUI interface or web interface on that
computer.  The scanner cameras are attached directly to the laptop or desktop computer 
and the entire process takes place in the local environment.

**Required:** Laptop or Desktop computer with Python 2.7 or 3.x installed

To get started:
  - :doc:`Command Line Installation and Configuration<setup-other>`
  - :doc:`GUI Installation and Configuration<gui>` (optional)
  - :doc:`Installing the Web Interface<web_install>` (optional)
Using Spreads:
  - :doc:`Command Line Tutorial<tutorial>`
  - :doc:`Command Line Reference<gui>`
  - :doc:`Using the Web Interface<web_interface>`

Next Steps
----------  
After you have Spreads up and running you may want to tailor the 
software to suit your workflow.  For example, you can login to the Raspberry
Pi device and issue command line commands via ssh. You can even use the 
:doc:`api` API to implement your own customization(s).  Because Spreads 
is implemented in a modular fashion there is a lot of flexibility available
for you to make Spreads fit the way you want to work.
 
.. note::

    In case you're wondering about the choice of mascot, the figure depicted is
    a Benedictine monk in his congregation's traditional costume, sourced from
    a `series of 17th century etchings`_ by the Bohemian artist `Wenceslaus
    Hollar`_, depicting the robes of various religious orders. The book he
    holds in his hand is no accident, but was likely deliberately chosen by the
    artist: The Benedictines_ used to be among the most prolific `copiers of
    books`_ in the middle-ages, preserving Europe's written cultural heritage,
    book spread for book spread, in a time when a lot of it was in danger of
    perishing.  *spreads* wants to help you do the same in the present day.
    Furthermore, the Benedictines were (and still are) very active
    missionaries, going out into the world and spreading 'the word'. *spreads*
    wants you to do the same with your digitized books (within the boundaries
    of copyright law, of course).

    .. _series of 17th century etchings: http://commons.wikimedia.org/wiki/Category:Clothing_of_religious_orders_by_Wenzel_Hollar
    .. _Wenceslaus Hollar: http://en.wikipedia.org/wiki/Wenceslaus_Hollar
    .. _Benedictines: http://en.wikipedia.org/wiki/Order_of_Saint_Benedict
    .. _copiers of books: http://en.wikipedia.org/wiki/Scriptorium
