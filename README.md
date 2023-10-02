<h2 align="center">Python connectivity scripts for KEYSIGHT/TENMA PPS</h2>
<p align="center">
<i>Python scripts to connect to KEYSIGHT and TENMA programmable power supplies (PPS)</i>
<br>
<br>
<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
<a href="https://github.com/andriandreo/pyPPS/releases"><img src="https://img.shields.io/github/v/release/andriandreo/pyPPS"></a>
<a href="https://doi.org/10.5281/zenodo.8398410"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.8398410.svg" alt="DOI"></a>
</p>

The code includes Python scripts to connect to either KEYSIGHT or TENMA programmable power supplies and perform either sweeping voltage or pulsing voltage supply upon several selectable channels.

## Warnings:

- Only KEYSIGHT E3631A and TENMA 72-13330 (KORAD KA3000) models have been tested. The scripts should work for other devices of the same manufacturers (at least within the same series) as long as they share the same [Standard Commands for Programmable Instrumentation (SCPI) - IVI Foundation](https://www.ivifoundation.org/scpi).
- The serial COM/GPIB connection port must be specified in `inst = rm.open_resource("GPIB0::xx::INSTR")` (`xx` port, KEYSIGHT), or `ser.port = 'COMx'` (`x` port, TENMA).
- The IVI drivers for the desired equipment must be installed beforehand (**not provided**).
- In the case of the KEYSIGHT PPS, the path for `visa.ResourceManager` must be specified: something similar to `'C:/Program Files/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll'` for Windows.
- The scripts have only been tested on Windows OS. The aforementioned path will change depending on the OS.

## Installation:

Just download the latest version and run the desired script (Python 3.0+ is required) with the device connected and ON. *Remember that the IVI drivers must be installed and the right device connection port must be specified in the code.*

## Usage:

Terminology is set for a FET-derived transistor (`Vg`: gate voltage; `Vd`: drain voltage), and units are set in accordingly to the International System of Units (SI). Thus, the following parameters may be changed in the code:

**Pulsing supply:**
```py
# Pulse test parameters:

npulses = 1170 # Total number of pulses

# Duty cycle parameters:
tpulse = 0.8 # Time for pulse ON (s)
trelax = 0.2 # Time for pulse OFF (s)

# Voltage parameters:
Vg_0 = 0 # Initial supply voltage (V)
Vg_1 = 3.3  # Final supply voltage (V)
Vg_set = 0.5 # Voltage set to be supplied after the pulses (V)
```

**Sweeping supply:**
```py
# Sweep test parameters:
    #Ch 2 - Drain:
    Vd_0 = 0.36 # Initial supply voltage (V)
    Vd_f = 0.52 # Final supply voltage (V)
    Vd_step = 0.08 # In steps of x volts

    #Ch 1 - Gate:
    Vg_0 = 0 # Initial supply voltage (V)
    Vg_f = 0.8 # Final supply voltage (V)
    Vg_step = 0.1 # In steps of x volts
    EnableVg = True # True: enable secondary sweep; False: disable secondary sweep

    tsweep = 100 # Duration of each supplied step voltage (s)
    trelax = 100 # Time between the last secondary sweep of a primary sweep and the first secondary sweep of the next primary sweep (s)  
```




