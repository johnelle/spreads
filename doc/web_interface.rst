Web Interface
=============

Connection on a General-Purpose Computer
----------------------------------------
You can connect to the interface by opening your browser on an address that
looks like this::

    http://<host-ip-address>:5000

If you are running spreads in your local machine, using `localhost` or
`127.0.0.1` for the IP address will be enough. If you are running it on a
remote machine, you will have to find out its IP address. When you are
using CHDK cameras and have them turned on when you launch spreads, their
displays will show the IP address of the computer they are connected to.

Connection to SpreadPi
----------------------
By default the web interface to Spreads runs on port 80 so you simply need to point
your browser to the ip address of the Raspberry Pi running SpreadPi::

	http://<raspberry-pi-ip-address>

.. hint::
 
  By default SpreadPi used the nodename "spreadpi" on the network.  If you
  review the list of connected devices on your router it should be easy to 
  find the address of spreadpi, even when DHCP moves the assignment to a 
  different address.  
	
Using the Web Interface Basics
------------------------------

The **initial screen** will list all previously created workflows with a small
preview image and some information on their status. On clicking one of the
workflows, you will be taken to its details page where you can view all
of the images and see more information on it. You can also choose to download
a ZIP file with the workflow, containing all images and a configuration file.

.. figure:: _static/web_list.png

Workflow List

From the navigation bar, you can choose to **create a new workflow**. The only
setting you absolutely have to enter is the workflow name. You can also change
driver and plugin settings for this workflow by selecting either one from the
dropdown menu. When you are done, you can submit the workflow and the
application will take you to the capture screen.

.. figure:: _static/web_create.png

Workflow Creation

On the **capture screen**, you can see two small review images with which
you can verify that the last capture went well. Trigger a new capture by
clicking the appropriate button and you will see the images update.
If you spotted an error, you can click the *Rektake* button, which will discard
the last capture and trigger a new one. Once you are done, use the *finish*
button.

.. figure:: _static/web_capture.png

