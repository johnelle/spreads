# -*- coding: utf-8 -*-

# Copyright (c) 2013 Johannes Baiter. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import division, unicode_literals

import logging
import subprocess
import sys


class BaseCamera(object):
    """ Base class for cameras.

        Subclass to implement support for different cameras.

    """
    @classmethod
    def match(cls, vendor_id, product_id):
        """ Match camera against USB device information.

        :param vendor_id:   idVendor of the USB device
        :type vendor_id:    unicode (hex, zero-padded to 4, e.g. "04a1")
        :param product_id:  idProduct of the USB device
        :type product_id:   unicode (hex, zero-padded to 4, e.g. "12a3")
        :return:            True if the IDs match the implemented model

        """
        raise NotImplementedError

    def __init__(self, bus, device):
        """ Set connection information and try to retrieve orientation.

        :param bus:     USB bus number of the camera
        :type bus:      int, str, unicode
        :param device:  USB device number of the camera
        :type bus:      int, str, unicode

        """
        self._port = (int(bus), int(device))
        self.orientation = (self._gphoto2(["--get-config",
                                           "/main/settings/ownername"])
                            .split("\n")[-2][9:] or None)

    def _gphoto2(self, args):
        """ Call gphoto2.

        :param args:  The arguments for gphoto2
        :type args:   list
        :returns:     unicode -- combined stdout and stderr of the gphoto2
                                    process.

        """
        cmd = (["gphoto2", "--port", "usb:{0:03},{1:03}".format(*self._port)]
               + args)
        logging.debug("Running " + " ".join(cmd))
        try:
            out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except OSError:
            logging.error("gphoto2 executable could not be found, please"
                          "install!")
            sys.exit(0)
        return out

    def _ptpcam(self, command):
        """ Call ptpcam to execute command on camera.

        :param command: The CHDK command to execute on the camera
        :type command:  unicode
        :returns:       unicode -- combined stdout and stderr of the ptpcam
                                    process

        """
        bus, device = self._port
        cmd = ["ptpcam", "--dev={0:03}".format(device),
               "--bus={0:03}".format(bus),
               "--chdk='{0}'".format(command)]
        logging.debug("Running " + " ".join(cmd))
        try:
            out = subprocess.check_output(" ".join(cmd), shell=True,
                                          stderr=subprocess.STDOUT)
        except OSError:
            logging.error("ptpcam executable could not be found, please"
                          "install!")
            sys.exit(0)
        return out

    def set_orientation(self, orientation):
        """ Set the camera orientation.

        :param orientation: The orientation name
        :type orientation:  unicode in (u"left", u"right")

        """
        self._gphoto2(["--set-config",
                       "/main/settings/ownername={0}".format(orientation)])
        self.orientation = orientation

    def delete_files(self):
        """ Delete all files from camera. """
        raise NotImplementedError

    def download_files(self, path):
        """ Download all files from camera.

        :param path:  The destination path for the downloaded images
        :type path:   unicode

        """
        raise NotImplementedError

    def set_record_mode(self):
        """ Put the camera in record mode. """
        raise NotImplementedError

    def get_zoom(self):
        """ Get current zoom level.

        :returns: int -- the current zoom level

        """
        raise NotImplementedError

    def set_zoom(self, level):
        """ Set zoom level.

        :param level: The zoom level to be used
        :type level:  int

        """
        raise NotImplementedError

    def disable_flash(self):
        """ Disable the camera's flash. """
        raise NotImplementedError

    def set_iso(self, iso_value):
        """ Set the camera's ISO value.

        :param iso_value: The ISO value in ISO/ASA format
        :type iso-value:  int

        """
        raise NotImplementedError

    def disable_ndfilter(self):
        """ Disable the camera's ND Filter. """
        raise NotImplementedError

    def shoot(self, shutter_speed, iso_value):
        """ Shoot a picture.

        :param shutter_speed: The shutter speed to be used
        :type shutter_speed:  float (e.g. 64.0 or 1/25)

        """
        raise NotImplementedError

    def play_sound(self, sound_num):
        """ Play sound.

        :param sound_num: The ID of the sound
        :type sound_num:  int

        """
        raise NotImplementedError