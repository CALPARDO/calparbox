import lcdlibrary
from time import *

mylcd = lcdlibrary.lcd()

mylcd.lcd_display_string("Hello World!", 1, 1)