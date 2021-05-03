# Loopback timing measure for Serial ports
# Richard Schrader - 05-02-21

import serial
import time
import serial.tools.list_ports
from msvcrt import getch
from sys import exit
from os import system

BAUD_RATE = 38400
TIME_OUT = 5

ser = serial.Serial()


def main():
    system('cls')

    ports = serial.tools.list_ports.comports()
    if not ports:
        sys.exit("Error: No serial ports available")

    print("Available Serial Ports Menu\n")

    for i in sorted(ports):
        (port, desc, hwid) = i
        try:
            check = serial.Serial(port)
            check.close()
            print(str(ports.index(i)+1) +
                  "- {}: {} [{}]".format(port, desc, hwid))
        except:
            pass

    print()

    while True:
        try:
            opt = int(input("Enter your choice (1-"+str(len(ports))+"): "))
            if opt in list(range(1, len(ports) + 1)):
                break
        except:
            pass

    ser.port = ports[opt - 1][0]
    ser.baudrate = BAUD_RATE
    ser.timeout = TIME_OUT
    ser.open()

    print("\nConnected to: " + ser.portstr)

    while True:
        start = time.perf_counter()
        tran = 'loop\n'
        print("\nTransmitting the string('loop\\n') at 38400bps@8N1...")
        ser.write(tran.encode('ascii'))
        recv = ser.readline().decode('utf-8')
        end = time.perf_counter()
        execution_time = (end - start)
        if recv == tran:
            print("\nReceived the string('loop\\n') in " +
                  str(execution_time)+" seconds")
        else:
            print("Serial comms timeout error")

        print("\nPress any key to repeat or Q to quit.")

        c = getch().decode("utf8")
        if c.lower() == 'q':
            break


if __name__ == '__main__':
    main()
