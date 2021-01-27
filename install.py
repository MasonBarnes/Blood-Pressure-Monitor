import os
import platform
import getpass
import time
import webbrowser

if platform.system() == "Windows":
    os.system("pip install flask")
    os.system("pip install matplotlib")
    cwd = os.getcwd()
    main_path = os.path.abspath("main.py")
    os.chdir(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(getpass.getuser()))
    with open("blood_pressure_manager.bat", "w") as f:
        f.write("python3 \"" + main_path + "\"")
    webbrowser.open("http://localhost:7634/")
    os.chdir(cwd)
    os.system("python3 \"" + main_path + "\"")
elif platform.system() == "Darwin":
    os.system("sudo pip3 install flask")
    os.system("sudo pip3 install matplotlib")
else:
    print("Operating system not supported!")
    time.sleep(5)