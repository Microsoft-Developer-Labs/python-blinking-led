# Python Blinking LED With The Raspberry Pi's GPIO Pins
Feel free to copy and share.

If some of you don't even know what a Raspberry Pi is, it's a Linux based computer running Raspbian OS.

Order Raspberry Pi's here:

[Visit Website](https://www.canakit.com/)

## What are GPIO pins?
GPIO pins are the various header pins that stick out of the Raspberry Pi's motherboard. Usually people attach these to breadboards using ribbon cable and a cobbler. The cobber has an insert for the ribbon cable that connects to the GPIO pins.

## Setup
1. Place Cobbler on breadboard

![](http://www.raspberrypi.org/wp-content/uploads/2012/11/t-cobbler.jpg?raw=true)

2. Place ribbon cable on the GPIO pins and connect it to the cobbler.

# IMPORTANT!!!
3. As for the LED to blink in the program, you need to connect the positive LED pin to the correct pin number it's assigned to in the python code. Our default pin number is __PIN 11__. The positive goes in __PIN 11__, and the negative pin of the LED goes into the __GND__. Of course, you can change this is you ever want to.

4. This step requires the Raspberry Pi terminal. For a shortcut to the terminal just press __CTRL + ALT + T__.

You should see this window:

![](http://1.bp.blogspot.com/-n5b6Qjw1Ltk/UQpdU1Z3_uI/AAAAAAAAAEs/lf-imDaNQdk/s1600/lxterminal.jpg?raw=true)

If you see this window, great! That's what should happen. Now navigate to the directory the python code is in by using `cd your/dir/here`

After you're in the directory, make sure either your __root@raspberrypi__ or you enter the `sudo` command.

## To make yourself root@raspberrypi

All you have to do is type in `sudo su`, then type `python Program.py`.

## To run the program as pi@raspberrypi

To run this program as the user __pi__, all you need to type is `sudo python Program.py`

&copy; Microsoft Corporation 2018. All rights reserved.
