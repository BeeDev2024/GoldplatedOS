import tkinter as tk
from time import strftime
from tkinter import Label, filedialog

def update_clock():
    current_time = strftime('%H:%M')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every second

def check_password():
    password = "windy"  # Set your desired password here
    entered_password = password_entry.get()
    
    if entered_password == password:
        root.deiconify()
        login_screen.withdraw()
    else:
        incorrect_label.config(text="Incorrect password")

def open_file_explorer():
    file_path = filedialog.askopenfilename()
    if file_path:
        if file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                file_contents = file.read()
                display_text.config(text=file_contents)
        else:
            display_text.config(text="Selected file is not a text file")
    

# Create the login screen
login_screen = tk.Tk()
login_screen.geometry("500x500")
login_screen.title("Login")

password_label = tk.Label(login_screen, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(login_screen, show="*")
password_entry.pack()

login_button = tk.Button(login_screen, text="Login", command=check_password)
login_button.pack()

incorrect_label = tk.Label(login_screen, text="")
incorrect_label.pack()

# Hide the main window initially
root = tk.Tk()
root.title("GoldplatedOS")
root.geometry("500x500")
root.withdraw()

# Create a clock label
clock_label = Label(root, font=('calibri', 12, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='ne', padx=10, pady=10)

# Display text from selected file
display_text = Label(root, font=('calibri', 12), wraplength=400)
display_text.pack(pady=20)

file_explorer_button = tk.Button(root, text="Open File Explorer", command=open_file_explorer)
file_explorer_button.pack()

# Update the clock initially and start the update loop
update_clock()

# Run the main loop for the login screen
login_screen.mainloop()
