# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:04:42 2018

@author: james
"""
"""
my_cx_freeze.py
To run code from cmd
python my_cx_freeze.py build
Eksp from cmd:
C:\Python32\Scripts>python my_cx_freeze.py build
"""
import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Setup_pi.py", base=base, )]

cx_Freeze.setup(
    name = "SeaofBTC-Client",
    options = {"build_exe": {"packages":["tkinter","matplotlib"]}},
    version = "0.01",
    description = "Sea of BTC trading application",
    executables = executables
    )