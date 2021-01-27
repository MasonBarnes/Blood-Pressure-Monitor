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
    import grp
    os.system("sudo pip3 install flask")
    os.system("sudo pip3 install matplotlib")
    os.chdir(os.path.dirname(os.path.abspath(__file__)).replace("install.py", "main.py"))
    cwd = os.getcwd()
    main_path = os.path.abspath("main.py")
    try:
        os.chdir("/Users/" + getpass.getuser() + "/Library/LaunchAgents")
    except OSError:
        os.chdir("/Users/" + getpass.getuser() + "/Library")
        os.mkdir("LaunchAgents")
        os.chdir("LaunchAgents")
    with open("blood_pressure_manager.plist", "w") as f:
        f.write("""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>blood_pressure_manager</string>

    <key>OnDemand</key>
    <false/>

    <key>UserName</key>
    <string>""" + getpass.getuser() + """</string>

    <key>ProgramArguments</key>
    <array>
            <string>sudo python3 \"""" + main_path + """\"</string>
    </array>
</dict>
</plist>
        """.strip())
    webbrowser.open("http://localhost:7634/")
    os.chdir(cwd)
    os.system("sudo python3 \"" + main_path + "\"")
else:
    print("Operating system not supported!")
    time.sleep(5)