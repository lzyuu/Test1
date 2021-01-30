# my serial

import sys
import os
import serial
import serial.tools.list_ports

class COM:

    def __init__(self):
        self.serial_search()

    def serial_open(self,port_name):
        self.serial.serial(port_name,9600,timeout = 0.5)

    def serial_search():
        port =  serial.tools.list_ports.comports()
        if len(port) <= 0:
            print(u"不能找到串口呀")

        else:
            print(u"找到可用串口: ",len(port))
            port_num = 0
            for port_num in range(0,len(port)):
                port_frist = list(port[port_num])
                port_firts_name = port_frist[0]

                print(port_firts_name)
                print(port_frist)


if __name__ == "__main__":
    x = COM
    # x.serial_search()
    # x.serial_open(input("你要打开几号呀"))
    
