from click import command
import serial
import getch
serialport = serial.serial("/dev/tty50")
serial.port.baudrate=115200

while true : 
    s= getch.getch()
    if x == "q":
        break
    elif x== "w":
        command = "+100+10015+00"
    elif x== "s":
        command = "-100-10015+00"
    elif x=="d":
        command = "+100-10015+00"
    elif x=="a":
        command = "-100+10015+00"
    elif x=="x":
        command = "+000+00015+00" 
serial.port.write(command.encode())
