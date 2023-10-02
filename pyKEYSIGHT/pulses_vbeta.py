import pyvisa as visa
import time

import keysight_functions as kf

# WARNING: Ensure the Keysight I/O Configuration ('I/O Button' in front panel) is correctly set for the GPIB interface

# Open Connection Keysight Visa
rm = visa.ResourceManager('C:/Program Files/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll')

# Connect to VISA Address
# GPIB Connection: 'GPIP0::xx::INSTR'
inst = rm.open_resource("GPIB0::8::INSTR")

# Set Timeout - 1 second
inst.timeout = 1000

# Check and print the device connection info, Beep once it's done
inst.write('*IDN?')
response = inst.read()
print(f'Connected to: {response}')

inst.write('SYSTem:BEEPer:IMMediate')

# Set the maximum current for the two channels of the power supply
current = 0.1

# Set the value for the Drain Voltage
#    channel = 'P6V'
#    voltage = 0.4
#    command = kf.set_voltage(channel,voltage,current)
#    inst.write(command)
#    time.sleep(0.1)

# Turn power supply output ON
inst.write('OUTPUT:STATE ON')
time.sleep(0.1)

# Pulse test parameters:
npulses = 1170
tpulse = 0.8
trelax = 0.2
Vg_0 = 0
Vg_1 = 3.3
Vg_set = 0.5

# Pulses' loop:
channel = 'P25V'
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
    command = kf.set_voltage(channel,voltage,current)
    inst.write(command)
    time.sleep(twait)

# Ensure the last Vg applied is the set point for the next experiment with steady state
#if voltage == Vg_0:
voltage = Vg_set
command = kf.set_voltage(channel,voltage,current)
inst.write(command)
time.sleep(0.1)

# Turn power supply output OFF, reset and close the connection
#inst.write('OUTPUT:STATE OFF')
#time.sleep(0.1)

#reset = '*RST'
#inst.write(reset)
#time.sleep(0.1)

inst.write('SYSTem:BEEPer:IMMediate')

inst.close()

print(f'Test performed')
