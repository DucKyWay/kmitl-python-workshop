import tm1637

from machine import Pin
from time import sleep

tm = tm1637.TM1637(clk=Pin(5),dio=Pin(4))

tm.number(953)