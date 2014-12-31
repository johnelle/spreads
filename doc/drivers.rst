Device Drivers
==============

In order for your capture device to work with spreads, you need to tell the
application which driver it is supposed to use.
This can be either done by running the `configure` subcommand and selecting
one from the provided list or by manually editing the configuration file
in `.config/spreads/config.yaml` in your home directory.

Currently, the following drivers are available:

chdkcamera
----------
This driver should work with any Canon camera that runs the custom `CHDK`_
firmware in version 1.3 or higher.

For it to work, the `chdkptp`_ application must be installed in
`/usr/local/lib/chdkptp` (though that path can be configured, see below).
You also need to install the `pyusb` package, with either of the following
two commands::

    $ pip install spreads[chdkcamera]
    $ pip install pyusb

The following cameras have been tested and confirmed to work:

* A2200
* A810
* A410

If you own another CHDK-supported camera and have problems getting it to run
with this driver, please `open an issue on GitHub`_, we would love to make
it work.

The following configuration keys/command-line flags are available:

.. include:: fields.dat

.. program:: chdkcamera-driver

.. option:: --sensitivity <int>

   |iso|

.. option:: --shutter-speed <fraction>

   |shutter-speed|

.. option:: --zoom-level <int>

   |zoom-level|
   
.. option:: --dpi <int>

   |dpi|

.. option:: --shoot-raw

  |shoot-raw|

.. option:: --focus-distance <int/auto>

  |focus-distance|

.. option:: --chdkptp-path <path>

  |chdkptp-path|

.. _CHDK: http://chdk.wikia.com
.. _chdkptp: http://www.assembla.com/spaces/chdkptp
.. _open an issue on Github: http://github.com/DIYBookScanner/spreads/issues


gphoto2camera
-------------
This driver works with many PTP compatible camera.  The full list of
compatible cameras can be found here: http://www.gphoto.org/doc/remote/

For it to work, the following must be installed:

* libgphoto2: http://www.gphoto.org/
  This provides the low-level PTP interface.

  You can either build from source (http://sourceforge.net/projects/gphoto/files/)
  or install via your local package manager (apt, brew, etc).

  For example, on Mac OS X with brew installed:
    $ brew install gphoto2 libgphoto2

* piggyphoto: https://github.com/YesVideo/piggyphoto
  This is the python interface to libgphoto2.  The original source is
  https://github.com/alexdu/piggyphoto (our pull request to merge is pending).

  The easiest way to install is:
    $ pip install -e git://github.com/YesVideo/piggyphoto#egg=piggyphoto

The following cameras have been tested and confirmed to work:

* Canon T2i
* Canon 5D mk2

If you own another libgphoto2-supported camera and have problems getting it to run
with this driver, please `open an issue on GitHub`_, we would love to make
it work.

The following configuration keys/command-line flags are available:

.. program:: gphoto2-driver

.. option:: --iso <string>

   The ISO value.  Default is 'Auto'.

.. option:: --shutter-speed <fraction>

   The desired shutter speed as a fractional value. Default is 1/25.
   The equivalent key in the configuration file is `shutter_speed`.

.. option:: --aperture <float>

   The desired aperture expressed as an f-stop (without the 'f/' prefix). Default is 5.6.
   The equivalent key in the configuration file is `aperture`.

.. option:: --shoot-raw

   Shoot RAW images instead of JPEG. Please note that this setting is
   **highly experimental** at the moment and RAW files are not supported
   by the postprocessing and output plugins as of now.
   The equivalent key in the configuration file is `shoot_raw`.