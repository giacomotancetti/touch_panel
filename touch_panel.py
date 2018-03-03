import Leap, sys, thread, time, os
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import mtTkinter as Tkinter
from Tkinter import *
from PIL import Image, ImageTk

imm_num = 0
root = Tk()
#root.attributes("-fullscreen",True)

# canvas for image
canvas = Canvas(width=1368, height=768)
canvas.grid(row=0, column=0)

# image directories
path_1 = "01.jpg"
path_2 = "02.jpg"
path_3 = "03.jpg"
path_4 = "04.jpg"
path_5 = "05.jpg"

# image conversion
img_1 = ImageTk.PhotoImage(Image.open(path_1))
img_2 = ImageTk.PhotoImage(Image.open(path_2))
img_3 = ImageTk.PhotoImage(Image.open(path_3))
img_4 = ImageTk.PhotoImage(Image.open(path_4))
img_5 = ImageTk.PhotoImage(Image.open(path_5))

# images
my_images = []
my_images.append(img_1)
my_images.append(img_2)
my_images.append(img_3)
my_images.append(img_4)
my_images.append(img_5)

# set first image on canvas
image_on_canvas = canvas.create_image(0, 0, anchor = NW, image = my_images[4])

def change_image(imm_num):
  # change image
  canvas.itemconfig(image_on_canvas, image = my_images[imm_num-1])



class LeapMotionListener(Leap.Listener):
  finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
  bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
  state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
  
  def on_init(self, controller):
    print("Initialized")

  def on_connect(self, controller):
    print("Motion Sensor Connected")
    #controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
    #controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
    #controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
    #controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

  def on_disconnect(self, controller):
    print("Motion Sensor Disconnected")

  def on_exit(self, controller):
    print("Exited")

  def on_frame(self, controller):
    frame = controller.frame()
    interactionBox = frame.interaction_box
    if (frame.pointables.is_empty == True):
       self.position = Leap.Vector(0,0,0)
    elif (frame.pointables.is_empty == False):
         for pointable in frame.pointables:
             pointable = frame.pointables.frontmost
             self.position = pointable.tip_position    
    print(self.position)
    return self.position
   
  def image_select(self):
        if -92 < position.x < -50 and 325 < position.y < 386 and position.z < -90:  
           if imm_num != 1:
             imm_num = 1                   
        elif -50 < position.x < 75 and 225 < position.y < 370 and position.z < -85:
             if imm_num != 2:
              imm_num = 2                        
        elif 94 < position.x < 140 and 289 < position.y < 370 and position.z < -85:
             if imm_num != 3:
              imm_num = 3            
        elif -29 < position.x < 55 and 155 < position.y < 207 and position.z < -85:
             if imm_num != 4:
              imm_num = 4
        print(str(imm_num))
        return imm_num

def main():
    
    listener = LeapMotionListener()      # assegna l'oggetto "listener" alla classe "LeapMotionListener"
    controller = Leap.Controller()       # assegna l'oggetto "controller" alla classe "Leap.Controller"
    controller.add_listener(listener)    # invoca il metodo "add_listener()" sull'oggetto controller
    #listener.on_frame(controller)
    #print(listener.position)

    print("Press enter to quit")
    try:
      sys.stdin.readline()
    except KeyboardInterrupt:
      pass
    finally:
      controller.remove_listener(listener)

if __name__ == "__main__":
   main()
