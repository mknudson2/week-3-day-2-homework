import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Game Boy Color")
window.geometry("320x288")  # Adjust the size to match the Game Boy Color screen resolution

# Create a frame to hold the Game Boy Color screen
screen_frame = tk.Frame(window, bg="lightgray", width=160, height=144)
screen_frame.pack(padx=20, pady=20)

# Create a label to represent the Game Boy Color logo
logo_label = tk.Label(screen_frame, text="Game Boy Color", font=("Arial", 14, "bold"), bg="darkgray", fg="white")
logo_label.pack(pady=20)

# Add any additional widgets or elements to mimic the Game Boy Color interface

# Start the Tkinter event loop
window.mainloop()
