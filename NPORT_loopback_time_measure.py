# Loopback timing measure for NPORT Ethernet to Serial converter
# Note: Set the NPORT for TCP-Server and check if the IP address and port number are correct in the code.
# Turn off your Firewall if necessary.
# Richard Schrader - 05-02-21


import serial
import time
from msvcrt import getch


def main():

    with serial.serial_for_url("socket://192.168.127.254:4001") as ser:
        ser.timeout = 5
        ser.baudrate = 38400

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
