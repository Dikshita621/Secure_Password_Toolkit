import customtkinter as ctk

#appearance mode
ctk.set_appearance_mode("System")  # "Light", "Dark", or "System"
#default color theme
ctk.set_default_color_theme("blue")

#the main window
app = ctk.CTk()

# Window title
app.title("Secure Password Toolkit")

# Window size
app.geometry("900x650")

# Prevent resizing
app.resizable(False, False)

# Run the application
app.mainloop()