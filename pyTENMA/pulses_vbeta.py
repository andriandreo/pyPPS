import serial
import time

import tenma_functions as tf

# Define the device connection settings and parameters
with serial.Serial() as ser:

    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.bytesize = 8
    ser.timeout = 10
    ser.parity = 'N'
    ser.open()

    #print(ser)

    time.sleep(2)

# Check and print the device connection info
    command = '*IDN?\n'
    ser.write(command.encode('utf-8'))
    response = ser.readline()
    dresp = response.decode('utf-8')
    print(f'Connected to : {dresp}')

# Set the maximum current for the two channels of the power supply
    for i in [1,2]:
        channel = i
        current = 0.1
        command = tf.set_maxcurrent(channel, current)
        ser.write(command)
        time.sleep(0.1)

# Set the value for the Drain Voltage
#    channel = 2
#    voltage = 0.4
#    command = tf.set_voltage(channel,voltage)
#    ser.write(command)
#    time.sleep(0.1)

# Turn power supply output ON
    output = 'OUT1\n'
    ser.write(output.encode('utf-8'))
    time.sleep(0.1)

# Pulse test parameters:
    npulses = 1170
    tpulse = 1.5
    trelax = 0.5
    Vg_0 = 0
    Vg_1 = 0.6
    Vg_set = 0.5

# Pulses loop:
    channel = 1
    pulse_flag = True
    for i in range (0, npulses*2):
        if pulse_flag == True:
            voltage = Vg_1
            twait = tpulse
            pulse_flag = False
        else:
            voltage = Vg_0
            twait = trelax
            pulse_flag = True
        command = tf.set_voltage(channel,voltage)
        ser.write(command)
        time.sleep(twait)

# Ensure the last Vg applied is the set point for the next experiment with steady state
    #if voltage == Vg_0:
    voltage = Vg_set
    command = tf.set_voltage(channel,voltage)
    ser.write(command)
    time.sleep(0.1)

# Turn power supply output OFF
#    output = 'OUT0\n'
#    ser.write(output.encode('utf-8'))
#    time.sleep(0.1)

    print(f'Test performed')
