# aelna354's AutoClicker Using Python

Like my last project, this was one I probably didn't need to make; but I thought it would be fun to make, and it was! I just enjoy coding in Python; something about the language, with it's high-level nature, makes writing code in it fun.

After losing my save file 13/16 chapters into a visual novel that didn't have a skip function, I was bugged. Bugged enough that I wasn't about to manually go through it all again, but not bugged enough that I wasn't willing to find some way to automate the tedium. So I made this for both a practical reason and for fun; and it was both fun and practical.

It's a minimalistic GUI autoclicker program. For what I intended to use it for, it did it's job and I'm quite satisfied.

How to use:
* First, you will need to install the two dependencies with `pip install keyboard` and `pip install mouse`.
* Run main.py (you can use app.cmd, I am too lazy to make a proper EXE.)
* Select your desired time interval for seconds between clicks (from left to right, it is fastest to slowest, by default set to fastest).
* Press the F3 or F4 button to toggle the program. You can also hit the RMB to disable it.
* Note you must stop the program before changing speeds; you cannot change speeds while it is autoclicking.

Coded from April 20th to 22nd 2018 using Python 3 with tkinter, as well as the packages [keyboard](https://github.com/boppreh/keyboard) and [mouse](https://github.com/boppreh/mouse). My IDE of choice was Sublime Text 3 with ctrl+b running the .py file right into the native Windows terminal.