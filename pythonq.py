# using python program create a function if input is 1 create a folder on desktop
# if input is 2 = create a file on desktop
# if input is 3 = whatsapp your friend with a msg
"tera account hack kr liya"
# if input is 4 = shut down the system 


import os
import datetime
import pywhatkit
import platform

def take_action(choice):
    # Get the Desktop path for the current user
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    if choice == 1:
        folder_name = "MyFolder"
        path = os.path.join(desktop, folder_name)
        os.makedirs(path, exist_ok=True)
        print(f"Folder created at: {path}")

    elif choice == 2:
        file_name = "my_file.txt"
        file_path = os.path.join(desktop, file_name)
        with open(file_path, "w") as file:
            file.write("This is a test file created by Python.")
        print(f"File created at: {file_path}")

    elif choice == 3:
        # Change this number to your friend's number (include country code)
        phone_number = "+91xxxxxxxxxx"  # Replace with a real number
        message = "Hey! Just testing a Python script."
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  # Send 1 minute later to allow processing
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled.")

    elif choice == 4:
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /s /t 10")  # 10 seconds delay
        elif system == "Linux" or system == "Darwin":
            os.system("shutdown -h now")
        else:
            print("Unsupported OS for shutdown command.")
    else:
        print("Invalid choice.")

# Example usage:
try:
    user_choice = int(input("Enter your choice (1-4): "))
    take_action(user_choice)
except ValueError:
    print("Please enter a valid number.")

