AES MixColumns Python Implementation
Description
This repository contains a simple Python implementation of the MixColumns operation from the AES (Advanced Encryption Standard) encryption algorithm. The code performs matrix multiplication in GF(2^8) using bitwise operations for efficiency, without external libraries.
The MixColumns step mixes the bytes in each column of the AES state matrix to provide diffusion.
Usage

The state is a 4x4 list of integers (0-255), representing the AES state matrix.
Call mix_columns(state) to modify the state in place.
The example shows before/after values (add print statements as needed).

What Was Done

Implemented the MixColumns transformation using manual GF(2^8) multiplications for 2 and 3.
Simplified from a general multiplication function to direct bitwise operations for performance.
Tested with a sample AES state matrix.

Steps to Run the Code


Copy the Code:
Save the following code into a file named mix_columns.py
Open a Terminal or Command Prompt:
On Windows: Search for "cmd" or "PowerShell".
On macOS/Linux: Open the Terminal app.


Navigate to the File Directory:
Use the cd command to change to the folder where you saved mix_columns.py.

Run the Script:
Execute the code with:
textpython mix_columns.py
