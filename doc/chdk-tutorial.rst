Tutorial: Gathering Information from CHDK Cameras
=================================================

Introduction
------------

If your camera is attached to Spreads via the CHDK driver, spreads reads the values
you provide in the various settings fields and passes them on to the 
CHDK firmware running in the camera. This means it is often useful to understand 
a little more about how CHDK *sees* your camera so that you can better understand 
how the values you provide are used.

This tutorial introduces a method for querying your camera interactively via the same
command interface used by Spreads.  We will be using one of the command line utilities **chdkptp**,
which is part of the chdk installation package on Linux and Raspberry Pi. 
It accepts commands in the so-called "Lua" scripting language syntax and
then returns any information from the camera back to the command line.

Understanding all CHDK commands is well beyond the scope of this tutorial.  
For detailed information on the various commands and scripting syntax it's best to consult the 
`CHDK Scripting Cross Reference <http://chdk.wikia.com/wiki/CHDK_Scripting_Cross_Reference_Page/>`_
pages.  That said, below are a series of commands which may be specifically useful to a Spreads
user.

The utility chdkptp is available on the command line.  If you are a SpreadPi user you
will have to ssh to the SpreadPi terminal to use chdkptp.  The common syntax for calling CHDK functions
is:

::

    1>=return get_stuff()  # call a function get stuff
    2:return:<value>       # function returned <value>

There is a brief tutorial on `using chdkptp <https://www.assembla.com/spaces/chdkptp/wiki/CLI_Quickstart>`_
if you want more details on other commands available.  For most of the examples below you will have to
be connected to a camera (via the connect command) to send the command to the camera.

Useful Command Examples
------------------------

.. topic:: Start chdkptp and list the attached cameras
	
  | $chdkptp 
  | ___> list
  | -1:Canon PowerShot A1400 b=001 d=006 v=0x4a9 p=0x3264 s=E93ED539C20C4C2F97D10CDA99649CE
  | -2:Canon PowerShot A1400 b=001 d=005 v=0x4a9 p=0x3264 s=77F52A1DFE1F497CB20E2B8CB3E22B71

.. topic:: Connect to one of the cameras via serial number

  | ___> connect -s=E93ED539C20C4C2F97D10CDA99649CEB
  | connected: Canon PowerShot A1400, max packet size 512

.. topic:: Get the number of zoom steps for the camera

  | con 35> =return get_zoom_steps()
  | 36:return:64

.. topic:: Return the current focus mode of the camera

  | con 50> =return get_focus_mode()
  | 51:return:0
  
  (focus mode, 0=auto, 1=MF, 3=inf., 4=macro, 5=supermacro)

  
.. topic:: Get the ISO mode of the camera

  | con 64> =return get_iso_mode()
  | 65:return:0
  
  (0 = auto iso, otherwise the ISO number)

.. topic:: Get various properties

  | con 69> =return get_prop(21)
  | 70:return:1

  ========  ====================================================================
  Prop_ID   Description
  ========  ====================================================================
  0         Shooting mode dial position
  1         Photo effect
  5         White balance
  6         Drive mode (S3 values: 0=single, 1=continuous, 2=timer)
  8         Hi-speed continuous mode (S3: 1=OFF, 0=ON
  9         Metering mode (S3 values: 0=eval 1=spot 2=center)
  11        Macro (S3 values: 0=normal, 1=macro, 2=super mac)
  12        Manual Focus (S3 values: 1=manual, 0=auto)
  14        Delay of selftimer (appears to be time in milliseconds)
  16        Flash mode (s3: 2=flash closed, otherwise 0=auto, 1=ON)
  18        Red eye mode (S3: 0=OFF, 1=ON)
  19        Flash slow sync (S3: 0=OFF, 1=ON)
  20        Flash Sync Curtain (S3: 0= first, 1 = second)
  21        ISO value (S3: 0=auto, 1=ISO-HI, or actual ISO: 80,100,200,400,800)
  23        Image quality (S3 values: 0,1,2 from best to worst)
  24        Image resolution (S3 values: 0,1,2,4,8 for L,M1,M2,S,W)
  25,26     EV correction (positive or negative, 96 units per stop)
  28        Flash correction (same units as 25,26)
  32        Exp bracket range (Same units as 25/26: e.g. 96 = +/- 1 stop range)
  34        Focus bracket range 2=Smallest, 1=Medium, 0=largest
  36        Bracket mode: 0=NONE, 1 = exposure, 2 = focus
  37        Orientation sensor
  39        Chosen Av (by user)
  40        Chosen Tv (by user)
  65        Focus distance
  67        Focus ok: 1=Yes, 0=NO
  68        Coming Av
  69        Coming Tv
  74        AE lock: 1=ON, 0=OFF
  126       Video FPS (15, 30 or 60.  don't change here!)
  127,128   Video resolution (S3: 2,1 for 640x480; 1,0 for 320x240)
  177       intervalometer: #of shots (0 if not activated)
  205       0 '1' during shooting process
  206       "MyColors?" mode (See link below)
  218       Custom timer continuous: # of shots to be taken
  219       Self Timer setting: 0=2 sec, 1=10 sec, 2=custom continuous
  ========  ====================================================================
.. topic:: Return information relevant to "depth of field" 

  | con 56> =return get_dofinfo()
  | 57:return:table:{hyp_valid=false,
  |               eff_focal_length=28000,
  |               coc=5,aperture=7914,
  |               near=-1,
  |               min_stack_dist=18,
  |               dof=-1,
  |               focal_length=5000
  |               hyp_dist=637,
  |               far=-1,
  |               focus=-1,
  |               focus_valid=false,}

   =============================  =====================================
    Field                          Description
   =============================  ===================================== 
   hyp_valid [boolean] -          Is hyperfocal distance valid?
   eff_focal_length [x 1000 mm]   35mm equivalent focal length
   coc [x 1000 mm]                circle of confusion
   aperture [x 1000]              aperture
   near [mm]                      near limit
   min_stack_dist [mm]            smallest meaningful stack distance
   dof [mm]                       DOF
   focal_length [x 1000 mm]       focal length
   hyp_dist [mm]                  hyperfocal distance
   far [mm]                       far limit
   focus [mm]                     focus distance
   focus_valid [boolean]          Is focus valid?
   ====================================================================

.. topic:: Just for fun..play the shutter click sound

   | con 43> =play_sound(1)
   | con 44>
