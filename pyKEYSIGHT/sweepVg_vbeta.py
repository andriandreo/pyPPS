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

# Sweep test parameters:
tsweep = 100
Vg_0 = 0.2
Vg_f = 5
Vg_step = 0.4

# Sweep steps number calculation:

Vg_nsteps = round((Vg_f - Vg_0)/Vg_step)

# Sweep loop:
channel = 'P25V'
voltage = Vg_0
for i in range (0, Vg_nsteps + 1):
    command = kf.set_voltage(channel,voltage,current)
    inst.write(command)
    time.sleep(tsweep)
    voltage += Vg_step

# Turn power supply output OFF, reset and close the connection
#inst.write('OUTPUT:STATE OFF')
#time.sleep(0.1)

#reset = '*RST'
#inst.write(reset)

time.sleep(0.1)
voltage = 0
command = kf.set_voltage(channel,voltage,current)
inst.write(command)

inst.write('SYSTem:BEEPer:IMMediate')
inst.write('OUTPUT:STATE OFF')

inst.close()

print(f'Test performed')
