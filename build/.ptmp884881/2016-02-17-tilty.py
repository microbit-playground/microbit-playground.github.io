<script type="text/javascript" src="bundled.min.js"></script>
# A simple MicroBit game by Giles Booth
<script type="text/javascript" src="bundled.min.js"></script>
# Tilt and colour in all the squares
<script type="text/javascript" src="bundled.min.js"></script>
# If you win level 20, press reset button to play again
<script type="text/javascript" src="bundled.min.js"></script>
#
<script type="text/javascript" src="bundled.min.js"></script>
# MIT License (c) 2016 Giles Booth

<script type="text/javascript" src="bundled.min.js"></script>
from microbit import display, accelerometer, sleep, Image
<script type="text/javascript" src="bundled.min.js"></script>
from music import play, POWER_UP, NYAN

<script type="text/javascript" src="bundled.min.js"></script>
def get_xy():
<script type="text/javascript" src="bundled.min.js"></script>
    yaccel = accelerometer.get_y() * accelerometer_sensitivity
<script type="text/javascript" src="bundled.min.js"></script>
    xaccel = accelerometer.get_x() * accelerometer_sensitivity
<script type="text/javascript" src="bundled.min.js"></script>
    return yaccel, xaccel

<script type="text/javascript" src="bundled.min.js"></script>
def count_lit_pixels():
<script type="text/javascript" src="bundled.min.js"></script>
    pixel_count = 0
<script type="text/javascript" src="bundled.min.js"></script>
    for xx in range (5):
<script type="text/javascript" src="bundled.min.js"></script>
        for yy in range (5):
<script type="text/javascript" src="bundled.min.js"></script>
            if display.get_pixel(xx, yy) != 0:
<script type="text/javascript" src="bundled.min.js"></script>
                pixel_count += 1
<script type="text/javascript" src="bundled.min.js"></script>
    return pixel_count

<script type="text/javascript" src="bundled.min.js"></script>
pause = 100
<script type="text/javascript" src="bundled.min.js"></script>
level = 0
<script type="text/javascript" src="bundled.min.js"></script>
accelerometer_sensitivity=1/300

<script type="text/javascript" src="bundled.min.js"></script>
#set initial position
<script type="text/javascript" src="bundled.min.js"></script>
x, y = 2, 2
<script type="text/javascript" src="bundled.min.js"></script>
yaccel, xaccel = get_xy()
<script type="text/javascript" src="bundled.min.js"></script>
y = max(0, min(4, int(y + yaccel)))
<script type="text/javascript" src="bundled.min.js"></script>
x = max(0, min(4, int(x + xaccel)))

<script type="text/javascript" src="bundled.min.js"></script>
while pause > 0:
<script type="text/javascript" src="bundled.min.js"></script>
    yaccel, xaccel = get_xy()
<script type="text/javascript" src="bundled.min.js"></script>
    newy = max(0, min(4, int(y + yaccel)))
<script type="text/javascript" src="bundled.min.js"></script>
    newx = max(0, min(4, int(x + xaccel)))
<script type="text/javascript" src="bundled.min.js"></script>
    if newy != y or newx != x:
<script type="text/javascript" src="bundled.min.js"></script>
        display.set_pixel(x, y, 1)
<script type="text/javascript" src="bundled.min.js"></script>
        x, y = newx, newy
<script type="text/javascript" src="bundled.min.js"></script>
        display.set_pixel(x, y, 9)
<script type="text/javascript" src="bundled.min.js"></script>
    else:
<script type="text/javascript" src="bundled.min.js"></script>
        display.set_pixel(newx, newy, 9)
<script type="text/javascript" src="bundled.min.js"></script>
    pixels = count_lit_pixels()
<script type="text/javascript" src="bundled.min.js"></script>
    if pixels == 25:
<script type="text/javascript" src="bundled.min.js"></script>
        play(POWER_UP, wait=False)
<script type="text/javascript" src="bundled.min.js"></script>
        level += 1
<script type="text/javascript" src="bundled.min.js"></script>
        pause -= 5
<script type="text/javascript" src="bundled.min.js"></script>
        sleep(200)
<script type="text/javascript" src="bundled.min.js"></script>
        display.show(str(level))
<script type="text/javascript" src="bundled.min.js"></script>
        sleep(1000)
<script type="text/javascript" src="bundled.min.js"></script>
        display.clear()
<script type="text/javascript" src="bundled.min.js"></script>
    sleep(pause)

<script type="text/javascript" src="bundled.min.js"></script>
play(NYAN, wait=False)
<script type="text/javascript" src="bundled.min.js"></script>
display.show('WIN!')
<script type="text/javascript" src="bundled.min.js"></script>
sleep(200)
<script type="text/javascript" src="bundled.min.js"></script>
display.show(Image.HEART)
