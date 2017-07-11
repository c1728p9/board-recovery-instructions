# Unbricking Guide for mbed Devices

Before starting the unbricking process, it will be helpful to determine whether the actual bootloader on your target bricked, or just it's interface. Follow the steps below to determine what needs to be done to recover your board.

![](images/flowchart.png "Flowchart used to determine status of bricked board")

## Unbricking bootloader
Follow the steps in this section if the flowchart at the beginning of the document determined that your board's bootloader has been bricked.

### Required items
* [pyOCD](https://github.com/mbedmicro/pyOCD).
* [SWDAP debugging probe](https://developer.mbed.org/platforms/SWDAP-LPC11U35/).
* [10 pin debug cable](https://developer.mbed.org/platforms/SWDAP-LPC11U35/).

### Step 1: Install pyOCD
pyOCD is an Open Source Python 2.7 based library for programming and debugging ARM Cortex-M microcontrollers using CMSIS-DAP. In a terminal, you can install pyOCD using the following command:
`sudo pip install pyOCD`

Once pyOCD is installed, make a new directory, and put the file `restore_k20dx_firmware.py` at the root of that directory. `restore_k20dx_firmware.py` is a Python script used to flash binaries onto a bricked board.

### Step 2: Choose firmware to flash to the board
* Find a working bootloader that you would like to flash to the board. Rename its binary file to `rom.bin`.
* Place `rom.bin` in the same root directory as the Python script.

### Step 3: Connect debugger to bricked board
Locate the 10-pin header associated with your board's k20dx flash. Usually, the header is near the OpenSDA USB port on the device. Connect your 10-pin debug cable to this header, so pin 1 of the header connects to the red wire on your debug cable, as seen in the image below. The pin numbering is printed on the silkscreen of your board for your reference. After you have connected the debugger to your board, ensure that both the debugger and the bricked board are plugged into a power source (usually via USB cable).

![](images/header.png "K20dx flash chip and associated 10-pin header. Pin 1 on the header had been circled.")

![](images/connected.png "Connecting the debugger to the bricked board")

### Step 4: Flashing bricked board
Now you are ready to flash the bricked board with your chosen firmware. Go to your directory that has the Python script, `restore_k20dx_firmware.py`. To run the script, use the following command (run with superuser privileges): `sudo python restore_k20dx_firmware.py`.

The console then prompts you to specify which board to use as the debugger. The output looks similar to the following:
```
id => usbinfo | boardname
0 => NXP LPC800-MAX [k20d50m]
1 => FRDM-K64F [k20d50m]
input id num to choice your board want to connect
```
Choose `id=0` here because that represents the debugger, and then hit enter. The unbricking begins. The terminal reports something like the following:

```
brandon@mint64 ~/Work/pyOCD $ sudo python restore_k20dx_firmware.py
WARNING:root:Invalid coresight component, cidr=0x0
WARNING:root:Invalid coresight component, cidr=0x1010101
WARNING:root:Invalid coresight component, cidr=0x0
Flashing rom.bin to target
Recovery successful
```

### Step 5: Verify
Now, unplug and replug the board into your computer normally (without holding down the reset button). The device mounts normally.

## Unbricking interface
Follow the steps in this section if the flowchart at the beginning of the document determined that your board's interface has been bricked.

### Step 0: Required items
* Windows 7 machine

### Step 1: Enter device into bootloader mode
Hold down the reset button on your board, and while holding down the button, plug it into a Windows 7 machine. The board should mount as a `BOOTLOADER`.

![](images/bootloader.png "Image of what the bootloader looks like on windows7")

### Step 2: Drag working binary onto your device
Drag and drop your binary onto the device while it is in bootloader mode.

### Step 3: Verify
Now, unplug and replug the board into your computer normally (without holding down the reset button). The device mounts normally.
