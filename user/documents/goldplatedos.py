import calendar
import datetime
import getpass
import logging
import os
import platform
import random
import shutil
import string
import wikipedia

safety = {
    "safety": str(random.choice(
        ["safe", "very safe", "extremely safe", "completely safe"]))
}
passhint = {}
user = {
    "username": getpass.getuser(),
    "password": "chicken",
    "backup_pass": "chicken",
}
year = datetime.datetime.now().strftime("%Y")
hour = datetime.datetime.now().hour
memos = []
packages = ["ascii_cub", "eggs", "mathgreekabc",
            "greetMe", "quickcalc", "commandnow",
            "null", "timemachine"]
packages_installed = []
package_error = "Package error: No such package installed. SUGGESTION: Go to Terminal to install."
machine_name = user["username"] + "s-GoldplatedOS"
version = "3.2 (Bemru)"
new = [
    "Better login",
    "Enhanced display and performance",
    "More apps, commands, and packages",
    "Reset command",
    "User info and FAQ page"
]
default = "\033[33m"
pink = "\033[95m"
blue = "\033[36m"
text_color = {
    "color": default
}


class EchoClass(string.Template):
    delimiter = "@"

    substitutes = {
        "username": user,
        "user": user,
        "path": os.getcwd(),
        "home": os.path.expanduser('~'),
        "year": year,
        "version": version,
        "credits": f"© 2022-{year} BeeDev"
    }


class Printer(string.Template):
    delimiter = "@"
    vars = {
        "credits": f"© 2022-{year} BeeDev"
    }


def clear():
    os.system('clear')


def login():
    while True:
        clear()
        print(text_color["color"] + ("=" * 29)
          + "LOGIN TO "+user["username"].upper()+"'S PC" + ("=" * 29))
        if len(passhint) == 0:
            print("No hint available.")
        else:
            print("HINT: " + passhint["hint"])
        password = input("Password: ")
        if password == user["password"]:
            print("Correct password.")
            everything2()
        else:
            print("Incorrect password.")


def everything():
    clear()
    login()
    clear()
    main()


def everything2():
    clear()
    main()


def calendar_app():
    month = int(input("Month: "))
    year = int(input("Year: "))
    if calendar.isleap(year) is True:
        print("\nThe year you entered is a leap year.\n")
    else:
        print("\nThe year you entered is not a leap year.\n")
    print(calendar.month(year, month, w=5))


def calc_app():
    equation = str(eval(input("Enter your equation: ")))
    print("The answer is " + equation + ".")


def passgen_app():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!/'@#$%^&*()/\"{}[]:;<>,.?/~`"
    codelen = int(input("Length: "))
    passwordgen = "".join(random.sample(chars, codelen))
    print(f"Generated password: {passwordgen}")


def pycode_app():
    line_count = 1
    while True:
        code = input(f"[{line_count}]: ")
        line_count = line_count + 1
        try:
            if code == "quit":
                print("Exiting Pycode...")
                break
            else:
                exec(code)
        except Exception:
            print("Bad python line. Try again.")
            continue
def numberguess_app():
    amount = int(input("Up to what number? "))
    guess = int(input("What's your choice? "))
    number = random.randint(1, amount)
    if number == guess:
        print("You win!")
    else:
        print("You lose.")


def netsurf_app():
    while True:
        topic = input("🔎 Search for: ")
        if topic.lower() != "exit":
            try:
                my_page = wikipedia.page(topic)
                wikipedia_results = my_page.content
                print(f"Results for {topic}...")
                print(f"WIKIPEDIA SAYS: {wikipedia_results}")
            except:
                print(
                    f"Either there is no Wikipedia page on {topic} or you have not downloaded the Python wikipedia module.")
        else:
            break


def textreader_app():
    while True:
        file = input("File: ")
        try:
            target = open(file, 'r').read()
            print(target)
        except Exception:
            print("Error occurred.")
            break


def list_app():
    while True:
        option = input("Add to list (a) or see list (s)? ")
        if option.lower() == "a":
            item = input("Add memo: ")
            if item.lower() == "exit":
                break
            else:
                memos.append(item)
        elif option.lower() == "s":
            object_num = 1
            print("\nMY MEMOS\n---------------------------------")
            while object_num < len(memos):
                for object in memos:
                    print(f"MEMO NO. {object_num}: " + object)
                    object_num += 1
            print("\n")
            break
        else:
            break


def terminal_app():
    print("\n" + ("=" * 10) + "TERMINAL" + ("=" * 10) + "\n")
    print("Type 'help' for instructions if you are a beginner. To exit the language bc, you must press CONTROL-D. Also, if you type uname in the Terminal, you will get the computer type of the background OS.\n")
    while True:
        term_cmd = input("$ ").lower()
        if term_cmd.startswith("seed install ") is True:
            term_cmd = term_cmd.replace("seed install ", "")
            term_cmd = term_cmd.lower()
            if term_cmd in packages:
                packages_installed.append(term_cmd)
                if "ascii_cub" in packages_installed:
                    print("ascii_cub package installed.")
                    global cub_on
                    cub_on = True
                else:
                    cub_on = False

                if "eggs" in packages_installed:
                    print("eggs package installed.")
                    global eggs_on
                    eggs_on = True
                else:
                    eggs_on = False

                if "mathgreekabc" in packages_installed:
                    print("mathgreekabc package installed.")
                    global greek_on
                    greek_on = True
                else:
                    greek_on = False

                if "greetme" in packages_installed:
                    print("greetMe package installed.")
                    global greet_on
                    greet_on = True
                else:
                    greet_on = False

                if "quickcalc" in packages_installed:
                    print("quickcalc package installed.")
                    global calc_on
                    calc_on = True
                else:
                    calc_on = False

                if "commandnow" in packages_installed:
                    print("commandnow package installed.")
                    global command_on
                    command_on = True
                else:
                    command_on = False
                
                
                if "timemachine" in packages_installed:
                    print("timemachine package installed.")
                    global time_on
                    time_on = True
                else:
                    time_on = False

                if "null" in packages_installed:
                    print("It is in every package---it is null.")
            else:
                print("Inexistent package.")
        elif term_cmd.lower() == "installation list":
            if len(packages_installed) == 0:
                print("No packages installed.")
            else:
                print("===Installation List===")
                for package in packages_installed:
                    print(package)
        elif term_cmd.lower() == "package list":
            print("===All Packages===")
            print("ascii_cub - cute ASCII bear cub.")
            print("eggs - random egg emojis.")
            print(
                "greetme - greets you based on the time of day when you type 'greet me'.")
            print(
                "mathgreekabc - prints the Greek alphabet that is used in math.")
            print("null - what do you think it does?")
            print("quickcalc - automating equations by starting the equation with 'calc' so that the user does not have to keep opening up the Calculator app.")
            print(
                "timemachine - shows events that occured in years 1, 2, 3, 1066, 1492, 1500, 1605, 1776, 1861, 1900, this year, or 2070 AD.")
            print(
                "commandnow - allows users to use commands.")
        elif term_cmd.lower() == "help":
            print("THE TERMINAL: Terminal is a simple app designed for the GoldplatedOS. It can download useful (or just fun) packages, run code, and run commands.")
            print("MISCELLANEOUS: You can discover new packages by typing 'package list'. You can also see what you have installed by typing 'installation list', much like the 'pip list' command.")
            print("MISCELLANEOUS 2: If you don't know already, you can install any Terminal package by typing 'seed install', and the package name. Like this: seed install <package_name>. ")
        elif term_cmd.lower() == "exit":
            print("\n")
            break
        else:
            os.system(term_cmd)


def music_app():
    print("This app will tell you what motion to do to simulate instruments.")
    print("\nPlease type 'drum' for drums, 'flute' for flutes, 'cymbal' for cymbals, and 'piano' for piano.")
    while True:
        instrument = input("What's your choice? ")
        if instrument.lower() == "drum":
            print("Drum on a table or flat surface to simulate a drum.")
        elif instrument.lower() == "flute":
            print("Whistle to simulate a flute.")
        elif instrument.lower() == "cymbal":
            print("Add a cymbal sound by hitting metal.")
        elif instrument.lower() == "piano":
            print("Tap with all 10 fingers on a flat surface.")
        elif instrument.lower() == "exit":
            print()
            break
        else:
            print(
                "Sorry, that instrument isn't included. Try 'drum', 'flute', 'cymbal' or 'piano'!")


def word_scramble_app():
    words = ["interesting", "clever", "turtle", "lime", "squid", "candy",
             "mathematics", "emoji", "piano", "dictionary", "llama", "globe",
             "alarm", "language", "kitten", "dinosaur", "clock", "french",
             "badge", "feather", "air", "bird", "duck", "lantern", "mama",
             "papa", "hairband", "cube", "monkey", "circle", "warm", "cold",
             "red", "orange", "yellow", "green", "blue", "purple", "black",
             "white", "grey", "kaleidoscope", "braces", "paper", "pencil",
             "pen", "glue", "scissors", "tape", "gnat", "animal", "baby",
             "magic", "spider", "furry", "bookworm"]
    word = random.choice(words)
    print(f"The word is {len(word)} letters long!")
    word_split = []
    for char in word:
        word_split.append(char)
    word_split = sorted(word_split)
    print(f"LENGTH OF WORD: {len(word_split)}")
    print("SCRAMBLED LETTERS OF WORD:")
    for character in word_split:
        print(f"~ {character}")
    while True:
        print("That's all the letters. Now, unscramble the letters to make a word!")
        guessed_word = input("Word: ")
        try:
            if guessed_word.lower() == word:
                print(f"Yay! You got it! The word was {word}!\n")
                break
            elif guessed_word.lower() != word:
                print(f"Nope. {guessed_word} wasn't it.")
            else:
                print("Something happened and we couldn't process the info.")
        except Exception:
            print("An error occured.\n")
            break
    again = input("Do you want to play again [y/n]? ")
    if again.lower() == "y":
        word_scramble_app()
    elif again.lower() == "n":
        print("Game closed!")
    else:
        print("Invalid command.")

def security():
    print("Welcome to Goldplated Antivirus! Let's start making your computer SAFE!")
    print("You can choose between safe, very safe, extremely safe and completely safe.")
    types = ["safe", "very safe", "extremely safe", "completely safe"]
    type = input("Choice: ")
    if type.lower() not in types:
        print("I'm afraid we don't have that type. Try another?")
    elif type.lower() in types:
        safety["safety"] = type
        print(f"Okay, it's now set to {safety['safety']}!")

def main():
    def reboot():
        clear()
        everything()
    path = f"/Users/" + user["username"] + "/Documents"
    command_amount = 0
    print(text_color["color"] + ("=" * 93))
    print("""

     WELCOME TO YOUR
                                                                                _______    _______
     ________   _______  |    ____   ___  |     _____    _______  _____  ____  /       \  |
    /     ___  /       \ |    |   \ |__/  |    /_____\      |    |_____  |   \|         | \______
    \_______/  \_______/ \___ |___/ |     \___ |     |      |    |_____  |___/ \_______/   _____/

    """)
    print(("=" * 93) + "\n")
    print(("=" * 41) + "SYSTEM INFO"
          + ("=" * 41) + "\n")
    print("CPUs: " + str(os.cpu_count()))
    print("Disk usage: " + str(shutil.disk_usage(path)))
    print("Host: " + user["username"] + "s-GoldplatedOS.local")
    print("Machine: " + str(platform.machine()))
    print("Processor: " + str(platform.processor()))
    print(("=" * 93) + "\n")
    print(
        f"GOLDPLATED ANTIVIRUS ~ VIRUSES: 0 viruses found | STATUS: {safety['safety']}")
    print("TIP ~ Type 'help' for a list of commands.\n")
    while True:
        command = input(text_color["color"]
                        + user["username"] + f"@{machine_name} > ")
        command_amount += 1
        if command.lower() == "help":
            print("BASIC TOOLS")
            print("about - gives OS version info.")
            print("makehint - creates/changes a password hint for when you login.")
            print("apps - gives list of apps. Was in Unix too.")
            print("cal - prints a calendar. Was in Unix too.")
            print("changecolor - changes font color.")
            print("changepass - changes the password until shutdown.")
            print("credits - view the credits.")
            print("date - gives the date. Was in Unix too.")
            print("defaultlang - shows the default language on your operating system.")
            print("echo <text> - prints text to screen.")
            print("faq - frequently asked questions about GoldplatedOS systems.")
            print("filesize - prints amount of bytes in file.")
            print("getpass - tells your password.")
            print("getuser - tells your username.")
            print("help - gives list of commands (this page).")
            print("removefile - deletes file.")
            print("renamefile - renames file.")
            print(
                "requirements - shows needed requirements for running all or parts of the GoldplatedOS.")
            print(
                "userinfo - information about your computer-related things (including packages downloaded).")
            print("whoami - shows username. Was in Unix too.")
            print("who - displays who is on the OS. Was in Unix too.")
            print("new - see what is new in the latest version.")
            print("ondisk <disk> - finds file on a disk.")
            print("ssh - the Summer Shell.")
            print("var <varname> = <varvalue> - makes a variable for echo.")
            print("FUN AND HELPFUL")
            print("acronym <words> - tool for making acronyms")
            print("banner - tool for ascii art makers. Was in Unix too.")
            print("getline <file> - generates random lines from a file.")
            print(
                "reverse <file/text> - reverses text and files. NOTE: Periods cannot be used in text.")
            print("roman <numberal> - shows the integer equivalent of a roman numberal.")
            print("BOOTING, RESTARTING, RESETING, SHUTDOWN")
            print("reboot - restarts the OS (does not reset password).")
            print(
                "reset - resets the OS (password will revert to default like in shutdown).")
            print("shutdown - shuts down the OS (and resets password).")
        elif command.lower() == "about":
            print(
                f"The GoldplatedOS v.{version} © 2022-{year} is an Unix-like TUI (text-based user interface) operating system built to be a fun, additional OS. It is for 8+ year olds.")
        elif command.startswith("echo ") is True:
            try:
                command = command.replace("echo ", "")
                echo = EchoClass(command)
                echo = echo.safe_substitute(echo.substitutes)
                print(echo)
            except Exception as e:
                print("An error occured.")
        elif command.startswith("var ") is True:
            try:
                command = command.replace("var ", "")
                varname, varvalue = command.split(" = ")
                EchoClass.substitutes[varname] = eval(varvalue)
            except:
                print("An error occured.")
        elif command.lower().startswith("whoami") is True:
            print("This time?")
            print(os.system(command))
        elif command.lower().startswith("cat ") is True:
            command = command.split(" ")
            command.pop(0)
            for file in command:
                file = open(file).read()
                print(file)
        elif command.lower().startswith("who") is True:
            print(os.system(command))
        elif command.lower() == "changepass":
            while True:
                authorize = input("Old password: ")
                if authorize == user["password"]:
                    print("Authorized!")
                    break
                else:
                    print("Not authorized!")
            while True:
                newpass = input("New password: ")
                if newpass.lower() == "password":
                    print("This is not a secure password! You should change it.")
                elif newpass.lower() == "123":
                    print("This is not a secure password! You should change it.")
                else:
                    user["password"] = newpass
                    print("Password changed!")
                    revert = input("Do you want to revert it [y/n]? ")
                    if revert.lower() == "y":
                        user["password"] = user["backup_pass"]
                        print("Reverted!")
                        break
                    elif revert.lower() == "n":
                        break
                    else:
                        print("Invalid option.")
        elif command.lower() == "changecolor":
            print("Current color: {}".format(text_color["color"]))
            print("Available options: pink, blue, default (yellow)")
            color = input("Color: ")
            if color.lower() == "pink":
                text_color["color"] = pink
                print("Changed!")
            elif color.lower() == "blue":
                text_color["color"] = blue
                print("Changed!")
            elif color.lower() == "default":
                text_color["color"] = default
                print("Changed!")
            else:
                print("That is not an available color.")
        elif command.lower().startswith("banner ") is True:
            print(os.system(command))
        elif command.lower().startswith("reverse ") is True:
            parts = command.split("reverse ", 1)
            if len(parts) >= 2 and parts[1] and "." in command:
                try:
                    parts.pop(0)
                    parts = str(parts)
                    parts = parts.replace("['", "")
                    parts = parts.replace("']", "")
                    print(open(parts).read()[::-1])
                except Exception:
                    print("An error occurred.")
            else:
                print(command.replace("reverse ", "")[::-1])
        elif command.lower() == "date":
            print(os.system(command))
        elif command.lower().startswith("cal") and not command.lower() == "calendar":
            print(os.system(command))
        elif command.lower() == "ver":
            print(f"GoldplatedOS Version {version}")
        elif command.lower() == "credits":
            print(f"© 2022-{year} BeeDev")
        elif command.lower() == "ssh":
            while True:
                code = input(">>> ")
                printer = Printer(code)
                if code.startswith("write ") is True:
                    try:
                        print(printer.safe_substitute(
                            printer.vars).split(' ', 1)[1])
                    except:
                        print("An error occured.")
                elif code.startswith("var ") is True:
                    try:
                        code = code.split(" ")
                        code.pop(0)
                        code = " ".join(code)
                        varname, varvalue = code.split(" = ")
                        printer.vars[varname] = eval(varvalue)
                    except:
                        print("An error occured.")
                elif code.startswith("$$") is True:
                    pass
                elif code.startswith("if ") is True:
                    code = code.replace("otherwise ", "else ")
                    print(exec(code))
                elif code.lower() == "exit":
                    break
                else:
                    print("ERROR: Unknown command.")
        elif command.startswith("factorial ") is True:
            command = command.replace("factorial ", "")
            try:
                command = int(command)
                if command > 0:
                    factorial = 1
                    for i in range(2, command + 1):
                        factorial *= i
                    print("FACTORIAL OF", command, ": ", factorial)
                else:
                    print("ERROR: Number cannot be negative.")
            except Exception:
                print("An error occured.")
        elif command.lower() == "uname":
            print(
                "GoldplatedOS " + user["username"] + f" v.{version} {str(platform.machine())} {str(platform.processor())}")
        elif command.lower() == "defaultlang":
            os.system("echo $LANG")
        elif command.lower() == "faq":
            print("\nFAQ")
            print("""
Q. What is this?
A. This is an attempt to create a fully-functional Unix-like operating system in Python.

Q. Will there ever be a GUI?
A. Yes, eventually. Plans to make a GUI are being made.

Q. Is there a way to make an app?
A. Yes, there is. You can create an app and send it to us. We'll review it and add it if we like it.

Q. I have heard some operating system come with their own programming languages---like Unix has Bash or other things (awk, c, dc, etc.)---does GoldplatedOS have one?
A. Yes, we do. The Unix programming languages bc and dc and the cross-platform Python language are our official programming languages. Summer sorta works, but it's for fun right now.

Q. Any chance I can program C and/or Ruby on my GoldplatedOS?
A. C, no. Ruby, yes. You can run Ruby files through Terminal if you have it set up.

Q. Will I ever get colors for my Python editor?
A. Sorry, no. Not until we make a GUI.

Q. I typed bc into the command line and I received an error (Invalid command). What to do?
A. Open the terminal and type bc. To exit, press CONTROL-D.

Q. Does the Antivirus actually work?
A. No, not really. But GoldplatedOS does have some security stuff, like passwords and not permit one to change their password to 'password' or '123'.

Q. What should I use GoldplatedOS for?
A. You can use it for its user-friendly Terminal (perfect for aspiring programmers and people who like Terminals) and its many great apps.

Q. Can I run my GoldplatedOS by itself? Without a background operating system?
A. No, you can't. The GoldplatedOS was coded in Python (not C or C++ or any assembly language) so it has to have a 'background operating system'.

Q. Can I have a little emoji in my password?
A. You can, yes. But it might be hard to remember and type.

Q. Can I put my Python operating system on GoldplatedOS?
A. Sure! Make a TUI operating system, send it in, and we see if we should put a little virtual app of your operating system in GoldplatedOS.

Q. Where does the user info (like how many packages I downloaded and how many commands I typed) go? Anywhere besides the userinfo page?
A. It goes straight to the userinfo page. No. Also, they are just variables.

            """)
        elif command.lower() == "getpass":
            print(user["password"])
        elif command.lower() == "reset":
            logging.warning(
                "Resetting will revert the password to the original.")
            sure = input("Are you sure you want to reset your OS [y/n]? ")
            if sure.lower() == "y":
                user["password"] = user["backup_pass"]
                memos.clear()
                passhint.clear()
                print("Resetted!")
                reboot_program = input("Would you like to reboot [y/n]? ")
                if reboot_program.lower() == "y":
                    reboot()
                elif reboot_program.lower() == "n":
                    print("OS not rebooted.")
                else:
                    print("Invalid option.")
            elif sure.lower() == "n":
                print("OS not resetted.")
            else:
                print("Invalid option.")
        elif command.lower() == "makehint":
            while True:
                authorize = input("Old password: ")
                if authorize == user["password"]:
                    print("Authorized!")
                    break
                else:
                    print("Not authorized!")
            hint = input("Hint: ")
            passhint["hint"] = hint
            print("Hint made.")
        elif command.lower() == "getuser":
            print(getpass.getuser())
        elif command.lower().startswith("ondisk ") is True:
            command = command.replace("ondisk ", "")
            print(os.listdir(command))
        elif command.lower().startswith("ls") is True:
            print(os.system(command))
        elif command.lower().startswith("mkdir ") is True:
            os.mkdir("/Users/"+ user["username"] + "/Documents/- 1. curriculum for bee (2021-2022)/programming/GoldplatedOS/user/documents/" + command.split(" ", 1)[1])
            print("Directory made.")
        elif command.lower().startswith("cd ") is True and command.lower() != "cd documents":
            os.chdir("/Users/"+ user["username"] + "/Documents/- 1. curriculum for bee (2021-2022)/programming/GoldplatedOS/user/documents/" + command.split(" ", 1)[1])
        elif command.lower() == "cd documents":
            os.chdir("/Users/"+ user["username"] + "/Documents/- 1. curriculum for bee (2021-2022)/programming/GoldplatedOS/user/documents/")
        elif command.lower().startswith("getline ") is True:
            file = command.lower().replace("getline ", "")
            file = open(file).read()
            lines = file.split(".")
            print(random.choice(lines) + ".")
        elif command.lower().startswith("acronym ") is True:
            words = command.lower().replace("acronym ", "")
            words = words.split(" ")
            array = [element[0].capitalize() for element in words]
            print("".join(array))
        elif command.lower().startswith("roman ") is True:
            roman = command.lower().replace("roman ", "")
            roman = roman.upper()

            # Credit to a Stack Overflow post
            def romanToInt(s: str):
                roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                         'C': 100, 'D': 500, 'M': 1000}
                num = 0
                for i in range(len(s)):
                    if i != len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                        num += roman[s[i]]*-1
                    else:
                        num += roman[s[i]]
                return int(num)
            print(romanToInt(roman))
        elif command.lower() == "new":
            print(f"\nWhat's New In Version {version}")
            for newthing in new:
                print(f"  *{newthing}")
            array = [element[0].capitalize() for element in new]
            print("Acronym: " + "".join(array) + "!\n")
        elif command.lower() == "userinfo":
            print(f"\nINFO ON {machine_name} AND {user['username']}@{machine_name}")
            print("KNOWN FACTS")
            print("\t*" + user["username"]
                  + f"@{machine_name} is an GoldplatedOS user.")
            print(
                "\t*" + user["username"] + f"@{machine_name} has downloaded {len(packages_installed)} packages.")
            print(
                "\t*" + user["username"] + f"@{machine_name} has typed {command_amount} commands.")
            print("UNKNOWN FACTS")
            print(
                "\t* Facts that are personal (we don't collect any info other than the above)\n")
        elif command.lower() == "calendar":
            calendar_app()
        elif command.lower() == user["password"]:
            print("That is your password!")
        elif command.lower() == "eggs":
            if eggs_on is True:
                print(random.choice(["🥚", "🪺", "🍳"]))
            else:
                print(package_error)
        elif command.lower() == "ascii_cub":
            if cub_on is True:
                print("""
 ^---^
 (0_0)
/(   )\\
 (___)
 // \\\\
                """)
            else:
                print(package_error)
        elif command.lower() == "mathgreekabc":
            if greek_on is True:
                print("𝞐𝞑𝞒𝞓𝞔𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞡𝞢𝞣𝞤𝞥𝞦𝞧𝞨")
                print("𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝜾𝜿𝝀𝝁𝝂𝝃𝝄𝝅𝝆𝝇𝝈𝝉𝝊𝝋𝝌𝝍𝝎𝝏𝝐𝝑𝝒𝝓𝝔𝝕")
            else:
                print(package_error)
        elif command.lower().startswith("command ") is True:
            if command_on is True:
                command = command.lower().replace("command ", "")
                print(os.system(command))
            else:
                print(package_error)
        elif command.lower().startswith("calc ") is True:
            if calc_on is True:
                command = command.lower().replace("calc ", "")
                print(eval(command))
            else:
                print(package_error)
        elif command.lower().startswith("timemachine ") is True:
            if time_on is True:
                command = command.lower().replace("timemachine ", "")
                if command.lower() == "1":
                    print("First year of CE starts.")
                elif command.lower() == "2":
                    print("Second year of CE starts.")
                elif command.lower() == "3":
                    print("Third year of CE starts.")
                elif command.lower() == "1066":
                    print("William the Conqueror invades England.")
                elif command.lower() == "1492":
                    print(
                        "Christopher Columbus sets off and will find the Americas instead of India.")
                elif command.lower() == "1500":
                    print("Christopher Columbus dies.")
                elif command.lower() == "1605":
                    print("Guy Fawkes is caught and arrested.")
                elif command.lower() == "1776":
                    print("The Declaration of Independence in America is signed.")
                elif command.lower() == "1861":
                    print("The American civil War starts.")
                elif command.lower() == "1900":
                    print("The turn of the century begins.")
                elif command.lower() == year:
                    print("You're living in it right now. Why would you need a timemachine for that?")
                elif command.lower() == "2070":
                    print("Who knows?")
                else:
                    print(
                        f"No event for year {command}. Try 1, 2, 3, 1066, 1492, 1500, 1605, 1776, 1861, 1900, this year, or 2070!")
            else:
                print(package_error)
        elif command.lower() == "requirements":
            print("REQUIREMENTS")
            print(
                "* a operating system to run your GoldplatedOS on (required | for whole GoldplatedOS)")
            print(
                "* a Python editor/compiler (required | for whole GoldplatedOS)")
            print("* wikipedia module (optional | for Netsurf app)")
        elif command.lower() == "calculator":
            calc_app()
        elif command.lower() == "passgen":
            passgen_app()
        elif command.lower() == "pycode":
            pycode_app()
        elif command.lower() == "numberguess":
            numberguess_app()
        elif command.lower() == "netsurf":
            netsurf_app()
        elif command.lower() == "textreader":
            textreader_app()
        elif command.lower() == "mymemos":
            list_app()
        elif command.lower() == "terminal":
            terminal_app()
        elif command.lower() == "music":
            music_app()
        elif command.lower() == "wordscramble":
            word_scramble_app()
        elif command.lower() == "security":
            security()
        elif command.lower() == "writeit":
            title = input("TITLE: ")
            file = open(f"{title}.cntnt", "a")
            while True:
                write = input("> ")
                if write.lower() == "quit":
                    file.close()
                    break
                else:
                    file.write(write + "\n")   
        elif command.lower() == "vim":
            print(os.system("vi"))
        elif command.lower() == "renamefile":
            file = input("Enter name of file: ")
            rename = input("Enter what it should be renamed to: ")
            os.rename(file, rename)
        elif command.lower() == "removefile":
            file = input("Enter name of file: ")
            os.remove(file)
        elif command.lower() == "filesize":
            file = input("Enter name of file: ")
            print(os.path.getsize(file), " bytes")
        elif command.lower() == "clear":
            os.system("clear")
            main()
        elif command.lower().startswith("man ") is True:
            man_needed = command.lower().replace("man ", "")
            print(
                f"Please consult the official manual The GoldplatedOS User's Manual for info on {man_needed}.")
        elif command.lower() == "apps":
            print("Calculator - Basic calculator that does simple addition/subtraction/multiplication/division problems.")
            print("Calendar - Simple but pretty text-based calendar app.")
            print("Music - Fun app for 4+ year olds to understand instruments.")
            print("MyMemos - Useful memo app that clears on shutdown.")
            print("Netsurf - Internet app that shows results from Wikipedia.")
            print("NumberGuess - Number guessing game.")
            print("PassGen - Generates password codes. Just for fun.")
            print("Pycode - Fun Python playground. Doesn't save.")
            print("Security - App for keeping everything secure!")
            print(
                "Terminal - the classic GoldplatedOS terminal that runs programming projects (and Unix) and downloads packages.")
            print("Textreader - Basic file reading app (only code and text files).")
            print(
                "Vim - Simple text editor based on Unix vi. GoldplatedOS developer did not create this app.")
            print("WriteIt - App for writing text files")
            print("Wordscramble - Fun game for unscrambling words.")
        elif command.lower() == "reboot":
            print("Restarting your GoldplatedOS...please wait...")
            reboot()
        elif command.lower() == "shutdown":
            print("Shutting down your GoldplatedOS...")
            exit(0)
        else:
            print(f"Invalid command '{command}'.")


if __name__ == '__main__':
    everything()