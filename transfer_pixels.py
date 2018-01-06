# transfer a shape pixel by pixel - by Sarah Samuelson
from microbit import *
import radio

radio.on()
while True:
    incoming = radio.receive()
    if incoming is not None:
        # split the incoming message into pixel info and convert to values 
        pix_x = int(float(incoming[0]))
        pix_y = int(float(incoming[1]))
        pix_b = int(float(incoming[2]))
        display.set_pixel(pix_x, pix_y, pix_b)
        sleep(100)

    if button_a.is_pressed():
        # display an image to transfer to another microbit
        display.show(Image.HEART)
        # create a loop for each of the rows on the microbit
        for y in range(0, 5):
            # create a loop for each pixel in the row
            for x in range(0, 5):
                # get the brightness of the pixel in the coord x, y
                brightness = display.get_pixel(x, y)
                # send the position and brightness of the pixel as a string
                msg = str(x)+str(y)+str(brightness)
                radio.send(msg)
                # turn the pixel off - set to 0
                display.set_pixel(x, y, 0)
                sleep(100)
