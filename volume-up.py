#!/usr/bin/env python3

from gpiozero import Button
from time import sleep

import os
button = Button(26)
while True:
    button.wait_for_press()
    os.system("amixer -q -M sset PCM 1%+")
    sleep(0.2)