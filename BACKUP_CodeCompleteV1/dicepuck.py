from random import randint # Random numbers
from machine import Pin, SoftI2C, SPI # ESP board
from sensorlib import cst816, qmi8658 # touch and spacial sensors
import gc9a01 # Display
import time # sleep
from data import dice # info about dice
# Fonts
from truetype import UniversCondensed_32 as uni_32
from truetype import UniversCondensed_48 as uni_48
from truetype import UniversCondensed_64 as uni_64



################################
# Global variables
################################
# Colors for UI (rgb 255)
c = {
    "primary": gc9a01.color565(255,255,255),
    "emphasis": gc9a01.color565(255,255,0),
    "background" : gc9a01.color565(0,0,0),
    "good roll": gc9a01.color565(0,255,0),
    "bad roll": gc9a01.color565(255,0,0)
}
# Distance travel to trigger a swipe action
swipeSensitivity = 40
# How hard any axis needs to be shaken to trigger a shake action
shakeSensitivity = 100 #400
# Current stage. "rollSetup", "rollResult"
stage = "rollSetup" #"rollSetup"
# Set up common bus for sensors
sensorBus = SoftI2C(scl=Pin(7),sda=Pin(6),freq=100000)
# Establish connections to hardware elements
display = gc9a01.GC9A01( #screen
    SPI(2, baudrate=80000000, polarity=0, sck=Pin(10), mosi=Pin(11)),
    240,
    240,
    reset=Pin(14, Pin.OUT),
    cs=Pin(9, Pin.OUT),
    dc=Pin(8, Pin.OUT),
    backlight=Pin(2, Pin.OUT),
    rotation=0)
display.init()
spacial = qmi8658.QMI8658(sensorBus) #gyro/accel
touch = cst816.CST816(sensorBus) #touchscreen



################################
# Main function
################################
   
def main():
    # Primary loop, runs as long as device is on
    while True:
        # Each "stage" is a screen the user interacts with
        # Select die and die count
        if stage=="rollSetup":
            stage_rollSetup()
        # Show results of roll
        if stage=="rollResult":
            stage_rollResult()

#display.sleep_mode(True)
#display.off()










################################
# Stage functions (each is a different "screen" of the dice puck
################################     
        
def stage_rollSetup():
    """Draw and run the roll setup screen"""
    # Draw initial screen
    draw_rollSetup_all()
    #Used to track if a gesture is made by the user, only 1 gesture can be made per press
    gestureFlag = False 
    # Used to detect how many frames the screen has been pressed (used to skip first screen and long press)
    i_press = 0
    
    while True:
        time.sleep(0.05)
        
        # Collect gyro data
        xyz = [abs(i) for i in spacial.Read_XYZ()] # absolute values (no negatives)
        
        # Collect touchscreen data
        #touch = cst816.CST816()
        #point = touch.get_point()
        press = touch.get_touch()
        distance = touch.get_distance()
        
        # Count frames where button is pressed
        # Also causes the first frame to be skipped
        # This is to avoid a bug where "distance" isn't reset from the last press yet
        if press:
            i_press += 1
        elif i_press is not 0:
            i_press = 0
        if i_press == 1:
            continue

        # Reset gesture flag if it isn't already
        if not press and gestureFlag:
            gestureFlag = False
        # If a gesture hasn't been captured yet, check for one
        elif not gestureFlag:
            # Long press
            if i_press >= 1.5 / 0.05:
                #print("Long press", i_press)
                dice.data[dice.i]["count"] = 1
                draw_rollSetup_text()
                gestureFlag = True
            # Swipe right
            if distance.x_dist >= swipeSensitivity:
                #print("Swipe Right", distance.x_dist)
                dice.i = wrapDiceIndex(dice.i - 1)
                draw_rollSetup_all()
                gestureFlag = True
            # Swipe left
            elif distance.x_dist <= -swipeSensitivity:
                #print("Swipe Left", distance.x_dist)
                dice.i = wrapDiceIndex(dice.i + 1)
                draw_rollSetup_all()
                gestureFlag = True
            # Swipe down
            elif distance.y_dist >= swipeSensitivity:
                #print("Swipe Down", distance.y_dist)
                dice.data[dice.i]["count"] += 1
                draw_rollSetup_text()
                gestureFlag = True
            # Swipe up
            elif distance.y_dist <= -swipeSensitivity:
                #print("Swipe Up", distance.y_dist)
                dice.data[dice.i]["count"] -= 1
                if dice.data[dice.i]["count"] < 1:
                    dice.data[dice.i]["count"] = 1
                draw_rollSetup_text()
                gestureFlag = True
        
        # Shake detection
        # Shaking initiates a roll, so this breaks out of rollSetup
        if press and (xyz[3] > shakeSensitivity or xyz[4] > shakeSensitivity or xyz[5] > shakeSensitivity):
            global stage
            stage = "rollResult"
            break


def stage_rollResult():
    """Draw and run the roll results screen"""
    # clear screen
    display.fill(c["background"])
    # Draw background for total result
    display.fill_rect( # rectagle covers up previous text drawn
        0,
        239-69,
        239,
        69,
        c["primary"]
    )
    
    # Get roll results
    rollResults = getRollResults()
    
    # <= 14 rolls made
    if len(rollResults) <= 14:
        # Get positions for placing the numbers (up to 14)    
        resultPositionList = getResultPositionList()
        # Draw individual roll results (up to 14)
        for i, result in enumerate(rollResults):
            if result == 1:
                textColor = c["bad roll"]
            elif result == dice.data[dice.i]["sides"]:
                textColor = c["good roll"]
            else:
                textColor = c["primary"]
            pos = resultPositionList[i]
            pos["x"] = int(pos["x"] - display.write_len(uni_32, str(result))/2) #center & make int
            display.write(uni_32, str(result), pos["x"], pos["y"], textColor, c["background"])
            time.sleep(0.1) #draw them more slowly for effect
    # > 14 rolls made
    else:
        x_start = 20
        y_start = 20 + 32 + 5
        x_max = 200
        y_max = 32*4 + 5*2
        # Draw roll results
        for result in rollResults:
            if result == 1:
                textColor = c["bad roll"]
            elif result == dice.data[dice.i]["sides"]:
                textColor = c["good roll"]
            else:
                textColor = c["primary"]
            display.write(uni_32, str(result), randint(x_start,x_max), randint(y_start,y_max), textColor, c["background"])
            time.sleep(0.1) #draw them more slowly for effect
    # Draw total
    total = str(sum(rollResults))
    display.write(
        uni_64,
        total,
        int(display.width()/2 - display.write_len(uni_64, total)/2), #center x
        239-64,
        c["background"],
        c["primary"]
    )
    
    #After results are displayed, wait for long press to shut down
    i_press = 0
    while True:
        press = touch.get_touch()
        if press:
            i_press += 1
            if i_press >= 1.5 / 0.05:
                #print("Long press", i_press)
                global stage
                stage = "rollSetup"
                break
        elif i_press is not 0:
            i_press = 0
        time.sleep(0.05)

    
    
   
        



################################
# Helper functions
################################

def draw_rollSetup_all():
    """Draw the roll setup screen image, then trigger the text redraw"""
    # Currently selected die's info
    die = dice.data[dice.i]
    # Clear screen
    display.fill(c["background"])
    # Draw die
    display.jpg(
        die["img"],
        int(display.width()/2 - 128/2), #128 is image dimension
        int(display.height()/2 - 128/2),
        gc9a01.FAST)
    # Redraw text
    draw_rollSetup_text()
    
    
# Redraw the text around the die image
def draw_rollSetup_text():
    """Redraw the text for the roll setup screen"""
    # Currently selected die's info
    die = dice.data[dice.i]
    
    # Text below image
    display.fill_rect( # rectagle covers up previous text drawn
        1,
        int(display.height()/2 + 128/2 + 8),
        238,
        40,
        c["background"]
    )
    text = die["name"]
    font = uni_48
    x = int(display.width()/2 - display.write_len(font, text)/2)
    y = int(display.height()/2 + 128/2 + 8)
    display.write(uni_48, text, x, y, c["primary"], c["background"]) 
    # Text above image
    display.fill_rect( # rectagle covers up previous text drawn
        1,
        1,
        238,
        46,
        c["background"]
    )
    text = str(die["count"])
    x = int(display.width()/2 - display.write_len(uni_48, text)/2)
    y = int(display.height()/2 - 128/2 - 48)
    display.write(uni_48, text, x, y, c["primary"], c["background"])


# Get the next index number for dice object, wrapping around to beginning/end if needed
def wrapDiceIndex(i):
    """Wrap the index # for dice.data's array so it loops if it goes over or under min/max index
    
    Arguments:
    i = index number to wrap (if needed)
    """
    length = len(dice.data)
    if i > length-1:
        return 0
    elif i < 0:
        return length-1
    else:
        return i


def getRollResults():
    """Returns an array of roll results (as ints)"""
    howManyRolls = dice.data[dice.i]["count"]
    dieSides = dice.data[dice.i]["sides"]
    # Collect rolls into array
    rollResults = []
    for _ in range(howManyRolls):
        rollResults.append(randint(1, dieSides))
    # Return array of ints    
    return rollResults

def getResultPositionList():
    """Returns an array of x/y coordinate objects for up to 14 positions
       The X is centered on the number since number length varries"""
    x_start = 22 #offset from edge
    y_start = 20
    x_number = 45 #max width of a number
    y_number = 32 #max height of a number
    x_space = 5 #space between columns
    y_space = 5 #space between rows
    
    # It is possible to make a math formula to do this in a loop
    # But it would be such a mess that I decided not to
    orderedList = [
        {
            "x": x_start + x_number*1 + x_space*1 + x_number/2,
            "y": y_start + y_number*0 + y_space*0
        },
        {
            "x": x_start + x_number*2 + x_space*2 + x_number/2,
            "y": y_start + y_number*0 + y_space*0
        },
        {
            "x": x_start + x_number*0 + x_space*0 + x_number/2,
            "y": y_start + y_number*1 + y_space*1
        },
        {
            "x": x_start + x_number*1 + x_space*1 + x_number/2,
            "y": y_start + y_number*1 + y_space*1
        },
        {
            "x": x_start + x_number*2 + x_space*2 + x_number/2,
            "y": y_start + y_number*1 + y_space*1
        },
        {
            "x": x_start + x_number*3 + x_space*3 + x_number/2,
            "y": y_start + y_number*1 + y_space*1
        },
        {
            "x": x_start + x_number*0 + x_space*0 + x_number/2,
            "y": y_start + y_number*2 + y_space*2
        },
        {
            "x": x_start + x_number*1 + x_space*1 + x_number/2,
            "y": y_start + y_number*2 + y_space*2
        },
        {
            "x": x_start + x_number*2 + x_space*2 + x_number/2,
            "y": y_start + y_number*2 + y_space*2
        },
        {
            "x": x_start + x_number*3 + x_space*3 + x_number/2,
            "y": y_start + y_number*2 + y_space*2
        },
        {
            "x": x_start + x_number*0 + x_space*0 + x_number/2,
            "y": y_start + y_number*3 + y_space*3
        },
        {
            "x": x_start + x_number*1 + x_space*1 + x_number/2,
            "y": y_start + y_number*3 + y_space*3
        },
        {
            "x": x_start + x_number*2 + x_space*2 + x_number/2,
            "y": y_start + y_number*3 + y_space*3
        },
        {
            "x": x_start + x_number*3 + x_space*3 + x_number/2,
            "y": y_start + y_number*3 + y_space*3
        }
    ]
    return [
        orderedList[3],
        orderedList[4],
        orderedList[7],
        orderedList[8],
        orderedList[11],
        orderedList[12],
        orderedList[2],
        orderedList[5],
        orderedList[6],
        orderedList[9],
        orderedList[10],
        orderedList[13],
        orderedList[0],
        orderedList[1]
    ]
    
    










main()