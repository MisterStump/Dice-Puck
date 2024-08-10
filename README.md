![Imgur](https://imgur.com/mSfZSoT)

# Overview
The goal of this project was to make a little pocket digital dice roller that worked with the standard 7 polyhedral dice used in games like D&D. This GitHub contains the things I purchased, build, or coded. I hope that if anyone else is interested in a project like this, they can use this as a rough guide. Or maybe just provide some insight to anyone interested into some of the challenges I ran into.

## Features
- Select a d4, d6, d8, d10, d12, d20, or d100, as well as how many of them to roll
- Roll the dice and see up to 14 individual results as well as the total
    - More than 14 dice can still be rolled but the individual results are all layers on top of eachother randomly
- Sleep mode to help extend battery life when not in use

## Functionality
The Dice Puck is always on when powered. It has 2 main screens and a sleep mode, all with different controls. Note that you can only roll 1 type of die at a time, and it does not apply any modifiers. The screen will go to sleep after 1 minute without use.
- Mode: Roll Selection
    - Drag up/down = increase/decrease # of dice to roll
    - Drag left/right = change which die type to roll
    - Press and hold  = Reset # of dice to roll to 0
    - Shake = Roll the currently selected die
- Mode: Roll Results
    - Press and hold = return to the Roll Selection screen
- Mode: Sleep
    - Press and hold = wake up

## Parts
There are 3 physical components to this project.

- Purchased Parts
    - ESP32-S3 development board with screen and sensors
        - https://www.waveshare.com/esp32-s3-touch-lcd-1.28.htm
    - Battery: 3.7v - 220mAh - JST PH1.25
        - https://www.amazon.com/dp/B0CHY5NBM2
- Printed Parts
    - Case requires a 3d printer to produce. I used a Prusa Mk3s+

# Development
The journey to create and run this project was involved and I was able to learn a lot. I'll outline my general journey and resources here, if you want to follow a similar path. In the next section I'll outline problems I encountered that you should be aware of if you want to do something similar.

## Image conversion
Getting images into the correct format and size was a pain. I had to save vector graphics (svc), export them into png to set the background color & dimensions, then convert them to jpg using a command line utility called ImageMagik. There are "source.txt" files in the image folders that give a little more detail.

## Font conversion
I used a python script called front2bitmap.py to convert a truetype font (UniversCondened.tff) into a file that MicroPython could render. The font is widely available, but I obtained it here:

> https://online-fonts.com/fonts/univers-condensed

## Coding
I set up this project to code using Thonny/MicroPython. I think the Arduino approach might potentially work better, but I was already familiar with Thonny/MPy. I followed the setup guide in the dev board's wiki:

> https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-1.28

The walkthrough provides the tools needed to flash board, connect to it with Thonny, etc. Once you do all that, you would use Thonny to upload all of the files/subfolders in the "Program" folder onto the device. Then you would either run "DicePuck.py" from the device, or you would unplug/replug the device.

## Modeling a case
I have done quite a bit with OpenSCAD, so this came together rather well. It is just a hollow shell with a cutout for the screen. Then a plastic "shelf" in the middle that keeps the battery off of the circuit board. If you get a thicker/thinner battery, you'd need to modify the .scad file using the OpenSCAD program's Customizer. No code changes required.

Note: The little cutout notch in the "shelf" goes on the opposite side from the battery connector.

# Problems
I ran across a number of problems during this project, some of which I did not fully solve. If you intend to build this project, or use it as a launchpad for yo
- Battery polarity this board takes is reversed from what seems to be widely available
    - I was able to use tweezers to lift up the little plastic tabs on the battery connector, pull out the wires, and reverse them. It is very small and fiddly but wasn't too bad.
- Battery level indication not solved
    - I found out how to read voltage from the ADR pin for this dev board, but in the MicroPython I could not figure out how to translate it into a charge percentage. This is currently unsolved, but i left my semi-functional library in the 'sensorlib' folder.
- In the MicroPython examples provided in the wiki, they only show how to read either the gyro OR the touch screen, not both at the same time.
    - I was able to solve this issue though once I realized both communicate on the same pin set, so I need to set up the connection to that pin set only once and use it with both sensor types
- Touchscreen is not as intuitive or smooth as modern touchscreens
    - I have spent little or no time refining the code to make for a good user experience. Improvements can be made, but my goal was to deliver minimal functionality with the lowest battery usage I could manage.
- The boot file on the ESP board causes the device to always run, which makes it hard to write to
    - I am able to solve this by just trying to run code from my PC on the thonny which tends to overwrite the automatic boot. But if worse came to worse, I could upload a new boot.py that odesn't autorun any code

