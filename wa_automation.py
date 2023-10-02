# setup pywhatkit from github@ Ankit404butfound/PyWhatKit

import pywhatkit as pa
import pyautogui as pg
import time

print("Pragram in 5 seconds...")
time.sleep(5)

txt = open('animals.txt', 'r')
a = "happy Gandhi Jayanti from "
for i in txt:
    pg.write(a+' '+i)
    # Send a WhatsApp Message to a Contact at 2:53 PM
    # pa.sendwhatmsg("+919556760902", text , 14, 53)
    pg.press('Enter')  
    
    
 
 
 
 
   
# for i in range(100):
#     pg.write("I Love You")
#     time.sleep(0.5)
#     pg.press("Enter")
    
    
    
    
    
    
    
    
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)  
    
    
    
    
    
    
# pywhatkit.start_server()
# sendwhatmsg(phone_no: str,
#              message: str,
#              time_hour: int,
#              time_min: int,
#              wait_time: int = 20,
#              tab_close: bool = False,
#              close_time: int = 3)


# # Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+919776109078", "Hi", 13, 55)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")

# Converting image to ASCII Art
#   ascii_art = pywhatkit.image_to_ascii_art("image path")
#   print(ascii_art)

# Installation
# ------------
# python -m ensurepip --default-pip
# python3 -m pip install pywhatkit
# pip3 install pywhatkit
# git clone https://github.com/Ankit404butfound/PyWhatKit.git
# import pywhatkit
# pywhatkit.start_server()