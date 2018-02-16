Title: Tangible interface tables
Date: 2018-02-08

[Slides](https://docs.google.com/presentation/d/1LrSjeT7zTV3mismZ41-fcisdNBFVRaTPRy6lJ0BwU-4/edit?usp=sharing)

TLTL is the proud home of four home-made tangible user interface tables. These are interesting
interfaces because they support physical interaction with programmed environments in a 
context well-suited to social play. They are also an excellent example of how our digital fabrication technologies
can be combined in powerful ways.

## Architecture

<img src="https://www.tuio.org/images/diagram.png" style="width:50%;">

The diagram above (from [TUIO.org](https://tuio.org), where you can read much more) shows the general architecture. A projector 
connected to your computer (probably running a Processing program) displays an image on the table 
surface from below. At the same time, a program called [ReacTIVision](http://reactivision.sourceforge.net/) uses a camera (also connected to your computer) to 
watch for interactions with physical objects on the tabletop.

<img src="{filename}/images/fiducials.png" style="width:50%;">

[ReacTIVision](http://reactivision.sourceforge.net/) watches for specific patterns, called fiducials,
and broadcasts a stream 
of data about their positions and orientations. You can use a Processing library called 
[TUIO Processing](https://www.tuio.org/?software) to write a program which listens to the stream of 
information about the fiducials. Your program can react to these and update what it draws to the screen. If you attach
fiducials to the bottom of physical objects, your program can then respond to their positions on the table.

During testing, we found that the projected images sometimes interfered with recognizing the fiducials. Therefore, we 
decided to use an infrared camera (instead of visible light) to detect fiducials. We use arrays of infrared LEDs to
illuminate the underside of the table with infrared light.

## Step by step

- Install [ReacTIVision](http://reactivision.sourceforge.net/). While it is running, you should see a window like the one below. 
  Press `h` to see the configuration options.

  <img src="{filename}/images/chris_react.png" style="width:40%;">

- Print out the fiducial patterns ([PDF](http://reactivision.sourceforge.net/data/fiducials.pdf)) and hold them in view of your 
  webcam. You should see them identified in the reacTIVision window. 
- Install the [TUIO Processing](https://www.tuio.org/?software) library. Download and unzip the folder, and then put it in the `libraries` folder
  inside your processing home directory. 
- Write a Processing program which listens for TUIO events (To see examples, use the demo app that comes with the [TUIO Processing](https://www.tuio.org/?software) library, or see Chris's [hospitals](https://github.com/cproctor/hospitals/releases) game). 
  You should be able to control it using fiducials held up to your webcam. 
- Once your program is working on your computer, connect your computer to the TUI table. You will need to connect to the table's projector
  (VGA) and to the camera (USB). Check the TUI table's systems:
    - Is the projector on and displaying your screen? You can adjust the mirror position under the table to align the image.
    - Is the camera plugged in and sending an image to reacTIVision? 
    - Are the LED arrays turned on? If not, the camera's image will be very dark. 
- Now you need to calibrate reacTIVision so that the camera's coordinates match the display coordinates. You have two options: 
    - Use the built-in calibration (press `h` for controls; `c` to enter calibration mode, and arrow keys plus `awdx` to adjust the calibration grid)
    - Bertrand Schneider, who graduated from TLTL and now teaches at Harvard, wrote a handy [calibration plugin](https://github.com/schneibe/Reactivision-Calibration)
      you can add to your program, so you don't have to re-calibrate it every time you restart.
- If reacTIVision is not detecting fiducials well, try adjusting the gradient gate (`g`) and the camera options (`o`). If all else 
  fails, try larger fiducials.
