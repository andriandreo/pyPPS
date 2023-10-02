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

# Sweep test parameters:
    #Ch 2 - Drain:
    Vd_0 = 0.36
    Vd_f = 0.52
    Vd_step = 0.08

    #Ch 1 - Gate:
    Vg_0 = 0
    Vg_f = 0.8
    Vg_step = 0.1
    EnableVg = True

    tsweep = 100
    trelax = 100

# Sweep steps number calculation:
    Vd_nsteps = round((Vd_f - Vd_0)/Vd_step)
    Vg_nsteps = round((Vg_f - Vg_0)/Vg_step)

# Sweep loop:

    # Secondary Sweep Disabled:
    if EnableVg == False:
        channel = 2
        voltage = Vd_0
        for i in range (0, Vd_nsteps + 1):
            command = tf.set_voltage(channel, voltage)
            ser.write(command)
            time.sleep(tsweep)
            voltage += Vd_step

    # Secondary Sweep Enabled:
    else:
        # Drain voltage steps:
        channel = 2
        for i in range (0, Vd_nsteps + 1):
            twait = tsweep
            voltage = Vd_0 + i*Vd_step
            command = tf.set_voltage(channel, voltage)
            ser.write(command)
            time.sleep(0.1)

            # Gate voltage steps:
            channel = 1
            voltage = Vg_0
            for j in range (0, Vg_nsteps + 1):
                command = tf.set_voltage(channel, voltage)
                ser.write(command)
                time.sleep(tsweep)
                voltage += Vg_step

            # Wait time before next Vd step and change back to Ch 2 - Drain:
            time.sleep(trelax)
            channel = 2

# Set the voltages to 0 after the sweep is completed:
    for i in range (1, 3):
        channel = i
        voltage = 0
        command = tf.set_voltage(channel,voltage)
        ser.write(command)
        time.sleep(0.1)

# Turn power supply output OFF
#    output = 'OUT0\n'
#    ser.write(output.encode('utf-8'))
#    time.sleep(0.1)

    print(f'Test performed')
