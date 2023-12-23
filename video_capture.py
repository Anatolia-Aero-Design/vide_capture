import cv2 as cv
import math
import time
import numpy as np

"""
cap = cv.VideoCapture(0)

# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# MACOS AND LINUX: *'XVID' (MacOS users may want to try VIDX as well just in case)
# WINDOWS *'VIDX'
writer = cv2.VideoWriter('student_capture.mp4', cv2.VideoWriter_fourcc(*'VIDX'),25, (width, height))

## You may want to instead use some sort of timer, like from time import sleep and then just record for 5 seconds.

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Write the video
    writer.write(frame)

    # Display the resulting frame
    cv.imshow('frame',frame)
    
    # This command let's us quit with the "esc" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv.waitKey(1) & 0xFF == 27:
        break

        
cap.release()
writer.release()
cv.destroyAllWindows()
"""

"""
cap = cv.VideoCapture('student_capture.mp4')

# FRAMES PER SECOND FOR VIDEO
fps = 25

# Always a good idea to check if the video was acutally there
# If you get an error at this step, triple check your file path!!
if cap.isOpened()== False: 
    print("Error opening the video file. Please double check your file path for typos" 
          "Or move the movie file to the same location as this script/notebook")
    

# While the video is opened
while cap.isOpened():
    
    # Read the video file.
    ret, frame = cap.read()
    
    # If we got frames, show them.
    if ret == True:
        
        # Display the frame at same frame rate of recording
        time.sleep(1/fps)
        cv.imshow('frame',frame)
 
        # Press esc to quit
        if cv.waitKey(25) & 0xFF == 27:
            
            break
    # Or automatically break this whole loop if the video is over.
    else:
        break
        
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
"""


# Create a function based on a CV2 Event (Left button click)

# mouse callback function
def draw_rectangle(event,x,y,flags,param):

    global pt1,pt2,topLeft_clicked,botRight_clicked

    # get mouse click
    if event == cv.EVENT_LBUTTONDOWN:

        if topLeft_clicked == True and botRight_clicked == True:
            topLeft_clicked = False
            botRight_clicked = False
            pt1 = (0,0)
            pt2 = (0,0)

        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
            
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True

        
# Haven't drawn anything yet!

pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

cap = cv.VideoCapture(0) 

# Create a named window for connections
cv.namedWindow('Test')

# Bind draw_rectangle function to mouse cliks
cv.setMouseCallback('Test', draw_rectangle) 


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if topLeft_clicked:
        cv.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
        
    #drawing rectangle
    if topLeft_clicked and botRight_clicked:
        cv.rectangle(frame, pt1, pt2, (0, 0, 255), 2)
        
    # Display the resulting frame
    cv.imshow('Test', frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()

# Create a function based on a CV2 Event (Left button click)
"""
# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked,pt

    # get mouse click on down and track center
    if event == cv.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False
    
    # Use boolean variable to track if the mouse has been released
    if event == cv.EVENT_LBUTTONUP:
        pt = (x, y)
        clicked = True

# Haven't drawn anything yet!
center = (0,0)
pt = (0,0)
clicked = False

cap = cv.VideoCapture(0) 

# Create a named window for connections
cv.namedWindow('Test')

# Bind draw_rectangle function to mouse cliks
cv.setMouseCallback('Test', draw_circle) 

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use if statement to see if clicked is true
    if clicked == True:
        # Draw circle on frame
        cv.circle(frame, center, radius=int(math.dist(center,pt)), color=(0,0,255), thickness=5)
        
    # Display the resulting frame
    cv.imshow('Test', frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
"""