import tkinter as tk
from tkinter import messagebox

from pypylon import pylon


# Search for available cameras
factory = pylon.TlFactory.GetInstance()
devices = factory.EnumerateDevices()


def select_camera():
    # Get the selected row from the list
    selected_items = camera_listbox.curselection()

    if not selected_items:
        messagebox.showwarning(
            "No camera selected",
            "Please select a camera first."
        )
        return

    # curselection returns positions such as (0,)
    selected_index = selected_items[0]

    # Get the corresponding pylon device information
    selected_device = devices[selected_index]

    model = selected_device.GetModelName()
    serial_number = selected_device.GetSerialNumber()

    messagebox.showinfo(
        "Camera selected",
        f"Model: {model}\nSerial number: {serial_number}"
    )


# Create the main window
root = tk.Tk()
root.title("Select Basler Camera")
root.geometry("500x300")


title_label = tk.Label(
    root,
    text="Available cameras",
    font=("Arial", 16)
)
title_label.pack(pady=15)


camera_listbox = tk.Listbox(
    root,
    width=60,
    height=8,
    font=("Arial", 11)
)
camera_listbox.pack(padx=20, pady=10)


# Add every detected camera to the listbox
for device in devices:
    camera_description = (
        f"{device.GetModelName()} | "
        f"Serial: {device.GetSerialNumber()} | "
        f"Type: {device.GetDeviceClass()}"
    )

    camera_listbox.insert(tk.END, camera_description)


select_button = tk.Button(
    root,
    text="Open Selected Camera",
    command=select_camera,
    width=25,
    height=2
)
select_button.pack(pady=15)


# Show a message if no cameras were detected
if len(devices) == 0:
    camera_listbox.insert(tk.END, "No cameras detected")
    select_button.config(state=tk.DISABLED)


# Start the Tkinter application
root.mainloop()