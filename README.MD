# AutoClicker Using Python
Like my last project, this was one I probably didn't need to make; but I thought it would be fun to make, and it was! I just enjoy coding in Python; something about the language, with it's high-level nature, makes coding in it fun to write.

This program has an extremely specific purpose - if you arrived in this repo without knowing it, then it probably won't be of use to you.

It was designed to be an autoclicker for BlueStacks. After losing my save file 13/16 chapters into a game, I was bugged. Bugged enough that I wasn't about to manually go through all that shit again, but not bugged enough that I wasn't willing to find some way to automate the tedium. So I made this.

Minimalistic GUI. But I'm satisfied. Coded in Sublime Text 3; ctrl+b is used to launch the app from the editor into the Windows native command line. A very comfortable developer environment for my tastes.

How to use:
* First, get the two dependencies: `pip install keyboard` and `pip install pyautogui`.
* Run main.py (you can use app.cmd, I am too lazy to make a proper EXE.)
* Select your desired time interval.
* Either hit the start button or press F3 to start, and either hit the stop button or press F4 to stop.
* Note you must stop the program before changing speeds; you cannot change speeds while it is autoclicking.

Features I will consider adding:
* Automatically disabling the program with a native mouse click.
* Custom hotkeys for enable/disable and custom time intervals (could easily do that, it's just a matter of tedium).