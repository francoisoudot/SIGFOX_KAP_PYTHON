import serial
import time

# SIGFOX device serial device
SIGFOX_DEVICE = "/dev/cu.usbserial-AH02DTED"
# SIGFOX device baud rate
SIGFOX_DEV_BR = 9600
# SIGFOX device byte size (5 to 8)
SIGFOX_DEV_BS = 8
# SIGFOX device parity ("[N]one", "[E]ven", "[O]dd", "[M]ark", "[S]pace")
SIGFOX_DEV_PAR = "N"
# SIGFOX device stop bits (1, 1.5, 2)
SIGFOX_DEV_SB = 1


sigfox = serial.Serial(port=SIGFOX_DEVICE, 
                       baudrate=SIGFOX_DEV_BR, 
                       parity=SIGFOX_DEV_PAR,
                       stopbits=SIGFOX_DEV_SB,
                       bytesize=SIGFOX_DEV_BS)

sigfox.write("at$ss=99999999\r")
time.sleep(10)
ans="answer is: "+sigfox.read(sigfox.inWaiting())+" sigfox"
print ans

time.sleep(1)
sigfox.close()
