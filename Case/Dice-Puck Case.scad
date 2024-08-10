/////////////////////////////
// Parameters
/////////////////////////////

//Which part to print
Part = "All"; //[All,Face,Back,Spacer]
//Thickness of battery
Battery_Thickness = 4.3;
//Extra spacing needed around threads to allow for parts to fit together
Thread_Tollerance = 0.2;
//Extra spacing needed around spacer to allow it to fit in the face
Spacer_Tolerance = 0.2;

module endParams(){}endParams();





/////////////////////////////
// Back-end parameters
/////////////////////////////

$fn = 128;
eps = 0.007;

//thread twists
threadTwists = 0.75;

//Measurements of display screen and its frame
//display is the screen
display_diameter = 35.7;
displayFrame_diameter = 39; //38.6
displayFrame_thickness = 1;
//Nub is the extra bit that sticks out towards USB on the frame
displayNub_x_widest = 25.3;
displayNub_x_widest_rot45 = displayNub_x_widest * sin(45);
displayNub_y_from0 = findTSide(t="b", a=(displayNub_x_widest/2), c=(displayFrame_diameter/2));
displayNub_y_cutoff = displayNub_y_from0 + 7.48;
//faceWall is the walls around the face and circuit board
wallThickness = 6.87/2; // there is prob math for this but its HARD so eff it
faceWall_diameter = displayFrame_diameter + wallThickness*2;
faceWall_depth = 10;
//Wall behind threads
threadWall = 1;
threadHeight = Battery_Thickness;
thread_inner = displayFrame_diameter/2+threadWall;
thread_outer = faceWall_diameter/2-threadWall;

//Measurements for the back piece
back_diameter = faceWall_diameter;
back_thickness = 1;
back_threadHeight = threadHeight;
back_thread_offset = Thread_Tollerance;
back_thread_outer = back_diameter/2-threadWall+back_thread_offset;
back_thread_inner = back_thread_outer - (thread_outer-thread_inner);

//Measurements for the spacer
//This goes in the case between the device and the battery
spacer_thickness = 1;
spacer_diameter = displayFrame_diameter - Spacer_Tolerance;
spacer_height = 4; //may need to be +4?
spacer_width = 2;





/////////////////////////////
// Logic - what gets made
/////////////////////////////

if (Part=="Face"){
    part_face();
}
else if (Part=="Back"){
    part_back();
}
else if (Part=="Spacer"){
    part_spacer();
}
else if (Part=="All"){
    translate([-faceWall_diameter - 5,0,0])
    part_face();
    translate([faceWall_diameter + 5,0,0])
    part_back();
    part_spacer();
}





/////////////////////////////
// Parts - elements of models
/////////////////////////////

//Inner face 2d shape, without a display cutout
module part_2d_face_inner(){
    difference(){
        union(){
            //circle
            circle(d=displayFrame_diameter);
            //Nub
            translate([0,-displayNub_y_from0,0])
            rotate([0,0,45])
            square(displayNub_x_widest_rot45,center=true);
        }
        //cutoff for end of nub
        translate([0,-displayNub_y_cutoff-(displayFrame_diameter/2),0])
        square(displayFrame_diameter, center=true);
    }
}

//Outer face 2d shape, without a display cutout
module part_2d_face_outer(){
    difference(){
        difference(){
            //wall area
            circle(d=faceWall_diameter);
            //center cutout
            part_2d_face_inner();
            //End cutoff at nub
            translate([0,-displayNub_y_cutoff-(displayFrame_diameter/2)+eps,0])
            square(displayFrame_diameter, center=true);
        }
    }
}

//Create the face of the case
module part_face(){
    union(){
        //inner area of the face
        linear_extrude(displayFrame_thickness)
        difference(){
            //face
            part_2d_face_inner();
            //display cutout
            circle(d=display_diameter);
        }

        //outer wall of the face
        linear_extrude(faceWall_depth)
        part_2d_face_outer();
        
        //wall in front of usb
        part_face_usbWall();
        
        //threads
        part_face_threads();
    }
}

//Creates little wall in front of USB on the face
module part_face_usbWall(){
    linear_extrude(faceWall_depth-5)
    intersection(){
        //wall
        translate([0,1/2 - displayNub_y_cutoff,0])
        square([15,1],center=true);
        //cylinder
        circle(d=faceWall_diameter);
    }
}

// Threaded part of the face
module part_face_threads(){
    translate([0,0,faceWall_depth])
    difference(){
        //Threads
        difference(){
            //thread
            printableThread(
                r_int=thread_inner,
                r_ext=thread_outer,
                h=threadHeight,
                twist=-threadTwists,
                tc=2
            );
            //chamfer
            threadChamfer(
                r_int=thread_inner,
                h=threadHeight,
                size=2,
                angle=45,
                edge="top",
                type="subtract"
            );
        }
        //Cutout for middle
        translate([0,0,-eps/2])
        cylinder(d=displayFrame_diameter, h=threadHeight+eps);
        //Cutout for usb nub
        translate([0,0,-eps/2])
        linear_extrude(threadHeight+eps)
        part_2d_face_inner();
        //Cutout for the pointy thread remainder bits
        translate([0,0,-eps/2])
        rotate([0,0,-90-(55/2)])
        rotate_extrude(angle=55)
        translate([displayNub_y_cutoff-threadHeight,0,0])
        square(threadHeight+eps);
    }
}

//Create back part of model
module part_back(){
    difference(){
        //back and walls
        linear_extrude(back_thickness+back_threadHeight)
        circle(d=back_diameter);
        //thread cutout
        translate([0,0,back_thickness+eps]){
            printableThread(
                r_int=back_thread_inner,
                r_ext=back_thread_outer,
                h=back_threadHeight,
                twist=-threadTwists,
                tc=2
            );
            //thread chamfer cutout
            threadChamfer(
                r_int=back_thread_inner,
                h=back_threadHeight,
                size=2,
                angle=45,
                edge="top",
                type="add"
            );
        }
        
    }
}

//Create a peg for the spacer
//A is the # of degrees (out of 360) that the peg's arc takes
//r is the amount of z rotation used to position it around the spacer
module part_spacer_peg(a,r){
    rotate([0,0,r])
    rotate_extrude(angle=a)
    translate([spacer_diameter/2-spacer_width,0,0])
    square([spacer_width,spacer_height]);
}

// Create spacer
module part_spacer(){
    //translate([0,0,10])
    //rotate([0,180,0])
    translate([0,0,spacer_thickness])
    difference(){
        //Spacer
        union(){
            //Plate
            translate([0,0,-spacer_thickness])
            linear_extrude(spacer_thickness)
            circle(d=spacer_diameter);
            //Pegs start with the big one opposite of the USB and go clockwise
            part_spacer_peg(60,60);
            part_spacer_peg(20,145);
            part_spacer_peg(20,198);
            part_spacer_peg(20,198);
            part_spacer_peg(10,245);
            part_spacer_peg(7,304);
            part_spacer_peg(10,337);
            part_spacer_peg(10,376);
        }
        //Notch cutout for power cord
        translate([spacer_diameter/2,0,0])
        cube(5,center=true);
    }
    *
    color([0.6,0.6,0.6])
    translate([0,0,-7])
    rotate([0,180,0])
    import("ESP32-S3-Touch-LCD-1_28.stl");
}





/////////////////////////////
// Helpers - extra libraries and functions
/////////////////////////////

//Find the requested side given either 2 sides or 1 side + 1 angle
//Only works for right triangles
//t must be "a", "b", or "c"
//This is a new func I made for this project because I was tied of dealing with triangle math
//Haven't tested all the variations
function findTSide(t,a=0,b=0,c=0,A=0, B=0) =
    //2 legs known
    a!=0 && b!=0 ? (
        t=="c" ? sqrt(pow(a,2)+pow(b,2)) :
        undef
    ):
    //1 leg (a) and hypotenuse known
    a!=0 && c!=0 ? (
        t=="b" ? sqrt(pow(c,2)-pow(a,2)) :
        undef
    ):
    //1 leg (b) and hypotenuse known
    b!=0 && c!=0 ? (
        t=="a" ? sqrt(pow(c,2)-pow(a,2)) :
        undef
    ):
    //1 leg (a) and opposite angle known
    a!=0 && A!=0 ? (
        t=="b" ? a * tan(90-A) :
        t=="c" ? sqrt(pow(a,2)+pow(a*tan(90-A),2)) :
        undef
    ):
    //1 leg (b) and opposite angle known
    b!=0 && B!=0 ? (
        t=="a" ? b * tan(90-B) :
        t=="c" ? sqrt(pow(b,2)+pow(b*tan(90-B),2)) :
        undef
    ):
    //1 leg (a) and adjacent angle known
    a!=0 && B!=0 ? (
        t=="b" ? a * tan(B):
        t=="c" ? sqrt(pow(a,2)+pow(a*tan(B),2)):
        undef
    ):
    //1 leg (b) and adjacent angle known
    b!=0 && A!=0 ? (
        t=="a" ? b * tan(A):
        t=="c" ? sqrt(pow(b,2)+pow(b*tan(A),2)):
        undef
    ):
    //None found
    undef;
        




///////////////////////////////////////////////////////////
//              Simple Printable Threads
//            Created by MrStump, Aug 2023
///////////////////////////////////////////////////////////
/*
Instructions for use:
    - Copy all of this code (not including the example at the top) into your script
        - You can alternatively use this as a library using the "use" command
    - Use the "printableThread" function to create a threaded shape
    - Optionally, you can use "threadChamfer" to spawn a shape to create chamfers
    
Notes on printability:
    ~45 degrees is the steepest overhang you want on a model if you want to print with no supports. When making a thread, look at it from the side and make sure you aren't making an angle too steep. If you are, try less threads, less twist/angle, or less difference between your interior and exterior radius.

Notes on tolerance:
    In the example you can see tolerance added to the "socket". Without it, the "perfect fit" would never go together once printed. 0.25-0.5 differnece in the radius measurements between the "socket" and the "screw" is a good general range, but your printer, printer settings, material and more all impact the fit. A test print is always a good idea to find a measurement that works for you.
*/



// Creates a printable thread shape
//         ----REQUIRED PARAMETERS----
// r_int = Distance from point where threads are closest to center
// r_ext = Distance from point where threads are furthest from center
// h     = Height of the threaded shape (overall screw length)
//         ----MUST USE ONE PARAMERS FROM THESE 2----
// twist = Number of 360 twists across the entire length (turns). Negative numbers are "righty tighty"
// angle = Angle of threads. Negative numbers are "righty tighty".
//         ----OPTIONAL PARAMETERS----
// tc    = Number of threads. Even number recommended.
// dpc   = Dots per circumfrance, how many dots make up the shape
// $fn   = Level of detail (default recommended, or use 32 for better performance)
//
// EXAMPLE:
// printableThread(r_int=40, r_ext=45, twist=-1.5, h=100, tc=6);
module printableThread(r_int, r_ext, h, twist=0, angle=0, tc=2, dpc=100, $fn=64){
    if (twist==0 && angle==0){
        //Makes no screw due to no twist or angle
        echo("\n\n    ATTENTION:\nYou did not set a 'twist' or 'angle' param in printableThread. You must set one.\n\n");
    } else if (twist!=0 && angle!=0){
        //Makes no screw due to both twist and angle being selected
        echo("\n\n    ATTENTION:\nYou set both 'twist' and 'angle' params in printableThread. You must set only one.\n\n");
    } else {
        //Makes screw
        
        //Determine twist count by twist or angle param
        desiredTwist = twist!=0 ? twist : twistFromAngle(r_ext,h,angle);
        
        //Calcualte twist
        degreesToTwist = 360 * desiredTwist;
        
        // Generate threaded shape
        linear_extrude(h, twist=degreesToTwist, $fn=$fn)
            thread2dShape(r_int, r_ext, tc, dpc);
    }
}


// Creates a chamfer to make mating threaded bits easier
//         ----REQUIRED PARAMETERS----
// r_int = Distance from point where threads are closest to center
// h     = Height of the threaded shape (overall screw length)
// size  = How much chamfering to do
//         ----OPTIONAL PARAMETERS----
// angle = Angle of the chamfer (between 0 and 90. Overhangs > 45 may not print without support)
// edge  = "top" or "bottom", for what edge of the screw chamfer aligns to
// type  = "add" or "subtract", for if the chamfer removes from the screw or adds to it
//          - "add" is for when you need to create a threaded socket in another shape
// $fn   = Level of detail (default recommended, or use 32 for better performance)
//
// EXAMPLE:
// threadChamfer(r_int=40, h=100, size=5);
module threadChamfer(r_int, h, size, angle=45, edge="top", type="subtract", $fn=64){
    //Epsilon, used to ensure the difference cleanly cuts paralell surfaces
    eps = 0.007;
    //Extra X added to the chamfer size if subtracting. Lets low poly meshes not clip through
    sizePlus = type=="subtract" ? size*1.2 : size;
    
    // Create a list of 3 different x/y/z coords for shape creation and position
    // index 0 = translate that changes z
    // index 1 = translate that changes x pos for rotate_extrude
    // index 2 = rotation applied to triangle prior to rotate_extrude
    extrudeAndTranslateData = 
        edge=="bottom" && type=="add" ?
            [ [0,0,0], [r_int,0,0], [0,0,0] ] :
        edge=="top" && type=="add" ?
            [ [0,0,h], [r_int,0,0], [180,0,0] ] :
        edge=="bottom" && type=="subtract" ?
            [ [0,0,-eps], [-(r_int+sizePlus),0,0], [0,0,0] ] :
        edge=="top" && type=="subtract" ?
            [ [0,0,h+eps], [-(r_int+sizePlus),0,0], [180,0,0] ] : 
        "If you get error in below translate, it is cause of this";
    
    // Create/position shape
    translate(extrudeAndTranslateData[0])
        rotate_extrude()
        translate(extrudeAndTranslateData[1])
        rotate(extrudeAndTranslateData[2])
        //polygon([[0,0],[0,sin(angle)*size],[cos(angle)*size,0]]);
        polygon([[0,0],[0,sizePlus*tan(angle)],[sizePlus,0]]);
}

// Creates the shape which is extrusion twisted to make threads
//         ----REQUIRED PARAMETERS----
// r_int = Distance from point where threads are closest to center
// r_ext = Distance from point where threads are furthest from center
//         ----OPTIONAL PARAMETERS----
// tc    = Number of threads. Even number recommended. Negative #s are "righty tighty"
// dpc   = Dots per circumfrance, how many dots make up the shape
//
// EXAMPLE:
// thread2dShape(30, 35, tc=6);
module thread2dShape(r_int, r_ext, tc=2, dpc=200){
    //How much threads stick out
    threadLength = r_ext-r_int;
    //Midpoint between the 2 radius measurements
    r_mid = r_int + (threadLength/2);
    //The size of each "step" making the shape
    interval = 1/dpc;
    
    //Generate list of [X,Y] coords, each acting as a point to make the shape
    pl = [
        for (i=[0:interval:1-interval])[
            (r_mid + (threadLength/2) * sin(tc * i * 360)) * cos(i * 360),
            (r_mid + (threadLength/2) * sin(tc * i * 360)) * sin(i * 360)
        ]
    ];
    
    //Generate the 2d shape from the list of points
    polygon(points=pl);
}

//Helper function: get twist based on radius, height (length), and desired angle
function twistFromAngle(_r,_h,_a) = _h / ( (2*PI*_r) * tan(_a) );















