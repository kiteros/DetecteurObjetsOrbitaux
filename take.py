import subprocess
import time
from datetime import datetime
import os

import board
import adafruit_bno055

import serial
from decimal import *
from subprocess import call
 
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

# If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF


def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result

print("Temperature: {} degrees C".format(sensor.temperature))
print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
print("Magnetometer (microteslas): {}".format(sensor.magnetic))
print("Gyroscope (rad/sec): {}".format(sensor.gyro))
print("Euler angle: {}".format(sensor.euler))
print("Quaternion: {}".format(sensor.quaternion))
print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
print("Gravity (m/s^2): {}".format(sensor.gravity))
print()
    

time.sleep(1)

print("Temperature: {} degrees C".format(sensor.temperature))
print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
print("Magnetometer (microteslas): {}".format(sensor.magnetic))
print("Gyroscope (rad/sec): {}".format(sensor.gyro))
print("Euler angle: {}".format(sensor.euler))
print("Quaternion: {}".format(sensor.quaternion))
print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
print("Gravity (m/s^2): {}".format(sensor.gravity))
print()
    

time.sleep(1)

print("Temperature: {} degrees C".format(sensor.temperature))
print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
print("Magnetometer (microteslas): {}".format(sensor.magnetic))
print("Gyroscope (rad/sec): {}".format(sensor.gyro))
print("Euler angle: {}".format(sensor.euler))
print("Quaternion: {}".format(sensor.quaternion))
print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
print("Gravity (m/s^2): {}".format(sensor.gravity))
print()
    

time.sleep(1)

# Enable Serial Communication
port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write(str.encode('AT'+'\r\n'))          
rcv = port.read(100).decode()
print(rcv)
time.sleep(.1)
 
port.write(str.encode('AT+CGNSPWR=1'+'\r\n'))             # to power the GPS
rcv = port.read(100).decode()
print(rcv)
time.sleep(.1)
 
port.write(str.encode('AT+CGNSIPR=115200'+'\r\n')) # Set the baud rate of GPS
rcv = port.read(100).decode()
print(rcv)
time.sleep(.1)
 
port.write(str.encode('AT+CGNSTST=1'+'\r\n'))    # Send data received to UART
rcv = port.read(100).decode()
print(rcv)
time.sleep(.1)
 
port.write(str.encode('AT+CGNSINF'+'\r\n'))       # Print the GPS information
rcv = port.read(200).decode()
print(rcv)
time.sleep(.1)
ck=1

s1 = 0
s2 = 0

counter = 0



while len(str(s1)) < 3 : # :
    fd = port.read(200).decode()        # Read the GPS data from UART
    print("new loop GPS")
    #print fd
    time.sleep(.5)
    if counter >= 50:
        break
    counter+=1
    if '$GNRMC' in fd:        # To Extract Lattitude and 
        ps=fd.find('$GNRMC')        # Longitude
        dif=len(fd)-ps
        if dif > 50:
            data=fd[ps:(ps+50)]
            print(data)
            ds=data.find('A')        # Check GPS is valid
            if ds > 0 and ds < 20:
                p=list(find(data, ","))
                lat=data[(p[2]+1):p[3]]
                lon=data[(p[4]+1):p[5]]
 
# GPS data calculation
 
                s1=lat[2:len(lat)]
                s1=Decimal(s1)
                s1=s1/60
                s11=int(lat[0:2])
                s1 = s11+s1
 
                s2=lon[3:len(lon)]
                s2=Decimal(s2)
                s2=s2/60
                s22=int(lon[0:3])
                s2 = s22+s2
 
                print(s1)
                print(s2)
###

print("Starting the program...")

APP_FOLDER = '/home/pi/PHOTO_FULLPROCESS'

totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1


print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)
print('Total:',(totalDir + totalFiles))

#create a new directory for the new set

try:
    os.mkdir(APP_FOLDER + '/set_' + str(totalDir + 1))
    #os.mkdir('/media/pi/DISQUE/debugging')
except OSError as e:
    print(e)
    print ("Creation of the directory %s failed" % APP_FOLDER)
else:
    print ("Successfully created the directory %s " % APP_FOLDER)
    
CURRENT_FOLDER = APP_FOLDER + '/set_' + str(totalDir + 1)

boussole = sensor.euler[0]
angle_vert = sensor.euler[2]
angle_horiz = sensor.euler[1]
focale = 50
pixsize = 5.97
station_number = '0001'
station_status = 'F'
tmps_expo = 8

GPS_la = 0.0
GPS_lo = 0.0

if len(str(s1)) > 3:
    GPS_la = s1
    GPS_lo =  s2
else:
    GPS_la = 46.6527
    GPS_lo =  6.3696
    


line_1 = "Boussole,AngleVert,AngleHoriz,Focale,Pixsize,StationNumber,StationStatut,TmpsExposition"
line_2 = str(boussole) + ',' + str(angle_vert) + ',' + str(angle_horiz) + ',' + str(pixsize) + ',' + station_number + ',' + station_status + ',' + str(tmps_expo)

f = open(CURRENT_FOLDER + '/param.txt', "w")
f.write(line_1 + '\n')
f.write(line_2 + '\n')
f.close()

#faire la station_

line_station = station_number + ' SA ' + str(GPS_la) + ' ' + str(GPS_lo) + ' 200. Ssa epfl team'
f2 = open(CURRENT_FOLDER + '/STATIONS.IN', "w")
f2.write(line_station + '\n')
f2.close()


while True:
    now = datetime.now()
    current = now.strftime("%Y-%m-%d+%H-%M-%S")
    cmd = "yes | gphoto2 --filename '" + APP_FOLDER + '/set_' + str(totalDir + 1) + "/pic_" + current + "+m+" + str(int(now.microsecond / 1000)) + ".%C' --capture-image-and-download"
    subprocess.call(cmd, shell=True)
    
    time.sleep(4)
    
