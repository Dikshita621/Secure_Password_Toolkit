import customtkinter as ctk
# the main application window
app = ctk.CTk()

# Window title
app.title("Secure Password Toolkit")

# Window size (Width x Height)
app.geometry("900x650")

# Prevent resizing (optional)
app.resizable(False, False)

# Start the application
app.mainloop()