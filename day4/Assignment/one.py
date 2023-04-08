import tm1637

from machine import Pin
from time import sleep

tm = tm1637.TM1637(clk=Pin(5),dio=Pin(4))

tm.number(3)
sleep(3)
tm.number(0)
sleep(1)
tm.number(1)
sleep(1)
tm.number(2)
sleep(1)
tm.number(3)
sleep(1)
tm.number(4)
sleep(1)
tm.number(5)
sleep(1)
tm.number(6)
sleep(1)
tm.number(7)
sleep(1)
tm.number(8)
sleep(1)
tm.number(9)